

import datetime as dt

def get_month(input):

    if input[0:1].isdigit():
        #print('position is ' + str(input.find('-', 0)))
        pos = input.find('-', 0)
        if pos == 1:
            ni = '0'+input
            Introdt = dt.datetime.strptime(ni, '%y-%b')
            return(Introdt.month)

        else:
            Introdt = dt.datetime.strptime(input, '%y-%b')
            return(Introdt.month)

    else :
        Introdt = dt.datetime.strptime(input, '%b-%y')
        return(Introdt.month)


def get_date_joined(yr, mth):

    jmnth = get_month(mth)

    joindt = dt.date(int(yr),jmnth,1 )  # prints in as 2018-05-01

    strdt = 'datetime.date('+str(yr)+ ', ' + str(jmnth) + ', ' + str(1) + ')'

    return(strdt)


def days_since_joined(yr, mth):

    d1 = dt.date.today()

    d2 = dt.date(int(yr),get_month(mth),1 ) #get_date_joined(yr, mth)

    return((d1-d2).days)

# def main():
#
#     print("i m in main")
#
#     #it's easy to print this list of course:
#     print(sys.argv)
#
#     #or it can be iterated via a for loop:
#
#     for i in range(len(sys.argv)):
#         if i == 0:
#             print("Function name: %s" % sys.argv[0])
#         else:
#             print("%d. argument: %s" % (i, sys.argv[i]))
#
#
#     mnth = get_month(sys.argv[2])
#     print(mnth)
#
#     jdate = get_date_joined(sys.argv[1], sys.argv[2])
#     print(jdate)
#
#     jdays = days_since_joined(sys.argv[1], sys.argv[2])
#     print('days difference :\t')
#     print(jdays)
#
#     print('read')
#
#
# if __name__ == "__main__":
#
#     main()
