# #DEALING WITH COLLISIONS USING LINKEDLISTS

hash_table = [None] * 8 # 8 slots, all initialized to None

def my_hash(s):
    sb = s.encode() # Get the UTF-8 bytes for the string

    total = 0

    for b in sb:
        total += b
        total &= 0xffffffff #clamp to 32 bits

    return total

def hash_index(key):
    h = my_hash(key)
    return h % len(hash_table)

def put(key, val):
    i = hash_index(key)
    if hash_table[i] != None:
        print(f"Collision! Overwriting {repr(hash_table[i])}!")
    hash_table[i] = val

def get(key):
    i = hash_index(key)
    return hash_table[i]

def delete(key):
    i = hash_index(key)
    hash_table[i] = NotImplemented

put("Hello", "Hello Value") # key:value pair
put("World", "World Value") # key:value pair
put("foo", "foo value") # key:value pair, "foo" hashes to same index as "Hello"
                        # AKA "foo collides with Hello"

print(hash_table)

class Node: # implement a node class
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList: #implement a linkedlist class
    def __init__(self):
        self.head = None

    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr is not None:
            currStr += f'{str(curr.value)} ->'
            curr = curr.next
        return currStr

    # 3 main methods we need to implement a linkedlist:
    # insert value into list (insert)
    # delete a value from the list (delete)
    # get a value from the list (find)

    #Runtime of insert_at_head??  O(1) Constant Time
    def insert_at_head(self, node): # insert a new node at the head of the linkedlist
        node.next = self.head # new node.next gets set to current head node
        self.head = node #assign this node as the head now

    #Runtime??  O(n) or O(number of nodes)
    def insert_at_head_or_overwrite(self, node): #takes in a node, either inserts it at the head or it will override the node in that linkedlist
        #reuse the functions that we've made to implement this function
        existingNode = self.find(node.value)
        if existingNode is not None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)

    #Runtime of delete()??  O(n) or O(number of nodes) Linear Time
    #Space complexity?? O(1) Constant time b/c space requirements don't change based on the input. Only initializing two pointers and moving them along the list.
    def delete(self, value):
        curr = self.head #set reference to current node, starting at the head

        if curr.value == value: #this takes care of the edge case where we are deleting the head node. If the current value (head) is the value we want to delete...
            self.head = curr.next #...make sure we move the head to the next value of the current head
            return curr # also want to return the node that we deleted

        #Need two pointers:
        prev = curr # previous pointer/slower pointer
        curr = curr.next #current pointer/one pointer ahead of previous

        while curr is not None: # iterate through the entire list, since front pointer is curr, make sure that curr is not None, or not in the list
            if curr.value == value: #if the fast pointer/current is value we want to delete, then we've found it, so make...
                prev.next = curr.next #..."previousPointer.next will now be currentPointer.next"
                curr.next = None #remove the connection b/c it won't be a part of the list anymore
                return curr #return node that we deleted
            else: #if we haven't found the node that we want to delete yet...
                prev = curr
                curr = curr.next #move the pointers forward by 1

        return None # if we pass this while loop, return None because we haven't found the node we want to delete

    #Runtime of find() method???   O(n) or O(number of nodes) Linear Time b/c worst case for this function is we need to traverse the entirety of this list
    def find(self, value): #traverse list starting at head until next pointer is none
        curr = self.head
        while curr is not None:
            if curr.value == value: # if we've found node we're looking for...
                return curr #  ...return the value
            curr = curr.next # if not, we'll go to the next one
        return None # if we pass this while loop, it means we traversed the entirety of the linkedlist, so we return None

a = Node(1)
b = Node(2)
c = Node(3)
ll = LinkedList()
ll.insert_at_head(a)
ll.insert_at_head(b)
ll.insert_at_head(c)
ll.insert_at_head_or_overwrite(a)

print(ll)