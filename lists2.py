# SORTING lists (function and method) and using len function 

destinations = ['china', 'brazil', 'europe', 'japan', 'russia', 'canada']
print(destinations)
print(sorted(destinations)) # the sorted FUNCTION is being applied to our variable 'destinations' and inherently sorts alphabetically

print(destinations)
destinations.reverse() #here we're using the reverse METHOD on our variable, 'destinations'
print(destinations)
destinations.reverse() # since the reverse method applies a permanent change to the order of the list, we reverse again to revert back to original list
print(destinations) 
destinations.sort() # now we apply the sort method to apply permanent sort of our list
print(destinations)
destinations.sort(reverse=True) #here we apply sort method but with condition where reverse order is true, so list comes across in reverse alphabetical order
print(destinations)

len(destinations) # the 'len' (length) function determines how many items are in a list

print("I have " + str(len(destinations)) + " destinations on my list.") #I want to show the count of my destinations, so i had to convert the output of applying the length function to my variable 'destinations', to a string. 
