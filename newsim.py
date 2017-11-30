import argparse
from random import shuffle, sample, random

"""
======================================================================
  Complete the following function.
======================================================================
"""
def acceptance_probability(old, new, temp):
    return 2.71828 ** ((old - new) / temp)

def cost(num_wiz_in_input, num_constraints, wizards, constraints):
    output_ordering = wizards
    output_ordering_set = set(output_ordering)
    output_ordering_map = {k: v for v, k in enumerate(output_ordering)}

    if (len(output_ordering_set) != num_wiz_in_input):
        return "Input file has unique {} wizards, but output file has {}".format(num_wiz_in_input, len(output_ordering_set))

    if (len(output_ordering_set) != len(output_ordering)):
        return "The output ordering contains repeated wizards."

    # Counts how many constraints are satisfied.
    constraints_satisfied = 0
    constraints_failed = []
    for i in range(num_constraints):
        constraint = constraints[i]

        c = constraint # Creating an alias for easy reference
        m = output_ordering_map # Creating an alias for easy reference

        wiz_a = m[c[0]]
        wiz_b = m[c[1]]
        wiz_mid = m[c[2]]

        if (wiz_a < wiz_mid < wiz_b) or (wiz_b < wiz_mid < wiz_a):
            constraints_failed.append(c)
        else:
            constraints_satisfied += 1

    return num_constraints - constraints_satisfied


def neighbor(wizards):
    indices = sample(range(len(wizards)), 2)
    newWiz = wizards[:]
    newWiz[indices[0]] = wizards[indices[1]]
    newWiz[indices[1]] = wizards[indices[0]]
    return newWiz

def randomWizard(wizards):
    newWiz = wizards[:]
    shuffle(newWiz)
    return newWiz

def solve(num_wizards, num_constraints, wizards, constraints):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints, 
                     where constraints[0] may take the form ['A', 'B', 'C']

    Output:
        An array of wizard names in the ordering your algorithm returns
    """
    shuffle(wizards)
    solution = wizards
    old_cost = cost(num_wizards, num_constraints, solution, constraints)
    T = 1
    T_min = 0.00000001
    alpha = 0.9999
    while T > T_min:
        i = 1
        print(cost(num_wizards, num_constraints, solution, constraints))
        while i <= 100:
            new_solution = neighbor(solution)
            new_cost = cost(num_wizards, num_constraints, new_solution, constraints)
            ap = acceptance_probability(old_cost, new_cost, T)

            if ap > random():
                solution = new_solution
                old_cost = new_cost
            i += 1
            if new_cost == 0:
                print(new_solution)
                return new_solution

        T = T*alpha
    print(solution)
    return solution

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