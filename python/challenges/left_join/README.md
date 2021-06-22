# Summary and the challenge of Left Join.
<!-- Short summary or background information -->
- The left-join keyword returns all records from the left table(t1), so the matched records from the right table (t2). The result is None from the right side, if there is no match.

### Approach & Efficiency:
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Create function called left join which takes two parameters. 
    - The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
    - The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
- Check if the first hashtable contains the value of the second hashtable.
- Add the values if true.
- Give the result (return) when the keys finish

### Solution:
<!-- Embedded whiteboard image -->
### [Code of left_join](left_join.py)

