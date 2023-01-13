import pandas as pd
from random import randint
from time import sleep
import threading
import multiprocessing
from multiprocessing import Process

# Spreadsheet: https://docs.google.com/spreadsheets/d/1r6HcTiOPP9tVCjsFV1DZtNVGSYF7wGCpdNheCbpVVZo/edit?usp=sharing


def printit(skip, loops, cookie):
    while True:
        if loops < 1:
            return
        sheet_id = "1r6HcTiOPP9tVCjsFV1DZtNVGSYF7wGCpdNheCbpVVZo"
        sheet_name = "campaign01_01"
        url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
        df = pd.read_csv(url, skiprows=skip.value, nrows=0)
        print("\n----------------- cookie -----------------")
        print(cookie)
        print("skip in timer: ", skip.value)
        skip.value += 1
        print("loops in timer: ", loops)
        loops -= 1
        print("----------------------- New Entry in DataFrame -------------------------")
        csv_list.append(df.columns.to_list())
        print(csv_list)
        sleep(randint(10, 15))


def main():
    # Global variables
    global csv_list
    global skip
    global loops

    cookies = {'cookie1': 'wwwwwwwwwwwwwwwwwwww',
               'cookie2': 'eeeeeeeeeeeeeeeeeee',
               'cookie3': 'sssssssssssssssssssss',
               'cookie4': 'qqqqqqqqqqqqqqqqq',
               'cookie5': 'kkkkkkkkkkkkkkkkk',
               }

    csv_list = []
    threads = []

    # Used to update skip through multiprocessing and parallel functioning
    skip = multiprocessing.Value('i', 0)

    # Set up a thread for each cookie
    for key, value in cookies.items():
        loops = 10

        t = threading.Thread(target=printit, args=(skip, loops, key,))
        threads.append(t)

    for x in threads:
        x.start()
        # if used the threads will run serially
        # if not, there might be an interference in data reading
        x.join()


if __name__ == '__main__':
    main()
