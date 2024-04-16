import os
import random
Location = ("Dataset/test_set/I am Confused")

for filename in os.listdir(Location):
    Dupe_Counter = random.randint(0,80)
    try:
        if filename.startswith("["):
            os.rename(Location + filename, Location + filename[7:])
    except:
            os.rename(Location + filename, Location +'[Duplicate]_' + '[' + str(Dupe_Counter) +']' + filename[7:])