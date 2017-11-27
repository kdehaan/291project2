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
<<<<<<< HEAD
    match_other = re.compile(r"other:")
    terms = db.DB()
    terms.open("terms.idx", None, db.DB_BTREE, db.DB_CREATE)
    years = db.DB()
    years.open("years.idx", None, db.DB_BTREE, db.DB_CREATE)
    recs = db.DB()
    recs.open("recs.idx", None, db.DB_HASH, db.DB_CREATE)



    while True:
        recscur = recs.cursor()
        yearscur = years.cursor()
        termscur = terms.cursor()
=======
    match_other = re.compile(r":")

    while True:
        terms = db.DB()
        terms.open("terms.idx", None, db.DB_BTREE, db.DB_CREATE)
        termscur = terms.cursor()
        years = db.DB()
        years.open("years.idx", None, db.DB_BTREE, db.DB_CREATE)
        yearscur = years.cursor()
        recs = db.DB()
        recs.open("recs.idx", None, db.DB_HASH, db.DB_CREATE)
        recscur = recs.cursor()
>>>>>>> moreparsing
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
<<<<<<< HEAD
                print("general term found")

        termscur.close()
        yearscur.close()
        recscur.close()


    terms.close()
    years.close()
    recs.close()

=======
                search_term = item
                print(item)
>>>>>>> moreparsing


        terms.close()
        years.close()
        recs.close()
        termscur.close()
        yearscur.close()
        recscur.close()

if __name__ == "__main__":
    main()