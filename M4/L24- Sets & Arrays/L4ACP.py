"""Write a Python program to find the symmetric difference between two sets.

For reference - The symmetric difference of two sets is equal to the set of elements that are in either of the sets but not in their intersection. In Python, you can use Set1.symmetric_difference(Set2)to find the symmetric of Set 1 and 2.

Example - Set 1 = {1,2,3} and Set 2 = {3,4}
Symmetric difference = {1,2,4}

Find Symmetric Difference for :

A. Set1 = {'blue', 'green'} Set2 = {'blue', 'yellow'}
B. Set1 = {1, 2, 3, 4, 5} Set2 = {1, 5, 6, 7, 8, 9}"""

def sym_difference(set1, set2):
	print("\nOriginal sets:")
	print(set1)
	print(set2)
	result = set1.symmetric_difference(set2)
	print("\nSymmetric difference of setc1 - setc2:")
	return result

seta1 = set(["green", "blue"])
seta2 = set(["blue", "yellow"])
setb1 = set([1, 1, 2, 3, 4, 5])
setb2 = set([1, 5, 6, 7, 8, 9])

print("Result of A Sets")
sym_difference(seta1, seta2)
print("Result of B Sets")
sym_difference(setb1, setb2)