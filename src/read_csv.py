import sys
import csv


def readcsv(inputfile):

    with open(inputfile, newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        print(rows[161]) # row 162 means index is 161 in list

def main():

    readcsv(sys.argv[1])

if __name__ == "__main__":

    main()
