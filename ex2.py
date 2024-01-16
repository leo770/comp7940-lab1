# Write a function that prints all factors of the given parameter x
l = [52633, 8137, 1024, 999]
def print_factor(x):
# your code here
	for i in range(x+1):
		if i == 0 :
			continue
		if x % i == 0 :
			print(i)

for t in l:
	print_factor(t)
