def my_hash(s): #create a function that takes in a string
    sb = s.encode() # use encode method to convert "hello world" string characters into unicode representation
    total = 0 # set initial total to 0
    for b in sb: #do a for loop: "for each character in sb..."
        # print(b) # "print b or print the unicode representation of those characters"
        total += b # add up all the character represented by numbers
        total &= 0xffffffff #force your hashing function to return a number related to the power of two
    return total # returns one totaled number of all the unicode representations of characters

my_array = [None] * 8 #Initialize an array to None, with a length of 8
print(f'my_array {my_array}')

#STORING A VALUE
hash_index = my_hash("hello world") % 8 #we need to use modulo to constrain values between 0 and 7 (since the length max is 8)
print(f'hash_index {hash_index}')

my_array[hash_index] = 'my value' #index into the underlying array and store the value there
print(f'my_array {my_array}') #outputs array with 'my value' stored at index 4

#GETTING A VALUE
hash_index = my_hash("hello world") % 8 #run the key string "hello world" through hash function to get hash value
print(my_array[hash_index]) #outputs 'my value'

#DELETING A VALUE
hash_index = my_hash("hello world") % 8 #get the hash index
my_array[hash_index] = None #set the hash index to none
print(my_array) #outputs array without 'my value'

#print(my_array) #prints the array with None as the value at each index
#print(my_hash("hello world")) #print out the hashed version of "hello world" which equals 1116