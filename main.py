# import subprocess
from bsddb3 import db
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
        terms = db.DB()
        terms.open("terms.idx", None, db.DB_BTREE, db.DB_CREATE)
        termscur = terms.cursor()
        queries = get_queries()

        for item in queries:
            if item == "output=key":
                output_type = 'key'
                print("changed output (key)")
            elif item == "output=full":
                output_type = 'full'
                print("changed output")
            elif match_title.match(item):
                if '"' in item:
                    print("multival")
                    search_term = item[7:-1]
                    print(search_term)
                else:
                    search_term = item[6:]
                    print(search_term)
            elif match_author.match(item):
                search_term = item[7:]
                print(search_term)
            elif match_year.match(item):
                equality = item[4]
                search_term = item[5:]
                print(search_term)
            elif match_other.match(item):
                search_term = item[6:]
                print(search_term)
            else:
                search_term = item
                print(item)



if __name__ == "__main__":
    main()