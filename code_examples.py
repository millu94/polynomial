# gpt
#x = [1, 2, 3]
#y = [4, 5, 6]

#z = [a + b for a, b in zip(x, y)]
#print(z)  # Output: [5, 7, 9]


#geeksforgeeks (googled: how to add two lists element-wise in python)
# Input lists
a = [1, 3, 4, 6, 8]
b = [4, 5, 6, 2, 10]

# Add corresponding elements using list comprehension
c = [a[i] + b[i] for i in range(len(a))]

# Print the result
print(c)