import re
import sys
from xml_object import XmlObject


def parse_data():

    data = sys.stdin.read()
    # example usage on linux: cat 10.txt | python3 part1.py

    return data


def prepare_files(data):

    terms_file = open("terms.txt", "w")
    years_file = open("years.txt", "w")
    recs_file = open("recs.txt", "w")

    re_object = re.compile(r'<.*>')
    re_xmlheader = re.compile(r'(<\?xml|<!DOCTYPE|</dblp>)')
    re_key = re.compile(r'(?<=key=\").*(?=\">)')
    re_tags = re.compile(r'(?=(<[\w]+>)).*?(?=</)')
    re_pages = re.compile(r'<pages>')
    re_title = re.compile(r'<title>')
    re_author = re.compile(r'<author>')
    re_year = re.compile(r'<year>')
    re_terms = re.compile(r'[0-9a-zA-Z_]{3,}')

    search_obj = re_object.finditer(data, re.M | re.I)

    if search_obj:
        for item in search_obj:
            if re_xmlheader.match(item.group()):
                continue
            xml = XmlObject(item.group())
            xml.key = re_key.search(xml.raw_string).group()
            tags = re_tags.finditer(xml.raw_string)
            for tag in tags:
                raw_tag = tag.group()
                if re_pages.match(raw_tag):
                    continue

                elif re_year.match(raw_tag):
                    xml.year = raw_tag[6:]
                    continue

                elif re_title.match(raw_tag):
                    titles = re_terms.finditer(raw_tag)
                    next(iter(titles))
                    for term in titles:
                        xml.title_terms.append(term.group().lower())

                elif re_author.match(raw_tag):
                    authors = re_terms.finditer(raw_tag)
                    next(iter(authors))
                    for term in authors:
                        xml.author_terms.append(term.group().lower())

                else:
                    others = re_terms.finditer(raw_tag)
                    next(iter(others))
                    for term in others:
                        xml.other_terms.append(term.group().lower())

            for title in xml.title_terms:
                line_string = 't-' + title + ':' + xml.key + '\n'
                terms_file.write(line_string)

            for other in xml.other_terms:
                line_string = 'o-' + other + ':' + xml.key + '\n'
                terms_file.write(line_string)

            for author in xml.author_terms:
                line_string = 'a-' + author + ':' + xml.key + '\n'
                terms_file.write(line_string)

            year_string = xml.year + ':' + xml.key + '\n'
            years_file.write(year_string)

            rec_string = xml.key + ':' + xml.raw_string + '\n'
            rec_string.replace("\\", "&#92;")
            recs_file.write(rec_string)


    # regex:
    # article block: <article.*/article>
    # article key: (?<=key=\").*(?=\")
    # terms: [0-9a-zA-Z_]{3,}
    # authors: (?<=<author>).*?(?=</)
    # title: (?<=<title>).*?(?=</)
    # contained tags with titles (?=(<[\w]+>)).*?(?=</)
    return


def create_years(data):
    return


def create_recs(data):
    return


def main():
    data = parse_data()
    prepare_files(data)


if __name__ == "__main__":
    main()