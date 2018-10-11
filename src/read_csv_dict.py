import sys
import csv


def readdict(inputfile):

    with open(inputfile, newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        orddict161 = rows[160]
        dict161 = dict(orddict161)
        #print(rows[160])  # prints row 161th record (index of records starts from 0) as ordered dict
        print(dict161)    # prints row 161th record as dict


def main():

    readdict(sys.argv[1])

if __name__ == "__main__":

    main()
