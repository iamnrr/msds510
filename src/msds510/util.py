import datetime as dt


def get_month(input):

    '''
    Function takes an input string from the intro field and returns the integer month
    Arguments: input string from the intro field
    return: integer month
    Execution: call as get_month(intro_field)
    '''

    if input[0:1].isdigit():
        # check the position of "-" to handle - intro='5-May'
        pos = input.find('-', 0)
        if pos == 1:
            ni = '0'+input
            Introdt = dt.datetime.strptime(ni, '%y-%b')
            return Introdt.month

        else:
            Introdt = dt.datetime.strptime(input, '%y-%b')
            return Introdt.month

    else:
        Introdt = dt.datetime.strptime(input, '%b-%y')
        return Introdt.month


def get_date_joined(yr, mth):

    '''
    Function to return a Python datetime.date of when the character joined the Avengers
    Arguments: 2 - year & month
    return: date (join date)
    Execution: get_date_joined(year, month)
    '''

    jmnth = get_month(mth)
    joindt = dt.date(int(yr),jmnth,1 )  # prints in as 2018-05-01
    strdt = 'datetime.date('+str(yr)+ ', ' + str(jmnth) + ', ' + str(1) + ')'
    return strdt


def days_since_joined(yr, mth):

    '''
    Function to return the integer number of days since the character joined the Avengers from today's date
    Arguments: 2 - year & month
    return: integer (number of days since joined)
    Execution: days_since_joined(year, month)
    '''

    d1 = dt.date.today()
    d2 = dt.date(int(yr), get_month(mth), 1)
    return (d1-d2).days
