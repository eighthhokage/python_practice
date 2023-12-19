# storing variables iteratively and removing whitespace via rstrip (right strip) method. 

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language) # often times you'll need to iteratively update a variable with a new value and re-use. Initially stored as python with a trailing whitespace, we use the rstrip (right) to remove and then redefine the value. 

