import msds510.util as u

records = [
            dict(year='1988', intro='Jun-88'),
            dict(year='1989', intro='May-89'),
            dict(year='2005', intro='5-May'),
            dict(year='2013', intro='13-Nov'),
            dict(year='2014', intro='14-Jun')
          ]


def main():

    '''
    Function to test the "util.py" module
    Arguments: none
    return: none
    Execution: test_util_module.py
    '''

    print('\n')
    for i in range(len(records)):

        print('Input Record - ', end='')
        print(records[i])
        jyr = records[i]['year']
        jmt = records[i]['intro']
        print('Date joined - ', end='')
        jdtstr = u.get_date_joined(jyr, jmt)
        if len(str(u.get_month(jmt))) == 2:
            newjdst = str(jyr) + '-' + str(u.get_month(jmt))+'-01'
        else:
            newjdst = str(jyr) + '-0' + str(u.get_month(jmt))+'-01'
        print(newjdst)

        print('Days since joined - ', end='')
        print((u.days_since_joined(jyr, jmt)))
        print('\n')


if __name__ == "__main__":

    main()
