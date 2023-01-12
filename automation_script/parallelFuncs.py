import multiprocessing
from multiprocessing import Process

def runInParallel(*fns):
    global variable
    proc = []
    for fn in fns:
        p = Process(target=fn, args=(variable,))
        p.start()
        proc.append(p)

    for p in proc:
        p.join()

def changethevariable(variable):
    with variable.get_lock():
        variable.value = variable.value + 1
    print(variable.value)

def changethevariable_again(variable):
    with variable.get_lock():
        variable.value = variable.value + 3
    print(variable.value)
    

def main():
    global variable
    variable = multiprocessing.Value('i', 1)
    runInParallel(changethevariable_again, changethevariable)
    print(variable.value)

if __name__ == '__main__':
    main()