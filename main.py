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

def get_year(yearscur, year, qualifier):
    result_set = set()
    if qualifier == ':':
        result = yearscur.get(year, year, db.DB_SET)
    elif qualifier == '<':
        result = yearscur.setrange(year, db.DB_SET)
    curs_iter = result

    while curs_iter[0] == year:
        result_set.add(curs_iter[1].decode('utf-8'))
        curs_iter = yearscur.next()
        if not curs_iter:
            curs_iter = ['', '']

    return result_set



def get_data(termscur, search_term):
    result = termscur.get(search_term, search_term, db.DB_SET)
    curs_iter = result
    result_set = set()
    if not result:
        return {}
    while curs_iter[0] == search_term:
        result_set.add(curs_iter[1].decode('utf-8'))
        curs_iter = termscur.next()
        if not curs_iter:
            curs_iter = ['', '']
    return result_set

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


        set_list = list()
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
                        term = term.encode('utf-8')
                        set_list.append(get_data(termscur, term))
                else:
                    search_term = item[6:]
                    search_term = 't-' + search_term
                    search_term = search_term.encode('utf-8')
                    set_list.append(get_data(termscur, search_term))
            elif match_author.match(item):
                search_term = item[7:]
                search_term = 'a-' + search_term
                set_list.append(get_data(termscur, search_term))
            elif match_year.match(item):
                equality = item[4]
                search_term = item[5:]
                search_term = search_term.encode('utf-8')
                set_list.append(get_year(yearscur, search_term, equality))
            elif match_other.search(item):
                search_term = item.split(':')
                search_term = search_term[1]
                search_term = 'o-' + search_term
                set_list.append(get_data(termscur, search_term))
            else:
                search_term_1 = 'o-' + item
                search_term_2 = 'a-' + item
                search_term_3 = 't-' + item
                data1 = get_data(termscur, search_term_1.encode('utf-8'))
                if data1:
                    set_list.append(data1)
                data2 = get_data(termscur, search_term_2.encode('utf-8'))
                if data2:
                    set_list.append(data2)
                data3 = get_data(termscur, search_term_3.encode('utf-8'))
                if data3:
                    set_list.append(data3)

        net_set = set()
        for setitem in set_list:
            if len(net_set) == 0:
                net_set = setitem
            else:
                net_set = net_set & setitem

        if output_type == 'key':
            for setitem in net_set:
                print(setitem)
        if output_type == 'full':
            for setitem in net_set:
                search_term = setitem.encode('utf-8')
                result = recs.get(search_term)
                print(result)





        termscur.close()
        yearscur.close()
        recscur.close()



if __name__ == "__main__":
    main()