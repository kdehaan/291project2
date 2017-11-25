import sys
import re
import subprocess
from bsddb3 import db

def fill_db(database, curs, filename):
    #outstr = '-o' + filename
    sort = subprocess.Popen(['sort', '-u', filename], stdout=subprocess.PIPE)
    for line in sort.stdout:


def clear_db(database, curs):
    iter = curs.first()
    while (iter):
        iter.delete()
        iter = curs.next()

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
    terms = db.DB()
    terms.open("terms.db",None, db.DB_BTREE, db.DB_CREATE)
    termscur = terms.cursor()
    years = db.DB()
    years.open("years.db",None, db.DB_BTREE, db.DB_CREATE)
    yearscur = years.cursor()
    recs = db.DB()
    recs.open("recs.db",None, db.DB_HASH, db.DB_CREATE)
    recscur = recs.cursor()

    clear = input("Would you like to clear the databases and remake them, or use the existing databases? [Y/N] ").lower()
    if clear == 'y':
        clear_db(recs, recscur)
        clear_db(years, yearscur)
        clear_db(terms, termscur)
        fill_db(terms, termscur, 'terms.txt')
        fill_db(years, yearscur, 'years.txt')
        fill_db(recs, recscur, 'recs.txt')







    terms.close()
    years.close()
    recs.close()
    termscur.close()
    yearscur.close()
    recscur.close()



if __name__ == "__main__":
    main()