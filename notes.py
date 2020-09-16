# Hash Tables
​
![Image of Hash Table Collision Solved Using Linear Probing](https://upload.wikimedia.org/wikipedia/commons/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg)
​
​
## Description
- A hash table is a fixed sized data structure in which the size is defined at the start. 
​
### Intro 
- Hash tables are excelent for quick storage and retrieval of data based on key-value pairs. Just like javascript objects. 
​
&nbsp;  
​
​
| Key         |  Value      |
| ----------- | ----------- |
| 0 | item 0|
| 1 | item 1|
| 2 | item 2|
| 3 | item 3|
| 4 | item 4|
| 5 | item 5|
| 6 | item 6|
​
&nbsp;  
​
​
### Notes:
- A hash table contains two main functions: put() and get().
- The put() function is used for storing data into the hash table.
- The get() function is used for retrieving data from the hash table.
- Both get() and put() functions have O(1) - constant time complexity.
​
## Hash Function
- Map every character in the string to its unique code. 
- Sum up all the numbers
- Mod the hash value with the table size to get the index.
​
## Put method
- Run key string throught the hash function to get the hash value.
- Store the value at the index in the bucket.
​
## Get Method
- Hash the key and get the index of that bucket.
- If there is no value in bucket at that index return null
- Return value
​
## Delete Method
- Hash the key and get the index of that bucket.
- If there is no bucket in that index return null
- Return value
​
### Example:
- The localStorage is an example of a data structure based on a hash table. It is a native JavaScript object. It lets developers persist data inside the browser, meaning it can be accessed after a session.
​
```
    localStorage.setItem("testKey", "testValue");
    location = location; // refreshes the page
​
    //--------------------------------------------
    localStorage.getItem("testKey"); // prints "testValue"
```
​
# Hashing Techniques
 - The hash function converts a specified key into an index for an array that stores all the data.
​
 #### *Good hashing requirements:*
​
 - *Deterministic:* Equal keys produce equal hash values.
 - *Efficiency:* It should be O(1) in time.
 - *Uniform distribution:* It makes the most use of array.
​
## 1. Prime Number Hashing
### Notes:
- By using the modulus operator with prime numbers, a uniform distribution of the index can be guaranteed. See, modules division using prime numbers yields an array index in a distributed manner. 
​
**Modules number:** 11
```
    4 % 11 = 4 collision same key
    7 % 11 = 7
    9 % 11 = 9
    15 % 11 = 4 collision same key
```
​
### Example:
​
*before:*
​
| index  |  0 |  1 |  2|  3 | 4  | 5  | 6 | 7 | 8 |  9 | 10|
|---|---|---|---|---|---|---|---|---|---|---|:-:|
keys|   |   |   |   |   |   |   |   |   |   |   |
values |   |   |   |   |   |   |   |   |   |   |   |
​
&nbsp;  
​
​
​
### Let's hash this key value pair
```
{key:7, value:"hi"}
{key:24, value:"hello"}
{key:42, value:"sunny"}
{key:34, value:"weather"}
​
Prime number: 11
7 % 11 = 7
24 % 11 = 2
42 % 11 = 9
34 % 11 = 1
```
​
*after:*
​
| index  |  0 |  1 |  2|  3 | 4  | 5  | 6 | 7 | 8 |  9 | 10|
|---|---|---|---|---|---|---|---|---|---|---|:-:|
keys|   |  34 |  24 |   |   |   |  |  7 |   |  42 |   |
values |   | weather  |  hello |   |   |   |   |  hi |   | sunny  |   |  
​
&nbsp;  
​
# Probing
​
- To work around occurring collisions, the probing hashing technique finds the next available index in the array. The linear probing technique resolves conflicts by finding the next available index via incremental trials, while quadratic probing uses quadratic functions to generate incremental trials. 
​
## Linear Probing
- Linear probing works by finding the next available index by incrementing one index at a time. In other words, if there is a collision it will find the next available empty spot. 
​
&nbsp;  
​
```
{key:7, value:"hi"}
{key:24, value:"hello"}
{key:42, value:"sunny"}
{key:34, value:"weather"}
{key:18, value:"wow"}
​
Prime number: 11
7 % 11 = 7 
24 % 11 = 2
42 % 11 = 9
18 % 11 = 7 collision applying linear probing becomes: 8
```
​
| index  |  0 |  1 |  2|  3 | 4  | 5  | 6 | 7 | 8 |  9 | 10|
|---|---|---|---|---|---|---|---|---|---|---|:-:|
keys|   |  34 |  24 |   |   |   |  |  7 | 18  |  42 |   |
values |   | weather  |  hello |   |   |   |   |  hi | wow  | sunny  |   |  
​
&nbsp;  
​
​
*Note:*
- The main disadvantage of linear probing is that it easily creates cluster, which are bad since they create more data to iterate through. 
​
&nbsp;  
 
![Image of Hash Table Collision](https://www.sysadmins.lv/content/images/pages/2047/ht-collision.png)
​
![Image of Hash Table Collision Solved Using Linear Probing](https://www.sysadmins.lv/content/images/pages/2047/linear-probing.png)
​
&nbsp;
​
## Quadratic Probing
- Quadratic pribing is a good technique for addressing the cluster issue. Quadratic probing uses perfect squares instead of incrementing by 1 each time. This helps to evenly distribute across the available indices. 
​
&nbsp;
​
![Linear and Quadratic Probing](https://www.codingeek.com/wp-content/uploads/2017/07/linear-and-quadratic-probing.png)
​
​
# Rehashing/Double Hashing
- Another great way to uniformly distribute the keys is by having a second hashing function that hashes the result from the original.
​
### Requirements of a good second hash table
- *Different*: It needs to be different to distribute it better.
- *Efficiency:* It should still be O(1) in time.
- *Nonzero:* It should never evaluate to zero. Zero gives the initial hash value. 
​
*Note:*
- A common use second hashing function is a follows:
    ```
    hash2(x) = R - (x % R)
    ```
- Here x is the result from hashing the first time, and R is less than the size of the hash table. Each hash collision is resolved by the following, where i is the iteration trial number:
        ```
            i * hash(x)
        ```
​
​
# Summary 
- A hash function is a fixed data structure in which the size is defined at the start. 
- Hash tables are implemented using a hash function to generate an index for the array.
- A good hash fincthing is deterministic, efficient and uniformly  distributive. 
- Hash collisions should be minimized with a good uniformly distributive hash function, but collisions having some collisions is unavoidable.
- Hash collisions handling techniques include but are not limited to linear probing (increment by 1), quadratic probing (using a quadratic function to increment the index), and double-hashing(using multiple hash functions).