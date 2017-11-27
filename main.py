# import subprocess
# from bsddb3 import db
import re


def get_queries():
    sel = input("Enter your database search: ").lower()
    parse_input = re.compile(r"([\w]+:[\w]+|year.{1,2}[\d]{4}|title:\".+\"|output=[\w]{3,4}|[\w]+)")
    input_iter = parse_input.finditer(sel)
    queries = list()
    for item in input_iter:
        queries.append(item.group())
    return queries

def main():
    output_type = 'key'
    match_title = re.compile(r"title:")
    match_author = re.compile(r"author:")
    match_year = re.compile(r"year[:<>]")
    match_other = re.compile(r"other:")
    while True:
        queries = get_queries()
        for item in queries:
            if item == "output=key":
                output_type = 'key'
                print("changed output (key)")
            elif item == "output=full":
                output_type = 'full'
                print("changed output")
            elif match_title.match(item):
                print("title found")
            elif match_author.match(item):
                print("author found")
            elif match_year.match(item):
                print("year found")
            elif match_other.match(item):
                print("other found")
            else:
                print("general term found")








if __name__ == "__main__":
    main()