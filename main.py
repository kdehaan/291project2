import subprocess
from bsddb3 import db
import re


def get_queries():
    sel = input("Enter your database search. To see query options, enter h. To quit, enter q: ").lower()
    parse_input = re.compile(r"([\w]+:[\w]+|year.{1,2}[\d]{4}|title:\".+\"|output=[\w]{3,4}|[\w]+)")
    input_iter = parse_input.finditer(sel)
    queries = list()
    for item in input_iter:
        queries.append(item.group())
    return queries

def main():


    done = False
    output = 'key'
    while not done:
        goodin = False
        queries = get_queries()
        answerparted = False
        answers = []
        counter = 0
        lastend = 0
        answercount = 0
        for i in answer:
            word = ''
            if i == ' ' or ord(i) == 10:
                for m in range(lastend, counter):
                    word += answer[m]
                answers[answercount] = word
            counter += 1

        counter = 0
        queryspots = []
        for i in answers:
            if ':' in i or '>' in i or '<' in i:
                queryspots.append(counter)


            counter += 1
            if i == 'q':
                print("Exiting program...\n")
                done = True
                goodin = True
            elif i == 'h':
                print('\nQuery options: (Enter the query type, then a colon, then the query. Multiple queries should be separated by a space)'
                      '\nTitle: Search by title, or words in title. \nAuthor: Search by author. \n'
                      'Year: Search by year. Can be equality search or range search. '
                      '\nOutput=full: Set output format to print entire entry. \nOutput=key: Set output to only show key. \n')
            elif i == 'output=full':
                output = 'full'
            elif i == 'output=key':
                output = 'key'

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
                elif '>' in i or '<' in i:
                    checkfound = True
                    querytype += m
                else:
                    querytype += m
                mspot += 1
            if checkfound:
                querylist.append([querytype, value])


        for i in querylist:
            if not done:
                if i[0] == 'title':
                    pass
                elif i[0] == 'author':
                    pass
                elif i[0] == 'year<':
                    pass
                elif i[0] == 'year>':
                    pass
                elif i[0] == 'year':
                    pass
                if i == title:
                    pass







if __name__ == "__main__":
    main()