'''
Exercise 1
Start the Python interpreter and use it as a calculator.

1.  How many seconds are there in 21 minutes and 15 seconds?
2.  How many miles are there in 5 kilometers?
3.  If you run a 5 kilometer race in 21 minutes and 15 seconds, what is your average pace (time per mile in minutes and seconds)?
4.  What is your average speed in miles per hour?
5.  Suppose the cover price of a book is $19.95, but bookstores get a 25% discount. 
    Shipping costs $2.50 for the first copy and $1 for each additional copy. What is the total wholesale cost for 75 copies?
    
'''

# 1.  How many seconds are there in 21 minutes and 15 seconds?

seconds = (21 * 60) + 15

# 2.  How many miles are there in 5 kilometers?

miles = 5 / 1.609

# 3.  If you run a 5 kilometer race in 21 minutes and 15 seconds, what is your average pace (time per mile in minutes and seconds)?

secondspermile = ( (21 * 60) + 15 ) / miles

# 4.  What is your average speed in miles per hour?

# 5.  Suppose the cover price of a book is $19.95, but bookstores get a 25% discount. 
#     Shipping costs $2.50 for the first copy and $1 for each additional copy. What is the total wholesale cost for 75 copies?

# Print in Terminal
print("There are " + str(seconds) + " seconds in 21 minutes and 15 seconds.")
print("There are " + str(miles) + " miles in 5 kilometers.")
print("Your average pace is " + str(round(secondspermile // 60)) + " minutes and " + str(round (secondspermile % 60)) + " seconds per mile. ")