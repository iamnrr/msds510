import sys


# Function takes 2 inputs - one source file and another target file
def convert(inputfile, outputfile):

    in_avengers = open(inputfile, encoding='iso-8859-1')
    in_data = in_avengers.read()
    out_data = in_data.encode('utf8')

    out_avengers = open(outputfile, 'wb')
    out_avengers.write(out_data)

    in_avengers.close()
    out_avengers.close()


def main():

    convert(sys.argv[1], sys.argv[2])

if __name__ == "__main__":

    main()
