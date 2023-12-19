# LISTS 101 and adding and removing items from a list

auras = ['frost', 'dark', 'water', 'cosmic', 'forest', 'flame', 'earth'] #lists are created with [ ] square brackets
print(auras[0].title()) # lists are indexed and we used the square bracket [ ] with numeric values to denote which item in the list we want to print, followed by title method in this case. Index positions start at 0
print(auras[-1].title()) # we use -1 to return the last value in a list. Useful. Also, same logic applies to -2 (2nd last) and so on. 
print(auras[1].title())
print(auras[2].title())
print(auras[3].title())
print(auras[4].title())
print(auras[5].title())
print(auras[0].title() + " " + "- " + "The coldest aura.")
print(auras[-1].title() + " " + "- " + "The boldest aura.")
print(auras[1].title() + " " + "- " + "The scariest aura.")
print(auras[2].title() + " " + "- " + "The slickest aura.")
print(auras[3].title() + " " + "- " + "The weirdest aura.")
print(auras[4].title() + " " + "- " + "The wildest aura.")
print(auras[5].title() + " " + "- " + "The brightest aura.")

auras.append('spirt') #append is simple method to add an element to a list. 
print(auras)

auras.insert(1,'light') # we can also insert, using insert method, to any position in index. 
print(auras[1].title())

del auras[3] # 'del' will delete element from list, using index.
print(auras)

popped_aura = auras.pop() #this pop method will remove the last value in a list, however, it can store the value in another variable for later use. Use pop method if you don't want to permanently delete (using del)
print(auras)
print(popped_aura)

print("The last aura i had added to my list was a " + popped_aura.title() + " aura.")
