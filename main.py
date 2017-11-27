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
    match_other = re.compile(r":")
    terms = db.DB()
    terms.open("terms.idx", None, db.DB_BTREE, db.DB_CREATE, db.DB_DUP)
    years = db.DB()
    years.open("years.idx", None, db.DB_BTREE, db.DB_CREATE, db.DB_DUP)
    recs = db.DB()
    recs.open("recs.idx", None, db.DB_HASH, db.DB_CREATE, db.DB_DUP)


    while True:
        termscur = terms.cursor()
        yearscur = years.cursor()
        recscur = recs.cursor()
        queries = get_queries()

        for item in queries:
            if item == "output=key":
                output_type = 'key'
                print("changed output (key)")
            elif item == "output=full":
                output_type = 'full'
                print("changed output (full)")
            elif match_title.match(item):
                if '"' in item:
                    search_term = item[7:-1]
                    search_terms = search_term.split()
                    for term in search_terms:
                        term = 't-' + term
                        print(term)
                else:
                    search_term = item[6:]
                    search_term = 't-' + search_term
                    result = termscur.get(search_term)
                    print(result)
                    print(search_term)
            elif match_author.match(item):
                search_term = item[7:]
                search_term = 'a-' + search_term
                print(search_term)
            elif match_year.match(item):
                equality = item[4]
                search_term = item[5:]
                if equality == ':':
                    continue
                if equality == '<':
                    continue
                if equality == '>':
                    continue
                print(search_term)
            elif match_other.search(item):
                search_term = item.split(':')
                search_term = search_term[1]
                search_term = 'o-' + search_term
                print(search_term)
            else:
                print("general term found")




        termscur.close()
        yearscur.close()
        recscur.close()



if __name__ == "__main__":
    main()