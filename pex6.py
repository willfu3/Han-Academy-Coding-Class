n = raw_input("number: ")
number = int (n)
choice = raw_input("sum or product?: ")
if choice == "sum":
	total = 0
	for i in range(number+1):
		total+=i;
	print("sum: " + str(total))
elif choice == "product":
	total = 1
	for i in range(1, number+1):
		total*=i;
	print("product: " + str(total))
