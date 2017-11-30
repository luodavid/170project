from random import shuffle

in20_0 = open("inputs/inputs20/input20_0.in", "r")
wizNum = int(in20_0.readline())
conNum = int(in20_0.readline())
print wizNum
print conNum
nameSet = set()
names = in20_0.readlines()

for line in names:
	lists = line.split(' ')
	nameSet.add(lists[0])
	nameSet.add(lists[1])
	nameSet.add(lists[2])
	if len(nameSet) == wizNum:
		break

firstChoose = list(nameSet)
shuffle(firstChoose)