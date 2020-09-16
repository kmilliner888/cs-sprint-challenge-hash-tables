#Step 1: create a function
#Step 2: find two items whose sum of weights equals the weight limit `limit`
#Step 2.1: Create a hash table
#Step 2.2: Store the weights as keys, and indexes as values
#Step 2.3: Check if hash table has limit weight
#Step 3: return a tuple of integers that has the following form: (zero, one)
#Step 4: if we find nothing, return None

#Constraint: Needs to run in Linear Time

# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21


def get_indices_of_item_weights(weights, length, limit):
    dictionary = {}

    for i in range (len(weights)):
       dictionary[weights[i]] = i

    for i in range (len(weights)):
        weight_limit = limit - weights[i]

        if weight_limit in dictionary:
            return ([max(i, dictionary[weight_limit]), min(i,dictionary[weight_limit])])
    return None





