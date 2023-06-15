

# Libraries and Modules -
# library - collection of modules
# module - collection of functions

# Seven "core" modules in Python

import sys

# get python version
print(sys.version)


import os

print(os.getcwd())


import subprocess #lets

# runs an external file when executed
subprocess.run(["python", "helloWorld.py"])



import math

pi = math.pi
piString = str(pi)
print(f"the val of file is {piString}")



import random
randNum = random.randrange(1, 10)
print(randNum)


import datetime

currentDate = datetime.datetime.now()
print(currentDate)


import json #transport data between two systems

x = {
    "name": "John",
    "age": 30,
    "city": "liverpool"
}

y = json.dumps(x)

print(y)
