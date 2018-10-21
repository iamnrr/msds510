import sys
import csv


def readdict(inputfile):

    '''
    Function to read the csv file and print 162nd record with field names using csv.DictReader
    Arguments: File path and name to be read
    return: none
    Execution: python read_csv_dict.py ../data/interim/avengers_utf8.csv
    '''

    with open(inputfile, newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        orddict161 = rows[160]
        dict161 = dict(orddict161)
        print(dict161)    # prints row 161th record as dict


def main():

    '''
    main function to call the readdict function
    :return: none
    '''

    readdict(sys.argv[1])

if __name__  == "__main__":

    main()
