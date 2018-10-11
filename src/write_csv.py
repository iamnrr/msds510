import sys
import csv


# Function takes 2 inputs - one source file and another target file
def writedict(inputfile, outputfile):

    with open(outputfile,  mode = 'w') as wfile:

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

def main():

    writedict(sys.argv[1], sys.argv[2])


if __name__ == "__main__":

    main()
