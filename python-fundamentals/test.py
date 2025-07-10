 prices = [10, 25, 5, 15, 30]

# for price in prices:
#     if price < 20:
        
#         print({price})

# Let's break this down step by step. 
# First, you need to initialize a variable to store the total cost. 
# Then, you'll iterate through the list of prices using a 'for' loop. 
# Inside the loop, use an 'if' statement to check if the current price is less than 20. 
# If it is, add it to the total cost. Here's how the code would look:


prices = [10, 25, 5, 15, 30]
total_cost = 0
for price in prices:
    if price < 20:
        total_cost += price
print(total_cost)


