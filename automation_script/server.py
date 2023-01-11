import pandas as pd
import threading


def list_to_dict(a):
    it = iter(a)
    ret_dict = dict(zip(it, it))
    return ret_dict


def printit(skip, loops, cookie):
    t= threading.Timer(5.0, printit, [skip+1, loops-1, cookie])
    sheet_id = "1r6HcTiOPP9tVCjsFV1DZtNVGSYF7wGCpdNheCbpVVZo"
    sheet_name = "campaign01_01"
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    t.start()
    # t.cancel() #to stop timer
    df = pd.read_csv(url, skiprows=skip, nrows=0)
    print("----------------- cookie -----------------")
    print(cookie)
    print(skip)
    skip = skip+1
    print(loops)
    loops = loops-1
    print("----------------------- New Entry in DataFrame -------------------------")
    # print(df.columns.to_list())
    csv_list.append(df.columns.to_list())
    print(csv_list)
    if loops < 1:
        t.cancel()
        return loops


cookies = {'cookie1': 'wwwwwwwwwwwwwwwwwwww',
           'cookie2': 'eeeeeeeeeeeeeeeeeee',
           'cookie3': 'sssssssssssssssssssss',
           'cookie4': 'qqqqqqqqqqqqqqqqq',
           'cookie5': 'kkkkkkkkkkkkkkkkk',
           }

skip = 0
num = 1
loops = 2
csv_list = []
# for key, value in cookies.items():
# printit(skip)
# threading.Timer(5.0, printit, [skip+1]).cancel()

# t.cancel()
# print(key + " => " + value)
printit(skip, loops, 'cookie1')
printit(skip, loops, 'cookie2')
printit(skip, loops, 'cookie3')


# https://docs.google.com/spreadsheets/d/1r6HcTiOPP9tVCjsFV1DZtNVGSYF7wGCpdNheCbpVVZo/edit?usp=sharing
