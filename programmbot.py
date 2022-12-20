import random 
import time 
import os

from procent import Percent 
from kosti import Kosti
from randomyze import Rand
from kalk import Kalc

print ("_______________________________________________________________________________________________________________")
print ("_______________________________________________________________________________________________________________")
print("вас приветсвует бот , в котором много ботов")

print ("_______________________________________________________________________________________________________________")
print ("_______________________________________________________________________________________________________________")
print ("_______________________________________________________________________________________________________________")
print("выберите программу для запуска ")
print("если вы хотите получить процент от числа : /procent")
print("если хотите открыть рандомайзер: /random")
print("если вы хотите принять решение : /rehen")
print("если хотите запустить калькулятор : /kalk")
programm = input("выберите программу для запуска:   ")

if programm == "/procent":

    print("запуск....")
    time.sleep(1)
    percent = Percent()
    percent.start()
     
  

if programm == "/rehen":

    print("запуск....")
    time.sleep(1)
    kosti = Kosti()
    kosti.start()
 



if programm =="/random":
     print("запуск")
     time.sleep(1)
     randomyze = Rand()
     randomyze.start()



if programm =="/kalk":
    print("запуск")
    time.sleep(1)
    kalk = Kalc()
    kalk.start()
