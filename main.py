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
        if 64 < ord(i) < 91:
            answer[count] = chr(ord(i) + 32)
        count += 1
    return answer

def print_db(db):
    curs = db.cursor()
    iter_curs = curs.first()
    while iter_curs:
        print(iter_curs)
        iter_curs = curs.next()

def clear_db(database, curs):
    iter = curs.first()
    while (iter):
        curs.delete()
        iter = curs.first()



def main():
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
                queryspots.append(counter)
            counter += 1
            if i == 'q':
                print("Exiting program...\n")
                done = True
                goodin = True
            elif i == 'h':
                print('\nQuery options: (Enter the query type, then a colon, then the query. Multiple queries should be separated by a space)'
                      '\nTitle: Search by title. \nAuthor: Search by author. \n'
                      'Year: Search by year. Can be equality search or range search. '
                      '\nOutput=full: Set output format to print entire entry. \nOutput=key: Set output to only show key. \n')

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


        for i in querylist:
            if not done:
                if i == title:
                    




    terms.close()
    years.close()
    recs.close()
    termscur.close()
    yearscur.close()
    recscur.close()



if __name__ == "__main__":
    main()