# You are conducting a contest at your college. This contest consists of two problems and 
#  participants. You know the problem that a candidate will solve during the contest.

# You provide a balloon to a participant after he or she solves a problem. 
# There are only green and purple-colored balloons available in a market. 
# Each problem must have a balloon associated with it as a prize for solving that specific problem. 
# You can distribute balloons to each participant by performing the following operation:

# Use green-colored balloons for the first problem and purple-colored balloons for the second problem
# Use purple-colored balloons for the first problem and green-colored balloons for the second problem
# You are given the cost of each balloon and problems that each participant solve. 
# Your task is to print the minimum price that you have to pay while purchasing balloons.

# Input format

# First line: 
#  that denotes the number of test cases (
# )
# For each test case: 
# First line: Cost of green and purple-colored balloons 
# Second line: 
#  that denotes the number of participants (
# )
# Next 
#  lines: Contain the status of users. For example, if the value of the 
#  integer in the 
#  row is 
# , then it depicts that the 
#  participant has not solved the 
#  problem. Similarly, if the value of the 
#  integer in the 
#  row is 
# , then it depicts that the 
#  participant has solved the 
#  problem.
# Output format
# For each test case, print the minimum cost that you have to pay to purchase balloons.

# Sample Input
# 2
# 9 6
# 10
# 1 1
# 1 1
# 0 1
# 0 0
# 0 1
# 0 0
# 0 1
# 0 1
# 1 1
# 0 0
# 1 9
# 10
# 0 1
# 0 0
# 0 0
# 0 1
# 1 0
# 0 1
# 0 1
# 0 0
# 0 1
# 0 0
# Sample Output
# 69
# 14




# Define a function to calculate the minimum cost of balloons
def min_cost(cost_green, cost_purple, participants):
  # Initialize the number of problems solved by participants
  problem_1_solved = 0
  problem_2_solved = 0
  # Loop through the participants and count the problems solved
  for p in participants:
    problem_1_solved += p[0]
    problem_2_solved += p[1]
  # Calculate the cost of using green balloons for problem 1 and purple balloons for problem 2
  cost_1 = cost_green * problem_1_solved + cost_purple * problem_2_solved
  # Calculate the cost of using purple balloons for problem 1 and green balloons for problem 2
  cost_2 = cost_purple * problem_1_solved + cost_green * problem_2_solved
  # Return the minimum of the two costs
  return min(cost_1, cost_2)

# Read the number of test cases
test_cases = int(input())
# Loop through the test cases
for _ in range(test_cases):
  # Read the cost of green and purple balloons
  cost_green, cost_purple = map(int, input().split())
  # Read the number of participants
  participants = int(input())
  # Initialize an empty list to store the status of participants
  status = []
  # Loop through the participants and read their status
  for _ in range(participants):
    status.append(list(map(int, input().split())))
  # Call the function to calculate the minimum cost and print it
  print(min_cost(cost_green, cost_purple, status))