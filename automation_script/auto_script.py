import pandas as pd
from random import randint
from time import sleep
import threading
import multiprocessing
from multiprocessing import Process
import json


# Target Spreadsheet: https://docs.google.com/spreadsheets/d/1r6HcTiOPP9tVCjsFV1DZtNVGSYF7wGCpdNheCbpVVZo/edit?usp=sharing

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
        # print("----------------------- New Entry in DataFrame -------------------------")
        csv_list.append(df.columns.to_list())
        # print(csv_list)


def main():
    # Global variables
    global csv_list
    global skip
    global loops

    cookies = {'cookie1': 'k0a3IBbK4EaP74dzyqpfXuqBcielrQnAKUYkiJIqBB5E8m9c',
               'cookie2': 'ZzNmV1lFYkpkdDcyNVROWTY1UGlYQVUzNldPSVNLNzQ',
               'cookie3': '53c1b957098f4d929135ae0ed42833efadagjvjakblk',
               'cookie4': 'fe746c765e324883af7bf8582774a789202gg20240113',
               'cookie5': '3CBCsdkwFE535wsd2716BwdDD0wdf690trgECD35gg36D6AB7',
               }

    csv_list = []
    threads = []

    # Used to update skip through multiprocessing and parallel functioning
    skip = multiprocessing.Value('i', 0)

    # Set up a thread for each cookie
    for key, value in cookies.items():
        loops = 10
        # Create a thread for every cookie in the list
        t = threading.Thread(target=printit, args=(skip, loops, key,))
        t.start()
        sleep(60)
        threads.append(t)

    for x in threads:
        # if used the threads will run serially
        # if not, they will run in parallel but there might be an interference in data reading
        x.join()

    json_object = json.dumps(csv_list)
    print(json_object)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:   
        outfile.write(json_object)


if __name__ == '__main__':
    main()
