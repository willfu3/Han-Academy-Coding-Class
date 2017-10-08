n = raw_input("number: ")
number = int (n);
total = 0;
for i in range(number+1):
	if i%3 == 0 or i%5 == 0:
		total+=i;
print("Modified sum: " + str(total))
