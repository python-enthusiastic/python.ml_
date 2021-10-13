import wsgiref.validate

from pygame import mixer
from time import time
from datetime import datetime


# function for pygame mixer

def music(file,stopper):
 mixer.init()

 mixer.music.load(file)
 mixer.music.play()
 while True:
  input_of_user = input()
  if input_of_user == stopper:
   mixer.music.stop()
   break
def log(msg):
 with open("mydeatil.txt",'a') as ex:
   ex.write(f"{msg} {datetime.now()} \n")
if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watertime =0
    eyestime = 0
    exercisetime = 0
    while True:
     if time() - init_water>watertime:
      print(f"water drinking time write done to stop the alarm :")
      music("manike.mpeg","drank")
      init_water = time()
      log("drink water at :")
     if time() - init_eyes>eyestime:
      print("time for eyes exercise  write doneeyes to stop the alarm :")
      music("OM.mpeg","doneeyes")
      init_eyes = time()
      log("done eyes exercise  at :")
     if time() - init_exercise > exercisetime:
         print("time for exercise write doneexe to stop the alarm :")
         music("SHI.mpeg","doneexe")
         init_exercise = time()
         log("done exercise at :")



# #Healthy Programmer
# # 9am - 5pm
# # Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# # Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# # Physical activity - physical.mp3 every - 45 min - ExDone - log
# # Rules
# # Pygame module to play audio
#
# from pygame import mixer
# from datetime import datetime
# from time import time
#
# def musiconloop(file, stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#     while True:
#         input_of_user = input()
#         if input_of_user == stopper:
#             mixer.music.stop()
#             break
#
# def log_now(msg):
#     with open("mylogs.txt", "a") as f:
#         f.write(f"{msg} {datetime.now()}\n")
#
# if __name__ == '__main__':
#     # musiconloop("water.mp3", "stop")
#     init_water = time()
#     init_eyes = time()
#     init_exercise = time()
#     watersecs = 0
#     exsecs = 0
#     eyessecs = 0
#
#     while True:
#         if time() - init_water > watersecs:
#             print("Water Drinking time. Enter 'drank' to stop the alarm.")
#             musiconloop('manike.mpeg', 'drank')
#             init_water = time()
#             log_now("Drank Water at")
#
#         if time() - init_eyes >eyessecs:
#             print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
#             musiconloop('OM.mpeg', 'doneeyes')
#             init_eyes = time()
#             log_now("Eyes Relaxed at")
#
#         if time() - init_exercise > exsecs:
#             print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
#             musiconloop('SHI.mpeg', 'donephy')
#             init_exercise = time()
#             log_now("Physical Activity done at")
#
#
#
#
