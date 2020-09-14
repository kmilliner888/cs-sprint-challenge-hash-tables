class HashTable {
  constructor(size) {
    this.size = size;
    this.buckets = this.initArray(size);
    this.limit = 0;
  }
  // to populate the hash table
  put(key, value) {
    // check if hash is at limit
    if (this.limit >= this.size) throw "Hash Table is full";
​
    // run the str throught the hash function to get hash value
    let hashIndex = this.hash(key);
​
    // Linear probing - while there is value at tha specific index in buckets
    while (this.buckets[hashIndex] !== null) {
      // increase the index
      hashIndex++;
    }
​
    // Store the value at the index in the bucket.
    this.buckets[hashIndex] = value;
​
    // increase our limit
    this.limit++;
  }
​
  // to get values out of the hash table
  get(key) {
    // Hash the key and get the index of that bucket.
    let hashIndex = this.hash(key);
​
    // If there is no bucket in that index return null
    if (this.buckets[hashIndex] === undefined) {
      return null;
    } else {
      return this.buckets[hashIndex];
    }
  }
​
  // delete method
  delete(key) {
    let hashIndex = this.hash(key);
    // If there is no value in bucket at that index return null
    if (!this.buckets[hashIndex]) {
      return null;
    } else {
      this.limit--;
      return (this.buckets[hashIndex] = null);
    }
  }
​
  initArray(size) {
    const array = [];
​
    for (let i = 0; i < size; i++) {
      array.push(null);
    }
    return array;
  }
​
  hash(key) {
    // place holders
    let total = 0;
    let hashIndex;
    // Map characters in the key to its unique code
    for (let i = 0; i < key.length; i++) {
      let charCode = key.charCodeAt(i);
      // sum up the values
      total += charCode;
    }
    // Mod the value to the size of my hash table
    hashIndex = total % this.size;
​
    // return index
    return hashIndex;
  }
}
​
// sanity check
const table = new HashTable(3);
console.log("Hash Table:", table);
​
// testing put method
table.put("foo", 1);
table.put("bar", 2);
table.put("baz", 3);
console.log(table);
​
// testing get method
let result = table.get("baz");
console.log("This is bazz:", result);
​
// testing get method
result = table.delete("baz");
console.log("This is bazz:", result);
console.log(table);
​
// testing for size full
table.put("blahblaya", 13);
console.log(table);
table.put("not sir", 20);