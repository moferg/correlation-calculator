# Correlation Calculator - Marshall Ferguson - 6/2020

# Imports

import math
import statistics

# Function Definitions

# Mean Formula
# M = sum of X / N
# The mean is the sum of the scores divided by number of scores

def mean_of_list(list_values):
	return sum(list_values) / len(list_values)

# Standard Deviation Formula
# SD ^ 2 = sum of (X - M) ^ 2 divided by N
# Variance is Standard Deviation squared, ie Standard Deviation is square root of Variance

def standard_deviation(list_values):
	deviation_scores = []
	deviation_scores_squared = []
	sum_of_squares = 0
	variance = 0
	std_deviation = 0
	for x in list_values:
		deviation_scores.append(x - mean_of_list(list_values))
	for x in deviation_scores:
		deviation_scores_squared.append(x ** 2)
	sum_of_squares = math.fsum(deviation_scores_squared)
	# sum_of_squares += (math.fsum(list_values[x] - mean_of_list(list_values))) ** 2
	variance = sum_of_squares / len(list_values)
	std_deviation = math.sqrt(variance)
	return std_deviation

# Z Score Formula
# Z = (X - M) \ SD
# Z score is equal to the raw score minus the mean, divided by standard deviation

def z_scores_of_list(list_values):
	z_scores = []
	for x in list_values:
		z_score = (x - mean_of_list(list_values)) / standard_deviation(list_values)
		z_scores.append(z_score)
	return z_scores

# Correlation Coefficient Formula
# r = the sum of Z(x) * Z(y) divided by N
# r = correlation coefficient
# Z = Z score
# N = sample size, number of participants

def correlation_of_two_lists(list_values_a, list_values_b):
	multiplied_z_scores = []
	z_scores_a = z_scores_of_list(list_values_a)
	z_scores_b = z_scores_of_list(list_values_b)
	# Below code does not work as intended, outputs a list with 26 indexes instead of 5 indexes
	# Nested for loops != solution
	# for x in z_scores_a:
	# 	for y in z_scores_b:
	# 		multiplied_z_score = x * y
	# 		multiplied_z_scores.append(multiplied_z_score)
	# sum_of_multiplied_z_scores = math.fsum(multiplied_z_scores)

	# Leaving the above code as a reminder that simple is better than complex

	for x, y in zip(z_scores_a, z_scores_b):
		multiplied_z_scores.append(x * y)
	sum_of_multiplied_z_scores = math.fsum(multiplied_z_scores)
	print(multiplied_z_scores)
	print(sum_of_multiplied_z_scores)
	# sum_of_multiplied_z_scores = sum((x - mean_of_list(list_values_a)) / standard_deviation(list_values_a) * (y - mean_of_list(list_values_b)) / standard_deviation(list_values_b))
	r = sum_of_multiplied_z_scores / len(list_values_a)
	return r

# Initial Variable Declarations 

correlation_values_a = []
correlation_values_b = []

# Ask the user to input values/scores for first list

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

# Print out the mean, standard deviation, and z scores for first list

print("The mean (average) of the first list is", mean_of_list(correlation_values_a))
print("The Standard Deviation of the first list is", standard_deviation(correlation_values_a))
print("The Standard Deviation of the first list (using .pstdev) is", statistics.pstdev(correlation_values_a))
print("The Z-Scores of the first list are", z_scores_of_list(correlation_values_a))

# Ask the user to input values/scores for second list

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

# Print out the mean, standard deviation, and z scores for second list

print("The mean (average) of the second list is", mean_of_list(correlation_values_b))
print("The Standard Deviation of the second list is", standard_deviation(correlation_values_b))
print("The Standard Deviation of the second list (using .pstdev) is", statistics.pstdev(correlation_values_b))
print("The Z-Scores of the second list are", z_scores_of_list(correlation_values_b))

# Print out the correlation coefficient of the two lists

print("The Correlation between the two lists is", correlation_of_two_lists(correlation_values_a, correlation_values_b))