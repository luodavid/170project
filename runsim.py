import subprocess
from os import listdir
from os.path import isfile, join
files20 = [f for f in listdir("./inputs/inputs20")]
files35 = [f for f in listdir("./inputs/inputs35")]
files50 = [f for f in listdir("./inputs/inputs50")]
filesStaff = [f for f in listdir("./inputs/inputsStaff")]


for i in files20:
	out = "output" + i[5:-3] + ".out"
	subprocess.call(["python2", "newsim2.py", "./inputs/inputs20/" + i, out])
	subprocess.call(["python2", "output_validator.py", "./inputs/inputs20/" + i, out])
	print out

for i in files35:
	out = "output" + i[5:-3] + ".out"
	subprocess.call(["python2", "newsim2.py", "./inputs/inputs35/" + i, out])
	subprocess.call(["python2", "output_validator.py", "./inputs/inputs35/" + i, out])
	print out

for i in files50:
	out = "output" + i[5:-3] + ".out"
	subprocess.call(["python2", "newsim2.py", "./inputs/inputs50/" + i, out])
	subprocess.call(["python2", "output_validator.py", "./inputs/inputs50/" + i, out])
	print out

for i in filesStaff:
	out = "staff" + i[5:-3] + ".out"
	subprocess.call(["python2", "newsim2.py", "./inputs/inputsStaff/" + i, out])
	subprocess.call(["python2", "output_validator.py", "./inputs/inputsStaff/" + i, out])
	print out

# customStaff = []

# customStaff.append('staff_60.in')
# customStaff.append('staff_80.in')
# customStaff.append('staff_260.in')
# customStaff.append('staff_280.in')
# customStaff.append('staff_300.in')
# customStaff.append('staff_320.in')
# customStaff.append('staff_340.in')
# customStaff.append('staff_360.in')
# customStaff.append('staff_380.in')
# customStaff.append('staff_400.in')

# for i in customStaff:
# 	out = "staff_" + i[5:-3] + ".out"
# 	subprocess.call(["python2", "newsim.py", "./inputs/inputsStaff/" + i, out])
# 	subprocess.call(["python2", "output_validator.py", "./inputs/inputsStaff/" + i, out])
# 	print out

