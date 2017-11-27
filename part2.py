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


def clear_db(database, curs):
    iter = curs.first()
    while (iter):
        curs.delete()
        iter = curs.first()

def main():
    terms = db.DB()
    terms.open("terms.idx", None, db.DB_BTREE, db.DB_CREATE)
    termscur = terms.cursor()
    years = db.DB()
    years.open("years.idx", None, db.DB_BTREE, db.DB_CREATE)
    yearscur = years.cursor()
    recs = db.DB()
    recs.open("recs.idx", None, db.DB_HASH, db.DB_CREATE)
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