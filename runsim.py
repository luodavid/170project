import subprocess
from os import listdir
from os.path import isfile, join
files20 = [f for f in listdir("./inputs/inputs20")]
files35 = [f for f in listdir("./inputs/inputs35")]
files50 = [f for f in listdir("./inputs/inputs50")]
filesStaff = [f for f in listdir("./inputs/inputsStaff")]



for i in filesStaff:
	out = "output" + i[5:-3] + ".out"
	subprocess.call(["python2", "newsim.py", "./inputs/inputsStaff/" + i, out])
	subprocess.call(["python2", "output_validator.py", "./inputs/inputsStaff/" + i, out])
	print out

for i in files20:
	out = "output" + i[5:-3] + ".out"
	subprocess.call(["python2", "newsim.py", "./inputs/inputs20/" + i, out])
	subprocess.call(["python2", "output_validator.py", "./inputs/inputs20/" + i, out])
	print out

for i in files35:
	out = "output" + i[5:-3] + ".out"
	subprocess.call(["python2", "newsim.py", "./inputs/inputs35/" + i, out])
	subprocess.call(["python2", "output_validator.py", "./inputs/inputs35/" + i, out])
	print out

for i in files50:
	out = "output" + i[5:-3] + ".out"
	subprocess.call(["python2", "newsim.py", "./inputs/inputs50/" + i, out])
	subprocess.call(["python2", "output_validator.py", "./inputs/inputs50/" + i, out])
	print out