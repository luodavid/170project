from random import shuffle
from random import randint
from random import random
import argparse
import output_validator
import math

# in20_0 = open("inputs20/input20_0.in", "r")
# wizNum = int(in20_0.readline())
# conNum = int(in20_0.readline())
# print wizNum
# print conNum
# nameSet = set()
# names = in20_0.readlines()
# for line in names:
# 	lists = line.split(' ')
# 	nameSet.add(lists[0])
# 	nameSet.add(lists[1])
# 	nameSet.add(lists[2])

# firstChoose = list(nameSet)
# shuffle(firstChoose)


"""
======================================================================
  Complete the following function.
======================================================================
"""

def acceptanceProbability(energy, newEnergy, temperature):
	if (newEnergy < energy):
		return 1
	else:
		return math.exp((energy - newEnergy) / temperature)

def energy(wizards, constraints, num_constraints):
	"""
	Input:
		wizards: An ordering of the wizards that is an attempt at a solution
		constraints: A 2D-array of constraints
	Output: 

	"""
	output_ordering = wizards
	output_ordering_set = set(output_ordering)
	output_ordering_map = {k: v for v,k in enumerate(output_ordering)}
	constraints_failed = []
	constraints_satisfied = 0

	for i in range(num_constraints):
		constraint = constraints[i]
		wizA = output_ordering_map[constraint[0]]
		wizB = output_ordering_map[constraint[1]]
		wizC = output_ordering_map[constraint[2]]
		if (wizA < wizC < wizB) or (wizB < wizC < wizA):
			constraints_failed.append(c)
		else:
			constraints_satisfied += 1

	return constraints_satisfied


def solve(num_wizards, num_constraints, wizards, constraints):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints, 
                     where constraints[0] may take the form ['A', 'B', 'C']i

    Output:
        An array of wizard names in the ordering your algorithm returns
    """
 #    output_ordering = wizards
	# output_ordering_set = set(output_ordering)
	# output_ordering_map = {k: v for v,k in enumerate(output_ordering)}
    temperature = 10000
    cooling_rate = 0.003
    base = shuffle(wizards)
    best = base
    bestEnergy = energy(best, constraints, num_constraints)
   	while (temperature > 1):
	    currentEnergy = energy(base, constraints, num_constraints)
	    randWiz1, randWiz2 = 0, 0
	    while (randWiz1 == randWiz2):
		    randWiz1 = random.randint(0, num_wizards)
		    randWiz2 = random.randint(0, num_wizards)
		wizard1 = wizards[randWiz1]
		wizard2 = wizards[randWiz2]

		newSolution = base
		newSolution[randWiz1] = wizard2
		newSolution[randWiz2] = wizard1
		newEnergy = energy(newSolution, constraints, num_constraints)

		prob = acceptanceProbability(currentEnergy, newEnergy, temperature)
		if (prob > random.random()):
			base = newSolution
			currentEnergy = newEnergy
		if (currentEnergy > best):
			best = base 
			bestEnergy = currentEnergy
		temp *= 1 - cooling_rate


    


    return []

"""
======================================================================
   No need to change any code below this line
======================================================================
"""

def read_input(filename):
    with open(filename) as f:
        num_wizards = int(f.readline())
        num_constraints = int(f.readline())
        constraints = []
        wizards = set()
        for _ in range(num_constraints):
            c = f.readline().split()
            constraints.append(c)
            for w in c:
                wizards.add(w)
                
    wizards = list(wizards)
    return num_wizards, num_constraints, wizards, constraints

def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
    solution = solve(num_wizards, num_constraints, wizards, constraints)
    write_output(args.output_file, solution)
