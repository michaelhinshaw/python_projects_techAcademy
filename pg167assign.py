import os
import time


myPath = 'C:\\Python_167_assignment\\'



for filename in os.listdir(myPath):
    if filename.endswith(".txt"):
        print(os.path.join(myPath, filename))


        
path1 = 'C:\Python_167_assignment\house.txt'

mod_time = os.path.getmtime(path1)
loc_time = time.ctime(mod_time)
print(path1,loc_time)

path2 = 'C:\Python_167_assignment\planets.txt'

mod_time = os.path.getmtime(path2)
loc_time = time.ctime(mod_time)
print(path2,loc_time)

path3 = 'C:\Python_167_assignment\plants.txt'

mod_time = os.path.getmtime(path3)
loc_time = time.ctime(mod_time)
print(path3,loc_time)



