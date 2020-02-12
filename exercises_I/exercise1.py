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

' seconds per mile = ((21 minutes * 60 seconds in a minute) + 15 seconds) / number of miles in 5 kilometers'
pace = ( (21 * 60) + 15 ) / miles

# 4.  What is your average speed in miles per hour?

'miles per hour = 1 mile / ( seconds per mile / 60 seconds in a minute / 60 minutes in an hour )'
mph = 1 / ( pace / 60 / 60 )

# 5.  Suppose the cover price of a book is $19.95, but bookstores get a 25% discount. 
#     Shipping costs $2.50 for the first copy and $1 for each additional copy. What is the total wholesale cost for 75 copies?

coverPrice = 19.95
discount = 0.25
shippingCost1 = 2.5
shippingCost2 = 1

numberOfCopies = 75
totalCoverPrice = numberOfCopies * ( coverPrice * (1 - discount) )
totalShippingCost = shippingCost1 + ( ( numberOfCopies - 1 ) * shippingCost2 )

wholesaleCost = totalCoverPrice + totalShippingCost

# Print in Terminal
print("There are " + str(seconds) + " seconds in 21 minutes and 15 seconds.")
print("There are " + str(miles) + " miles in 5 kilometers.")
print("Your average pace is " + str(round(pace // 60)) + " minutes and " + str(round(pace % 60)) + " seconds per mile. ")
print("Your average speed is " + format(mph, '.2f') + " miles per hour.")
print("The wholesale cost of 75 copies is: $" + format(wholesaleCost, '.2f') + ".")