casters = ['Sam', 'Rose', 'Adam', 'Phil', 'Tom',] 
for caster in casters: # here we are using a for loop so that for each 'caster' (new variable we're creating) in the list 'casters', we are storing each item in the list indiviually. The loop repeats that action.
	print(caster) # now we're printing the output of the dyanmic variable in which the for loop is executing. The loop repeats its program until no items are left in the list.
	
for caster in casters:
	print(caster.title() + ", " + "that was a great trick!") # Note, you have to indent following the for loop statement to indicate what actions are to take place within the loop.
	
	print("I look forward to what you come up with next, " + caster.title() + ".\n")


print("What performance, everyone!") #this statement doesn't loop since it is out of loop.


