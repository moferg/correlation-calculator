# Imports

import statistics

# Function Definitions

def mean_of_list(list_values):
	return sum(list_values) / len(list_values)


# Initial Variable Declarations 

correlation_values_a = []
correlation_values_b = []

# Ask the user to input values for correlation for each list

while True:
	print("Type 'DONE' when you have entered all values")
	user_input = input("Please enter the values for the first group:   ")
	if user_input.upper() != "DONE":
		user_input = int(user_input)
		correlation_values_a.append(user_input)
		print(correlation_values_a)
		print("The length of the first list is", len(correlation_values_a))
		print("The variable type of the last input is", type(correlation_values_a[-1]))
	else:
		print("The sum of the first list is", sum(correlation_values_a))
		break

print("The mean(average) of the first list is", mean_of_list(correlation_values_a))
print("The Standard Deviation of the first list is", statistics.stdev(correlation_values_a))

while True:
	print("Type 'DONE' when you have entered all values")
	user_input = input("Please enter the values for the second group:   ")
	if user_input.upper() != "DONE":
		user_input = int(user_input)
		correlation_values_b.append(user_input)
		print(correlation_values_b)
		print("The length of the second list is", len(correlation_values_b))
		print("The variable type of the last input is", type(correlation_values_b[-1]))
	else:
		print("The sum of the second list is", sum(correlation_values_b))
		break

print("The mean(average) of the second list is", mean_of_list(correlation_values_b))
print("The Standard Deviation of the second list is", statistics.stdev(correlation_values_b))

# Mean Formula
# M = sum of X / N
# The mean is the sum of the scores divided by number of scores

# Standard Deviation Formula
# SD ^ 2 = sum of (X - M) ^ 2 divided by N
# Variance is Standard Deviation squared, ie Standard Deviation is square root of Variance

# Z Score Formula
# Z = (X - M) \ SD
# Z score is equal to the raw score minus the mean, divided by standard deviation

# Correlation Coefficient Formula
# r = the sum of Z(x) * Z(y) divided by N
# r = correlation coefficient
# Z = Z score
# N = sample size, number of participants