import sys
import re
import subprocess
from bsddb3 import db

def fill_db(database, curs, filename):
    #outstr = '-o' + filename
    sort = subprocess.Popen(['sort', '-u', filename], stdout=subprocess.PIPE)
    for line in sort.stdout:
        key = ''
        value = ''
        if line[0] == 10:
            pass
        else:
            keyfound = False
            count = -1
            while not keyfound:
                count += 1
                if line[count] == 58:
                    keyfound = True
                else:
                    key += chr(line[count])
            valuefound = False
            while not valuefound:
                count += 1
                if line[count] == 10:
                    valuefound = True
                else:
                    value += chr(line[count])
            key = key.encode('utf-8')
            database.put(key, value)

def uncaps(answer):
    count = 0
    for i in answer:
        if ord(i) > 64 and ord(i) < 91:
            answer[count] = chr(ord(i) + 32)
        count += 1
    return answer

def print_db(db):
    curs = db.cursor()
    iter = curs.first()
    while iter:
        print(iter)
        iter = curs.next()

def clear_db(database, curs):
    iter = curs.first()
    while (iter):
        curs.delete()
        iter = curs.first()

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
    terms.open("terms.idx",None, db.DB_BTREE, db.DB_CREATE)
    termscur = terms.cursor()
    years = db.DB()
    years.open("years.idx",None, db.DB_BTREE, db.DB_CREATE)
    yearscur = years.cursor()
    recs = db.DB()
    recs.open("recs.idx",None, db.DB_HASH, db.DB_CREATE)
    recscur = recs.cursor()

    clear = uncaps(input("Would you like to clear the databases and remake them, or use the existing databases? [Y/N] "))
    if clear == 'y':
        clear_db(recs, recscur)
        clear_db(years, yearscur)
        clear_db(terms, termscur)
        fill_db(terms, termscur, 'terms.txt')
        fill_db(years, yearscur, 'years.txt')
        fill_db(recs, recscur, 'recs.txt')

    done= False
    while not done:
        goodin = False
        answer = uncaps(input("Enter your database search. To see query options, enter h. To quit, enter q: "))
        answerparted = False
        answers = []
        counter = 0
        lastend = 0
        answercount = 0
        for i in answer:
            word = ''
            if i == ' ' or ord(i) == 8:
                for m in range(lastend, counter):
                    word += answer[m]
                answers[answercount] = word
            counter += 1

        counter = 0
        queryspots = []
        for i in answers:
            if ':' in i:
                querylist.apend(counter)
            counter += 1
            if i == 'q':
                print("Exiting program...\n")
                done = True
                goodin = True

        querylist = []
        for i in queryspots:
            querytype = ''
            value = ''
            checkfound = False
            for m in answers[i]:
                if checkfound:
                    value += m
                elif m == ':':
                    checkfound = True
                else:
                    querytype += m
            querylist.append([querytype, value])


        for i in range(0, size(answers)):
            if not done:
                if answers[i] == 'h':
                    print('\nQuery options: (Enter the query type, then a colon, then the query)'
                          '\nTitle: Search by title. \nAuthor: Search by author. \n'
                          'Year: Search by year. Can be equality search or range search. '
                          '\nOutput=full: Set output format to print entire entry. \nOutput=key: Set output to only show key. \n')
                    goodin = True
                elif answer[i] == 'q':
                    print("Exiting program...\n")
                    done = True
                    goodin = True
                elif answer[i]




    terms.close()
    years.close()
    recs.close()
    termscur.close()
    yearscur.close()
    recscur.close()



if __name__ == "__main__":
    main()