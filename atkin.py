import os
import math
from sys import argv
import multiprocessing as mp
import time
import timeit

def Atkins(limit: int, s1: int, s2: int, s3: int):
    if s1 == 1:
        way = "first.txt"
        status = "1 процесс завершил работу"
        i=1
    elif s2 == 1:
        way = "second.txt"
        status = "2 процесс завершил работу"
        i=2
    elif s3 == 1:
        way = "third.txt"
        status = "3 процесс завершил работу"
        i=3
    sieve = [False] * (limit+1)
    check = 0
    t=time.time()
    t=int(t)
    for x in range(i, int(math.sqrt(limit)) + 1, 3):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
            if int(time.time())-t==6:
                print(x)
                t=time.time()
                t=int(t)
    with open(way, "w", encoding='utf-7') as file_atk:
        for id, x in enumerate(sieve):
            string = str(x) + '\n'
            file_atk.write(string)
    print(status + '\n')


def read_files()->list:
    print("start read 1")
    with open('first.txt','r',encoding='utf-8') as file_1:
        first_read = file_1.read()
        list_1 = first_read.split("\n")
    print("start read 2")
    with open('second.txt','r',encoding='utf-8') as file_2:
            first_read = file_2.read()
            list_2 = first_read.split("\n")
    print("start read 3")
    with open('third.txt','r',encoding='utf-8') as file_3:
        first_read = file_3.read()
        list_3 = first_read.split("\n")
    list_123=[False]*len(list_1)
    lens=len(list_1)
    for i in range(0,lens):
        if list_1[i]=="False":
            z1=False
        else: z1=True
        if list_2[i]=="False":
            z2=False
        else: z2=True
        if list_3[i]=="False":
            z3=False
        else: z3=True
        list_123[i]=(z1+z2+z3)%2
    list_4=[False]*len(list_123)
    for id,x in enumerate(list_123):
        if x==1:
            if id%5==0:
                pass
            else:
                list_4[id]=id
    for x in range(5, int(math.sqrt(len(list_123)))):
        if list_4[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                list_4[y] = False
    return list_4


def starts(limit: int):
    with mp.Pool(processes=3) as my_pool:
        p1 = my_pool.starmap(Atkins,
                             iterable=[
                                       [limit, 1, 0, 0],
                                       [limit, 0, 1, 0],
                                       [limit, 0, 0, 1]
                                      ],
                             )
        my_pool.close()


if __name__ == '__main__':
    try:
        # if int(argv[1]) > 0:
        #     pass
        # elif int(argv[1]) < 0:
        #     raise Exception
        # elif int(argv[1]) == 0:
        #     raise Exception
        # else:
        #     raise Exception
        # limit = int(argv[1])
        limit = 25000000
        a = timeit.default_timer()
        starts(limit)
        time_list = read_files()
        while len(time_list)>limit:
            time_list.pop()
        res=list()
        for index,elem in enumerate(time_list):
            if elem is not False:
                res.append(elem)
        res.sort()
        with open("result.txt", "w", encoding='utf-8') as file:
            file.write("2\n3\n5\n")
            for p in res:
                string = ""+str(p)+"\n"
                file.write(string)
        print("Алгоритм считал:", timeit.default_timer()-a, "секунд\n")
    except Exception:
        print("Неправильный аргумент")
    except BaseException:
        print("Вы нажали на Ctrl + C")
    except FileNotFoundError:
        pass