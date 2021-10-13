from pygame import mixer
from datetime import datetime
from time import time

# def function for music
def musicon(file,stop):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()


    while True:
        input_from_user = input()
        if input_from_user == stop:
            mixer.music.stop()
            break


# def function for write a deatil on it

def log1(msg):
    with open("pythontime.txt", "a") as my:
        my.write(f"{datetime.now()},{msg}")

# created main function :

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercises = time()
    watertime = 0
    eyestime = 0
    exerecisetime = 0

    while True:

        if time() - init_water > watertime:
            print("time for drink water once you done write drank for stop this alarm :")
            musicon("manike.mpeg","drank")
            init_water = time()
            log1("drink water at :")

        if time() - init_eyes > eyestime:
            print("time for eye exercise once done write done_eyes for stop this alarm :")
            musicon("OM.mpeg","done_eyes")
            init_eyes = time()
            log1("eyes excercise at :")
        if time() - init_exercises > exerecisetime:
            print("get ready ! its time for physical exercise once done enter physical for stop this alarm")
            musicon("SHI.mpeg","physical")
            init_exercises = time()
            log1("physical exercise at :")