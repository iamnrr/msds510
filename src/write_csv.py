import sys
import csv


def writedict(inputfile, outputfile):
    '''
    Function to read data from one csv and write to another csv file after cleansing the fieldnames
    Arguments: 2 -  source file and  target file
    return: none
    Execution: python write_csv.py ../data/interim/avengers_utf8.csv ../data/processed/avengers_processed.csv
    '''

    with open(outputfile,  mode='w') as wfile:

        with open(inputfile, newline='') as rfile:
            reader = csv.DictReader(rfile)
            header = reader.fieldnames
            rows = list(reader)
            new_header = []

            for item in header:
                new_header.append(item.lower().replace('/', '_').replace('?', '').replace(' ', '_').strip())

            writer = csv.DictWriter(wfile, lineterminator='\n', fieldnames=new_header)
            writer.writeheader()

            for i in range(len(rows)):
                orddict = rows[i]
                rowlist = []

                for key, value in orddict.items():
                    rowlist.append(value)

                nd = dict(zip(new_header, rowlist))
                writer.writerow(nd)

    print('File avengers_processed.csv created and copied ')


def main():

    '''
    main function to call the writedict function
    :return: none
    '''

    writedict(sys.argv[1], sys.argv[2])


if __name__ == "__main__":

    main()
