import sys
import csv


def readcsv(inputfile):

    '''
    Function to read the csv file and print 162nd row
    Arguments: File path and name to be read
    return: none
    Execution: python read_csv.py ../data/interim/avengers_utf8.csv
    '''

    with open(inputfile, newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        print(rows[161])  # row 162 means index is 161 in list


def main():

    '''
    main function to call the readcsv function
    :return: none
    '''

    readcsv(sys.argv[1])

if __name__  == "__main__":

    main()
