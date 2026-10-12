count = 1
total = 0

# BUG: The while statement needs a colon to start its indented block.
# BUG: < 5 stops before adding 5; use <= 5 to include it in the sum.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Convert the integer total to text before joining it to the message.
print("Sum of 1 to 5 is: " + str(total))

