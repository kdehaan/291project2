import sys
import re
import subprocess

def sort_data(filename):
    outstr = '-o' + filename
    subprocess.Popen(['sort', '-u', outstr, filename])


def parse_data():

    # while True:
    #     sel = input("Select file (F) or input from stdin (S): ").lower()
    #     if sel == "f":
    #         filename = input("enter file location: ")
    #         if not filename:
    #             filename = '/testxml.xml'
    #         f = open(filename, 'r')
    #         data = f.read()
    #         f.close()
    #         break
    #     elif sel == "s":
    #         data = sys.stdin
    #         break

    data = sys.stdin.read()
    # example usage on linux: cat 10.txt | python3 main.py

    return data


def prepare_files(data):
    create_terms(data)
    create_years(data)
    create_recs(data)


def create_terms(data):
    # articles = re.compile('<article.*/article>')
    # result = articles.match(data)

    line = "Cats are smarter than dogs";

    searchObj = re.search(r'(.*)a(.*?) .*', data, re.M | re.I)

    if searchObj:
        print(searchObj.group())
        for item in searchObj.groups():
            print(item)


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


def setup():
    return




def main():
    #data = parse_data()
    #prepare_files(data)
    sort_data('terms.txt')
    sort_data('years.txt')
    sort_data('recs.txt')


if __name__ == "__main__":
    main()