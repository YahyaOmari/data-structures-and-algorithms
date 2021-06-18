# Hash table:
<!-- Short summary or background information -->
- A hash table is a special collection that is used to store key-value items. So instead of storing just one value like the stack, array list and queue, the hash table stores 2 values. These 2 values form an element of the hash table. Below are some example of how values of a hash table might look like

### Challenge:
<!-- Description of the challenge -->
- 
### Approach & Efficiency:
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Create a list with 1024 None elements, whenever we add a value it will check if it's existed in the location, if there is not(none) it will create a linked list and insert to it, else it will add to the existing linked list.

- Big O of time --> O(1) Big O of space --> O(1)


### Solution:
<!-- Embedded whiteboard image -->


<!-- ![Hash table](../assets/.jpg) -->

- [Code of Hash table](hashtable.py)