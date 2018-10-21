import sys


def  convert(inputfile, outputfile):

    '''
    Function to convert data in csv file encoded in 'ISO-8859-1' to 'utf-8' and save in another csv
    Arguments: 2 -  source file and  target file
    inputfile contains the file path and name of the source file that need to be converted
    outputfile contains the file path and name of the destination file
    return: none
    Execution:  python convert_to_utf8.py ../data/raw/avengers.csv ../data/interim/avengers_utf8.csv
    '''

    in_avengers = open(inputfile, encoding='iso-8859-1')
    in_data = in_avengers.read()
    out_data = in_data.encode('utf8')

    out_avengers = open(outputfile, 'wb')
    out_avengers.write(out_data)

    in_avengers.close()
    out_avengers.close()

    print('File avengers_utf8.csv created with utf-8 encoded data')
    print("avengers_utf8.csv copied to destination directory")


def main():

    '''
    main function to call the convert function
    :return: none
    '''

    convert(sys.argv[1], sys.argv[2])

if __name__  == "__main__":

    main()
