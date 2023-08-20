import datetime as dt
import re
import datetime as dt
import random
import pandas as pd
import openpyxl

def read_lopgfile(logfile):
    for line in logfile:
        if 'INFO get credit request' in line:
          date=dt.datetime.strptime(line[:13], '%Y-%m-%d %H')
          hours_dict[date].append(line)
    for date in hours_list:
        potrebs=0
        autos=0
        mortgages=0
        for i in hours_dict[date]:
            if 'potreb' in i:
                potrebs+=1
            elif 'auto' in i:
                autos+=1
            elif 'mortgage' in i:
                mortgages+=1
        res[date][0] = potrebs
        res[date][1] = autos
        res[date][2] = mortgages

        #res[date][0] = hours_dict[date].count('potreb')



def generate_dates_range(start_date, end_date) -> list: #функция генерит список часов по которым будут группироваться запросы
    date_1 = min(start_date, end_date)
    date_2 = max(start_date, end_date)
    dates_list=[date_1]
    while date_1<date_2:
        date_1+=dt.timedelta(hours=1)
        dates_list.append(date_1)
    return dates_list




if __name__ == '__main__':
    start_date = dt.datetime(2023, 1, 1, 0)
    end_date = dt.datetime(2023, 4, 1, 23)
    hours_dict={}
    res={}
    hours_list = generate_dates_range(start_date, end_date)

    for i in hours_list:
        hours_dict[i]=[]
    for i in hours_list:
        res[i]=[0, 0, 0]


    logfile = open("LOGS.txt", "r")
    read_lopgfile(logfile)
    logfile.close()

    profile_table = pd.DataFrame(
        res
    )
    profile_table.to_excel('./profile.xlsx', sheet_name='profile', index='false')

    for i in hours_list:
        print(str(i)+' '+str(res[i]))





