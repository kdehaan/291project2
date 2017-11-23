import sys


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

    data = sys.stdin.readlines()
    # example usage on linux: cat 10.txt | python3 main.py

    return data


def setup():
    return




def main():
    data = parse_data()
    for line in data:
        print(line)


if __name__ == "__main__":
    main()