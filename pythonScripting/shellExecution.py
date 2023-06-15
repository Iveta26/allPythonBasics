import os
import subprocess

#run a shell script from python script

# stores file path to the current file
scriptDir = os.path.dirname(__file__) #means this __file__

# stores file path to the script you want to run
scriptAbsolutePath = os.path.join('C:/Users/iveta_6esu9b1/PycharmProjects/pythonScripting/shellScript.sh')


# calls the shell file and runs it
subprocess.call(['sh', scriptAbsolutePath])