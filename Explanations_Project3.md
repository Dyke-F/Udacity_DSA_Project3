# Project 3 - Explanations

---

**Problem_1**
___

The goal of this task is to calculate the square-root of a given number in a reversed manner by squaring a given input number and comparing it to the source value. To achieve the required time complexitiy, we here used binary search on values ranging vom 0 until number // 2 (because the square root of a number is always <= the floor division by 2) (thus additionally limiting the search space).
In binary search, divide the range of numbers in half (center) and check wheter center ** 2 is lower or higher or equal to the desired number and recurse on the lower / upper half again.
In case the square root is not an integer, when center ** 2 is lower than the input, check if the next largest center (center+1) ** 2 is higher than the desired number, calculate the difference and round accordingly. 

Time complexity: According to binary search, this is **O(log(n))**\
Space complexity: Independant, no new objects are created: **O(1)**

**Problem_2**
___

In this task we used binary search twice: First to find the pivot (the "break" in the sorted list). The pivot here equals a number that comes after a number that was larger than the pivot.
Second we used binary search to find the target number in 1 of the two sublists, depending wheter our value lies in the sublist before or after the pivot.

Time complexity: According to binary search, this is **O(log(n))**\
Space complexity: Independant, no new objects are created: **O(1)**

**Problem_3**
___

As stated the time complexity was supposed to be **O(n * log(n))** which made it obvious of using one self-implemented sorting algorithm like mergesort or quicksort. Afterwards we iterate through final sorted list 1 more time **(O(n))** to assign numbers to both values.
Space complexity depends on the lenght of our input as python holds the array the whole time while sorting it.

Time complexity: According to quicksort, this is **O(n * log(n))**. \
Space complexity: We rearrange the array in place, so: **O(n)**

**Problem_4**
___

I offer two versions to this problem:

Version 1: Dictionary Solution
Here we iterate through the entire list once (time complexity: **O(n)** and assign values to dict keys (Space complexity: **O(n)**).
Then we reassign a new list with the sorted values (additional space required, however the old list can be deleted, so this can be neglected). This version is indeed very fast to code and requires no pointes.

Version 2: 
Rearrange the items in place in one traversal, thus also time complexity of **O(n)**. However no new space is required: **O(1)**.



Time complexity: According to quicksort, this is **O(n)**. \
Space complexity: Version1: **O(n)**; Version2: **O(1)**.

**Problem_5**
___

Building a Trie, a relative of tree data structures for autocompletion of words: As we need to push every word character by charater into the Trie time complexity is O(x * n) where x is the length of a word and n the number of words. Space complexity can vary largely. If we have two words that overlap heavily its low. If two words like "donald" and "trump" have no character in common, Tries dont offer any benefit in this case. So worst-case scenario **O(n)**.

Time complexity: **O(x * n)**. \
Space complexity: Worst: **O(n)**.

**Problem_6**
___

Time complexity of one traversal of the input list is **O(n)**. Space complexity is O(1) as nothing in the input list is changed, only we are indexing in a for loop.

Time complexity: **O(n)**. \
Space complexity: **O(1)**.

**Problem_7**
___

Again like in Task 5 we used a trie data structure to build a web page router. Space complexity again can vary based on the overlap in website domains. If they are totally different we end up with a space complexity of **O(n)**. Time complexity depends on the task. Building up the trie, meaning inserting webpages takes **O(n)** time as we have to iterate through the entire domain to save it. \
Searching can be faster, for instance if we reach a path thats unique and might lie below **O(n)**.

Time complexity: Depending on the task, could be **O(n)**. \
Space complexity: Worst case: **O(n)**.
