**Data Structures:**
  - Hash Tables
  - Linked Lists
  - Stacks
  - Queues
  - Tries
    Heaps
  - Graphs
  - Trees, Binary Trees and BST:
    - Binary Search
    - BFS/DFS
  - Sorting
    - Quick Sort
    - Merge Sort
    - Quick Select Algorithm

**Line of Attack:**
- Start:
    - Asking clarifying questions
    - Input validity: Null/range, data types
- Ask for example. Can come up with another example. The example has to be not too simple or too complex.
- Walkthrough the algorithm. Start with brute force, try to optimize, confirm the solution verbally - Know your data structures
- The variables and when they change
- Corner Cases: negative, null, repeated/duplicates, non-continuous, too big, too homogeneous
- Then start coding
- Discuss time and space complexity
- Modularize your code first. Especially functions that might be uninteresting. When you have the skeleton of the code, start filling in the details

**Preparation Guide:**:
- Practice more problem types than a lot of one type
- Target 15 minutes for medium and hard leetcode
- Revise highlights of the Cracking the Coding Interview book

**Recursion:**
- Prune the recursion whenever possible
- Thinking bottom-up/base cases instead of top-down  might make it easier to think and then top-down
- For recursive calls, often we make use of original arrays, original pointers, or pointers with the original reference

**Need Clarification:**:  
- What if the base case is not O(1) in recursion? Do we multiply by number of rescursive calls?
- Do we explicity delete pointers in Python by setting to None or garbage collector takes care of it? For example:

#         delete = prev.next # useless step?
#         prev.next = prev.next.next
#         delete = None # useless step?


**General Python:**
- -ive numbers with positive modulo give weird results. if needed, do module with negative divisor. 
- Python functions argguments passed by reference
  - A class can have an object of its own class
  - All immutables like tuples are hashable. So can use them as dict keys. Sometimes, you might wanna convert list elements to a tuple or joint string for hashing.
    - Mutable objects have a tricky copy mechanism (a = [2], b = a, b[0] = 1 - a[0] = -1)
  - And since Python 3.7, official documentation states: Dictionaries preserve insertion order.
  - Use dict.values() instead of creating sublists manually

**General Definitions:**
- Every character is a palindrome
- Graphs can have loops unlike trees.
- Substring is contiguous, subsequence is contiguous, combinations is not and its completely differnet
- **The depth (or level) of a node is its distance (i.e. no of edge- s) from tree's root node. The height is number of edges between root node and furthest leaf.**
- **Power set is all possible combinations of all possible lengths, from 0 to n.
- A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
  - Non-decreasing means some values could be equal so not necessarily ascending.
  - # of subsets: each element include or not. If [1, 2, 3] > 2 x 2 x 2 = 2^n
    - Remember subset is not contiguous
    - Subsets are not combinations


**Other**:
- Maximize use of hash
- Think about running sums
 - Minor: use _ for variables that are not required, such as loop iterator to pretend you're a pro-grammer.
- If you have an order or if you have a range, just use it to iterate in a sorted order. No need to .sort.

    
**Linked-lists**:
- Linked Lists would need a dummy node (or None) or two pointer approach in many case. Two pointer could be a fast and slow (to detect cycle or middle). Or it could be in same direction and speed but with a gap to find from last nth node. Reverse can be iterative or recursive (like stack).
- dummy nodes are your best friends when dealing with linked lists
  - Pointers suck. Might just use stack for reversing linked lists.
    - Modify linked lists via in place



**Quick Select:**
    - The one I like is Lomuto btw
      - Easier to implemen
    - When already sorted, the middle index pivot in Lomuto results in base case N Log N
      - _Choosing a random pivot minimizes the chance that you will encounter worst-case O(n2) performance (always choosing first or last would cause worst-case performance for nearly-sorted or nearly-reverse-sorted data). Choosing the middle element would also be acceptable in the majority of cases._
    - Important: In Hoarse, the returned index is not necessarily the partitioned index
      - Need more understanding.
    - Hoare deals with duplicates and has less swap
    - While Hoare's scheme is indeed faster of the two, it doesn't fix the final position of the pivot element, hence can not be used in quickselect where pivot should be in it's final position after partitioning.
      - Actually it can be used but the fix is not so intuitive
    - Time Complexity:
      - Time complexity: \mathcal{O}(N)O(N) in the average case, \mathcal{O}(N^2)O(N2) in the worst case. Please refer to this card for the good detailed explanation of Master Theorem. Master Theorem helps to get an average complexity by writing the algorithm cost as T(N) = a T(N / b) + f(N)T(N)=aT(N/b)+f(N). Here we have an example of Master Theorem case III: T(N) = T \left(\frac{N}{2}\right) + NT(N)=T(2N)+N, that results in \mathcal{O}(N)O(N) time complexity. That's the case of random pivots.
      - In the worst-case of constantly bad chosen pivots, the problem is not divided by half at each step, it becomes just one element less, that leads to \mathcal{O}(N^2)O(N2) time complexity. It happens, for example, if at each step you choose the pivot not randomly, but take the rightmost element. For the random pivot choice the probability of having such a worst-case is negligibly small.
  


**Stack:**:
  - When encounter a situation where you have to traverse something till end before processing current element, use stack
  - *In the previous approach we rely on the system stack for our recursion's space requirements. However, as we all know, that stack is limited and for extremely long trees, it might not be feasible to use the system stack. So, we need to use our own stack that will be allocated memory on the heap and will be able to handle much larger sized trees easily.*
Monotonic stack (a stack with a certain order)
      - **Next Less Element and Previous Less Element problems can be solved efficiently**


**Arrays**:
  - Often O(n^2) array based solutions have some duplicated work being done.
    - Try caching
    - Or try maintaining a prefix-sum/max/min etc
    - Or use a hashmap?
- inf and -inf can be appended to lists before and after to simplify edge cases
- Instead of maintaining a list, try to see if you can store running/sum and number of items in a tuple
- When n^2 to get combinations look the first solution, see if dict can be used for linear type
- If implementing an equation, see if problem can be simplified using equation manipulation
- Whenever you're trying to solve an array problem in-place, always consider the possibility of iterating backwards instead of forwards through the array. It can completely change the problem, and make it a lot easier.
  - While rotating an array (i + k) % length will give new rightful position
  - If have to shift all elements in array again and again, can we just place them in the right position using a trick? %, placeholders, cyclic dependencies
    - Does visualizing the array/linked list in circular form simply stuff?
    - Sorting algorithms that are in-place
  - Changing Ascending to Descending may simplify a solution as well
  - First of all, the requirements of  **in-place replacement and constant space**  should immediately indicate  **swapping**
- It's a good idea to check array sizes and use a hash map for the smaller array. It will reduce memory usage when one of the arrays is very large.
- Try to simplify by sorting, reversal, math (equation manipulation)
- Instead of handling corner cases when subtracting in a cyclic manner, handle it with mod e.g. clock.
- Two-pointers
- Don't try to apply algos right away. There could be simple array swapping/other operations that can be used for a simpler solution.
 

        
**General Tips and Techniques:**:
  - Too many if conditions is a strong indicator that a simpler solution exists
  - There can be ways that you first apply the general algorithm and then do some corrections to match the problem statement
  - See whether starting index from beginning of the array has more chances to detect something or if you start from the last in reverse.
  - Problem Reframing: Can two problems have the same solution? For example, # of visible nodes from left-side is the same as returning height of the tree.
  - Read the question properly. Does it have anything that tells you to reuse past information?
  - When you need ALL the recursive calls to maintain/update something, just keep it outside the function (global variables).Dictionaries and lists are mutable objects which also imply that if they are defined outside ANY function, they can still be modified by function f or any inside f > f(g(h(…))) so no real need to pass by reference.
  - Applications of algorithms like binary search don't have to be EXACT. Sometimes minor modifications might be required to get the correct answer such as modified/adding a new base case, modifying how points ideally move etc.
  - Sometimes it's just easier separating two functions, one for calling and one for recursion, if there is some sort of set-up or loop required.
  - It may be nice to analyze big O and preference of a solution based on how it will be used in production. If for example, there's a certain query, is it a one off thing? Will there be a lot of inserts? Deletions? Searches? Ask frequency of operations from the interviewer
  - For every problem, see if we can return on some edge cases e.g. if lengths don't match, return False
  - Create decision tree for backtracking and explore every node like tree traversal
  - If the result is needed from inside out (two pointers), and its easier to code from outwards to inwards just do it and calculate result in reverse order.
  - # need a deep copy for 2d lists. can't use slicing or .copy().
Look for the twist. A detail. A detail that might look useless but it's there for providing a way to optimize.
    - Using input array as storage if it has extra
    - If input has useless elements
  - Sometimes reframing the problem simplifies or provides an opportunity for optimization
  - Whenever have to do a single O(N) pass, just make sure if the same can be achieved in previous iterations by maintaining a running sum/min/max etc.



**Connected Components:**
   - Whenever we must work with a set of elements (emails) that are connected (belong to the same user), we should always consider visualizing our input as a graph. In this problem, converting the input into a graph will facilitate the process of merging two accounts.
    - Any problem that involves merging connected components (accounts) is a natural fit for DFS or the Disjoint Set Union (DSU) data structure.
  - **Instead of jumping straight into DSU for connected components type of questions, check if labelling can be given using hashmaps.**

 
 
    

    
**Queue:**
    - queue:
      - queue.get(), .put(), .empty()
      - deque.popLeft()/pop(), append()/extendLeft, q
- Deque is better than queue
    
**Defining Graphs:**
- Adjacency matrix MAY sometimes be helpful than adjacency list (0 indicates self or disconnected).
    - tuple of edge as a key
  - Instead of deleting from heap, might just be better off not considering it when its time comes during popping. Lazy delete.
  - Defining graph:
    - - Choose format according to the problem. Do you even need a dictionary mapping or just a list of edges will work? If you need unique edges, defining a graph using a dict (adjacency list) will cause additional overhead.
    - Better to create a class with add_edge() method.


**Trees/Graphs:**
  - Can use depth-first or breadth-first to traverse a tree.
  - Design a basic class for example, a Node Class with value, right child and left child in a binary tree
  - Safe to assume that a binary search tree is balanaced or not? Is it a binary search tree or just a binary tree?
  - Topological Sort might be needed if we wanna extract the order but if we already have the order, just use hashmap and iterate over it.
**Eulerian Path is a path in graph that visits every edge exactly once. Eulerian Cycle is an Eulerian Path which starts and ends on the same vertex.**
    - Cycle if all degrees are even
      - Forget about 0 degree vertices
    - **In graph theory, an Eulerian trail (or Eulerian path) is a trail in a finite graph that visits every edge exactly once (allowing for revisiting vertices).**

**DFS vs BFS**:
  - If it is known that answer lies nearby the source node in graph, or to get optimal answer, BFS should be used.
  - BFS is ideal when we wanna find optimal path to take. We can make branches that can represent next potential steps and all of them would have the same cost as they all are siblings. In other words, we can label each solution and keep the label in the BFS queue.
  - DFS if answer lies quite far away or if backtracking is needed or if entire graph has to be traversed.
  - Cycle detection in a graph
  - Solving a maze because in DFS you explore every possible path before backtracking.
  - Checking if a graph is bipartite or not
  - Finding out strongly connected components of a graph.
  - Longest path between two nodes in a graph etc.


**DFS:**
    - There are cases where we are trying to backtrack essentially from the last failure with the help of a for loop to explore other solutions (similar to a graph structure / DFS for example). To catch a failed attempt and to continue exploring other options, catch the return False using an if condition and return True inside the if condition.




**Hashing:**:
  - Hashing: h(large_value) = large_value % size_of_hash
    - If I'm not wrong, for intergers hash = f(x) = x

  - **For very large numbers:**
    - **Hashing may result in collisions**
    - **I think this refers to constantly hashing a stream of numbers**
  - **If multiple queries, hashing overhead is amortized**
  - **Some comments from LeetCode on why we might be better off using arrays instead of hashmaps in case of very large numbers:**
    - **Your hash map will resize when it gets to 75% (by default) capacity, but then it will rehash everything. And this is likely to happen a lot. So between the resizing and the collisions, the hash map approach isn't going to scale well to a very large vector.**
    - **By using the array list you get around this. You don't have to worry about collisions and resizing is a bit cheaper because theres no rehashing when you resize an array list.**
      - **So I think if the size of array is such that it can be allocated in contiguous memory, array is better**
    - **Smaller or larger does not make them less or more sparse. For example, a vector could have 1 billion numbers, out of which only 10 million are non zeroes. This would be a very large list and still sparse vector. In a hash table, a common issue is hash collision. Typically we reduce collision by over allocating. For example, for a 10 million entry hash table, we might allocate memory for say 13 million entries based on 0.75% load factor. When we hash such large lists (I know 10 million ints is not really that large, but there are other items in memory and imagine many such parallel calculations being done) , we may start hitting memory limits so over allocating gets difficult, and we get too many hash collisions. Smaller in the context meant (and the interviewer gave me some similar numbers), 1 vector was 1 billion numbers and the other vector had only 1 million or less entries**
    - **I got this question today on my FB interview. I proposed the Hash solution, and he asked the downside to it. I responded with large size of sparse vectors, hash collisions will occur when we hit memory allocation limits, etc. He asked alternative solutions and I proposed array of (index, value) pair. He asked me to code that. Then he added a constraint where one vector is considerably smaller than the other, and asked if we can improve the time complexity from O(m+n). After some scratching around, I told them that we can by doing binary-search of small vector's index over the larger one. This should improve the time-complexity. Was not sure of the exact Big Oh, but it should be better than m  log(n), since the search space should keep reducing from n. Fingers crossed for the results**




**Combinations and Permutations:**:
Permutations: n! If r = n
    - Subsets = 2^n (since each element can be absent or present. I believe this equals subsequences)
  - Permutations are expensive. Avoid them at any cost through sorting, windowing, hashing
          - Permutations or combinations or subsets -> backtracking


**Bit Manipulation:**:
- XOR is commutative
    - can be used to extract unique number from list
- Odd-one out, unique, missing > XOR
  -   xor of number with 0 is itself. xor of number with itself is 0/
    - &amp-ing with 1 or 0 might help
    - to retrieve the right-most bit in an integer n, one could either apply the modulo operation (i.e. n % 2) or the bit AND operation (i.e. n &amp 1)
    - Observe patterns. Start with XOR, AND, NOT, Extracting last bits, shifting bits, settings bits
    - mod % 2 to extract last bit, >> to shift 
    - Adding two nums: (either do masking instead of this or do leetcode premium to find its answer)
      - Convert 8 usecases to two
      - Simplify problem down to two cases: sum or subtraction of two positive integers: **x + y , and x-y where x > y.** Save down the sign of the result.
      - If one has to compute the sum:
      - While carry is nonzero: y != 0:
      - Current answer without carry is XOR of x and y: answer = x^y.
      - **Current carry is left-shifted AND of x and y: carry = (x &amp y) << 1.**
      - Job is done, prepare the next loop: x = answer, y = carry.
      - Return x  sign.
      - If one has to compute the difference:
      - While borrow is nonzero: y != 0:
      - Current answer without borrow is XOR of x and y: answer = x^y.
      - **Current borrow is left-shifted AND of NOT x and y: borrow = ((~x) &amp y) << 1.**
      - Job is done, prepare the next loop: x = answer, y = borrow.
      - Return x  sign.
- **c = a + (~b) Difference of two integers using two's complement**


**Trees:**:
  - If a binary tree is balanced, depth first search traversal might only be log(n) space complexity
  - Level order BFS traversal can be done using:
    - Just use a single queue if no need to process nodes at a single level
    - Curr_level and next_level quques OR
    - Curr_level and n_current_level iterations

Graph:
  - **If graph is not weighted. We can consider each edge to have the same weight of 1. Since the graph is unweighted, BFS can be used to find the shortest path between a starting cell and any other reachable cell.**

DFS:
  - All Possibilies > DFS
    - Optimize along the way to minimize recursion by adding contraints and early stopping

Tree:
  - DFS:
    - If it's a graph instead of tree, we mark visited. We don't have to in a tree DFS.
    - Avoid creating additional visited set if modifying input is allowed

  - BFS:
    - In a graph, keep marking as visited before enqueing so we don't end up having duplicates in the queue
    - Think of BFS as a general framework. The exact implementation will be different based on the application.
      - Having same nodes with different costs in the queue (for example, in the form of priority queue) – Djikstra's/Prim's

  - At any given moment, the queue contains no more than  **two levels**  of nodes in the tree. The maximal number of nodes at one level is n/2​, which is the number of the leaf nodes in a balanced binary tree. As a result, the space needed for the queue would be O(_N_)
  - it would be _ **faster** _ to sort a series of subgroups than sorting them all together in a single group. Here is a not-so-rigid proof. Suppose that we have a list of _N_ elements, it would then take O(_N_log_N_) time to sort this list. Next, we divide the list into _k_ sublists equally. Each list would contain  _k/N_​ elements. Similarly, it would take O(_N/k_​log_N/k_​) time to sort each sublist. In total, to sort all the _k_ sublists, it would take O(_N_log_N/k_​), which is  **less than**  the time complexity of sorting the original list O(_N_log_N_)).
  - **DFS and BFS time complexity: O(n)**
    - Because this is tree traversal, we must touch every node, making this O(n) where n is the number of nodes in the tree.
  - **BFS space complexity: O(n)**
    - BFS will have to store at least an entire level of the tree in the queue (sample queue implementation). With a perfect fully balanced binary tree, this would be (n/2 + 1) nodes (the very last level). Best Case (in this context), the tree is severely unbalanced and contains only 1 element at each level and the space complexity is O(1). Worst Case would be storing (n - 1) nodes with a fairly useless N-ary tree where all but the root node are located at the second level.
  - **DFS space complexity: O(d)**
    - Regardless of the implementation (recursive or iterative), the stack (implicit or explicit) will contain d nodes, where d is the maximum depth of the tree. With a balanced tree, this would be (log n) nodes. Worst Case for DFS will be the best case for BFS, and the Best Case for DFS will be the worst case for BFS.
  - In backtracking (which is kind of a bruteforce) we have to undo changes for the next iteration
  - In dfs based structures, think about what makes more sense. Calling dfs iteratively from the main function or within the recursive function
    - 1st option: normayll when we have different starting points such as in labelling connected components
    - 2nd option: when we have multiple decisions to make within a single call




**Searching:**
  - Binary Search implementations can be tricky:
    - Check if you wanna include mid point for next search space or not and in what cases?
      - Can mid be a potential answer but you still wanna continue search until you narrow down to 2 or 1 options?
    - When does the while loop end
      - Searching for something? Might wanna check for single element
      - May not wanna execute when low == high if the low or high is the answer
      - Dry run and test if the while loop is infinite by testing for an array of size 2
    - It's not necessary that the mid point will always be the answer
    - I think if low = mid, then check for last two remaining examples. I think eventually it might lead to infinite loop.
      - Simple way is to break out and compare two values separately
  - While implementing recursion such as DFS:
    - Sometimes it might help to have conditions checked in the base cases instead of doing checks before making recursive calls. That is, it will help reach the base case to return answer instead of complicated logic in the main body.

**Common Problems:**
- Plot graphs in problems similar to stocks/heights.
- Elements sum to k:
      - Determine if –ive elements / sorting order
      - Start with bruteforce
      - Optimize by either adding a cum sum or just maintaining a single variable and reusing it (subtracting / resetting to 0)
      - Use equation to check value in hashmap (optimal)
- Flyod's algorithm to detect cycles in linked lists (the rabbit turtle thing). If there's a cycle, the rabbit and turtle will meet at some point other than starting point.
- Anagrams: Make sure to try to use frequency in array (Better to use array than hashmap as letters are limited)
- To check if prime, don't need to check divisors till n.
  - n/2 > because there is no integer after n/2 that will multiply by 2 (the smallest partner someone can get) that will not cross n.
    - In other words, 2 is the smallest factor possible
    - After n/2, all the 2  other_factor would obviously cross n
  - sqrt(n) > because if see closer, e.g. 16 has 4 sqrt. 4 x 4. This means that although it may have factors above 4 (indeed it does, 8) but those factors above will ALWAYS need values less than sqrt(n). Thus, if a number is not a prime, we should be able to detect it by dividing until sqrt(n) inclusive.
  - **claim # 1: for sqrt(n) + 1 and onwards, all the composites until n will be covered by the primes below sqrt(n).**
    - **The Sieve of Eratosthenes code on Wikipedia is intended to generate a list of all primes up to n. if k ≤ n is not prime, so we have two factors a, b. We can't have a, b both larger than n−−√, as then k=ab would be larger than n. Thus in order to show that k is prime, we only need to check that it is not divisible by a number up to n−−√. Equivalently (and this is the key insight in the Sieve) we only need to check that it is not divisible by a prime up to n−−√.**
    -
  - **claim # 2: for a prime number p, smaller prime numbers will have marked composites until p  p**
    - **25 already crossed 10 so 52 not needed. 35 already crossed 15 so 53 not needed...**
- Paranthesis:
    - If only same time of bracket, no need to use stack. If at anytime balance < 0, return False or if final balance is positive.
        - If single type bracket, mostly stakc is not required. Try multiple examples to see if balance can be used. Try multiple ways:
      - Count whenever balance goes negative
      - Combine with end balance
      - Etc.
- Fast Power Algorithm:
    - Log(N)
  - When trying to identify elements in decreasing or increasing order
    - Monotonic stack

Diagonals:
    - It turns out two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.
      - Or the plus ones
    - This leads to the following idea: remember the value of that diagonal as groups[r-c]
Intervals:
    - Sometimes you don't have to look at overlaps. There are other ways to look at the problem e.g. instead of finding overlap and then subtracting to get duration of intervals, just keep on accumulating the duration over time.
    - Think of keep a track of latest timestamp or event date.
  - However, like all in-place algorithms, overwriting the input can cause problems. Here are a couple of possible scenarios you need to consider.
    - That the algorithm is running in a  multithreaded environment, and it does not have exclusive access to the grid. Other threads might need to read the grid too, and might not expect it to be modified.
    - That there is only a single thread or the algorithm has exclusive access to the grid while running, but the grid might need to be reused later or by another thread once the lock has been released.
    


**Tuples:**:
  - Tuples are great for keep track of some information while new information keeps coming in.
  - While designing new data structures, think about
    - Tuples and storing information in them
    - Complementary data structures
  - Use tuples to store info to extract final answer instead of storing all the candidate answers:
    - For example, (window length, left, right)
  - If possible, delete useless stuff and keep the useful information in a tuple to reduce the number of iterations resulting in a single pass.
  - Use tuple instead of ''.join while hashing
  - Sorted(tuple()) might be a good idea to track results
  
**Sets:**
- Use sets to avoid duplicates and when O(1)/hashing required
  
**Strings:**
  - While working with characters, ASCII value of a character may help like ord(c) - ord('a')
  - If array is sorted or made sorted, two pointers might be helpful
  - First, make sure what do we have to output. Is it the values or the indices?
  - Two pointers (e.g. Expand and Contract, left and right, etc.)
  - Many times keeping counts in dictionary will help
  - Why maintain two lists when you can maintain a list of tuples (with corresponding elements) for association
  - Feel like popping multiple items from the queue just because its FIFO? Why not just slice and dice (NOT SURE ABOUT THIS ONE AS CREATING SLICES CAN LEAD TO MORE TIME/SPACE COMPLEXITY
  - While processing strings, do see if stacks can help or if checking validity, create a state machine.
  
- Deterministic Finite Automation (State Machine)
- problems where we have to process a user input with multiple conditions to account for, especially string processing, -> DFA/state machine solution using if/else or dict
- Make as many states to keep it simple
- See if using list of hashmaps can simplify the code:
  - Index corresponds to state number
  - Hashmap at the index tells which keys are allowed and the key to state mapping



**Binary Trees:**
    - The key observation to make is: the longest path has to be between two leaf nodes.
    - Here is the funny thing about BST. Inorder traversal is not a unique identifier of BST. At the same time both preorder and postorder traversals are unique identifiers of BST. From these traversals one could restore the inorder one: inorder = sorted(postorder) = sorted(preorder)
      - Inorder + postorder or inorder + preorder are both unique identifiers of whatever binary tree
    - In case of Binary Search Trees, only preorder or postorder traversal is sufficient to store structure information.
      - **Method 1:**
        - Need to extract in-order by sorting as well
        - Select node from pre
        - Find index using hashset from inorder
        - Use index to partition left and right subtrees
        - Increment pre_index counter
        - Left and right pointers used only in base case as a stopping condition to indicate subtree has ended
      - **Method 2:**
        - Just use value ranges as a base case
    - For a complete Binary Tree, level order traversal is sufficient to store the tree.
      - Like heap is a complete binary tree. It uses can array and children can be accessed at particular indices. Do simple recursion that creates a node with arr[i] value and recurses while setting right and left children.
    - A full Binary is a Binary Tree where every node has either 0 or 2 children. It is easy to serialize such trees as every internal node has 2 children.
      - We can simply store preorder traversal and store a bit with every node to indicate whether the node is an internal node or a leaf node.
      - Or use preorder and postorder. Preorder tells what is the root and postorder tells elements that are children/grand-children of the root. Do this recursively.
    - How to store a general Binary Tree?
      - A simple solution is to store both Inorder and Preorder traversals
      - OR Have nulls indicated by None for every non-NULL node's children and do pre-order traversal with None as a base case**
      - Preorder's first element is root. It's index in Inorder would give a midpoint. Elements to left belong to left subtree in inorder and SAME NUMBER of eleements in preorder.
      - In-order of BST is a sorted array.

**Binary Search:**:
  - I think once trick to binary search is that when I know I can find something in mid, maybe I check for when low == high, otherwise, low/high is the answer, no need to check for mid in the while loop.
  - Quick Sort:
    - Just use the method for last element as pivot. If required another method, just select it e.g. the middle index, swap it with last and continue with the same logic as the last one.
    - Follow the logic in the notebook.
    - Same code can be adapted to return kth largest/smallest or k largest/smallest.
      
  -  At any given moment, a queue in BFS level order traversal would hold no more two levels of nodes.
  - For a binary tree, the maximum number of nodes at a level would be N+1 / 2​ which is also the number of leafs in a full binary tree.
    
  - Make sure to make most out of running sums/running mins/running maxes instead of creating another pass.
  - For parenthesis related questions > stack / calculate balance (1 for closing/-1 for opening / max size of stack
    - If balance can solve the problem, no need to create additional stack
  - Need to process something after? >>>>>>> Stack




**Math:**
  - Equation involved? HAVE to do some manipulation like log/anti-log and stuff. (NOT SURE WHAT WAS THIS)
    - Unique/Prime Factorization Theorem:
      - every integer greater than 1 can be represented uniquely as a product of prime numbers, up to the order of the factors
      - ![](RackMultipart20220405-4-se8081_html_75f7df9fc7a80328.png)
      - The theorem says two things about this example: first, that 1200 can be represented as a product of primes, and second, that no matter how this is done, there will always be exactly four 2s, one 3, two 5s, and no other primes in the product.
      - For example, characters can be assigned a prime number. A string will have a different product than another string but the same product as its permutations.

**Sorting:**
    - Insertion would work best if an array is already sorted / small array
      - because it will quickly break the for loops because of its simplicity and no overhead of space allocation/recursion
    - Bucket sort needs to have distributed data to be useful, otherwise, it's just a waste of time to achieve the same thing with extra steps.
      - More memory
      - Good for parallel
    - Counting sort won't make sense when n < range
      - Normally a small range with duplicated elements
    - Quick Sort requires less space than merge sort since there is no merging. Worst case is O(n^2) but randomizing pivot leads to O(nlogn)
- dependencies/ordering is a strong indicator of graphs and topological sort
  - Quick Sort:
    - Concept: Divide and Conquer:
      - A group of students ask students to arrange themselves one by one.
    - The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.
  - QuickSelect:
    - It is not recursive.
    - First iteration: check all points and subsequently keep (almost, hopefully) halving:
      - _N_+N/2 + n/4 … = N
  - While calculating distances of point, using squared distances might help reducing computation since its all relative.
  - Whenever k-lowest or k-highest:
    - If ordering not required, make the most out of it
    - If no, see if we can use heap
      - Heap can be further optimized by maintaining the size k. Only pushpopping when needed.
      - Even if we need min, using max heap can help to see if the curr max is a part of final answer or not
    - When the k-elements are not part of the actual array (such as a calculation):
      - Can use a modified binary approach, e.g. by calculating the target distance at every iteration.
        - If < k elements, all curr elements satisfiying the condition are part of the final answer
        - If > k, just reduce the domain by (high > mid)
        - Caution: squared distances will skew datapoints resulting in uneven partitioning
    - Use QuickSelect to further optimize by doing inplace selection of k elements
- Bucket Sort:
    - Floating:
      - Create n buckets. Determine bucket index by multiplying number by n.
    - Integer
      - Range = max – min / n e.g. max = 10, min = 0, n = 5 then range = 2
      - Create n buckets based on calculated range – (12,34,56,78,9-10)
      - BucketIndex = ( arr[i] - min ) / range
        - If arr[i] = 10, index = 10 – 0 ) / 2 = 5
        - Remember to test for last element (max). Might just be easy to dump into the last bucket.
  - When/if array is sorted, leverage binary search
  - When guess work to optimize something and converge to a solution -- binary search
  - Counting sort can not be applied to floating as we use keys as index in counting sort. if keys are floating point numbers so use bucket



  




**Clarifications to ask the interviewer / small talk:**
  - Is the input sorted?
  - Duplicates allowed in the binary tree?
  - Single linked list or doubly linked list?
  - Do I need to implement classes?
  - Subsequence will be contiguous or just a subset?
  - Is it safe to assume that the input can be modified?
  - Example: What should we return when needle is an empty string? This is a great question to ask during an interview
  - What if input list has 0 or 1 elements only?
  - Can elements be negative
    - Medium:
    - Should this be done be in place? (No additional memory)
    - Can we make any assumptions about the input?
    - **Do we care more about performance or saving memory?**
      - **Too often, candidates make assumptions about the problem (i.e., all integers are positive, arrays are not empty, all input is safe) … big red flag.**
  - **You should always discuss the possibility of overwriting the input with your interviewer and clarify what kind of environment your algorithm is expected to run in. Sometimes they won't care, sometimes they'll state it has to run in a multithreaded environment, or sometimes they'll have a particular preference as it impacts what they're trying to see from you.**
  - Is the tree balanced? Complete? Binary?


  - Binary Search:
    - Can guess loose boundaries for initial search space and iterate
     - Binary search remains tricky to implement. Is it mid or mid + 1? Do we return left or right and until when does the loop run.
    - Do test infinite loop
    - I think the safest thing to do is to test last two remaining separately.
      
  - In subarray sum etc problems, just start with creating a cum sum and if question talks about mod, just develop a mod table.
    - Remember that if you have a mod X, adding the divisor to numerator will result in the same mod again. This way you can detect sums.
  - When wanna group stuff, connected components is one way but if working with strings, and trying to group different sequences of strings together, designing a hash key to use might be the only way to go about it.
    - Can use collisions to our advantage.
    - See if processing char by char makes more logical sense or splitting by a delimiter.
  - Visualize things in a practical manner as well in addition to in a data structure-oriented manner. E.g. if visualizing a unix file path, it makes sense to first visualize the problem by creating a tree similar to what we see in Windows file explorer.
  - 

      
  - Do check if any sort of computations can be performed along the way. (Deduplication)
    - Remember the operator precendence. If  or / are included:
      - Have cur_operand, prev_operand and value to take care of precendence
        
  - **Spanning Tree:**
      - **Wighted, undirected, connected graph**
    - **Kruskal:**
      - **Uses DSU**
      - **E Log E for sorting and since we are taking union of nodes E times, that is E log V. E in worst case is V^2 so it's gonna be E log V**
        - **Actually not log N. Remember with both path compression and union by rank, it actually becomes O(alpha N) where log is actually an upper bound and alpha refers to co-efficient of inverse Ackermann function**
    - **Primms:**
      - **Uses heap for optimal implementation**
      - **O(V log E + E log E) time and O(E + V) space**
        - **If edges in heap and V Log V + E Log V if nodes in heap by using min-heap operation**
        - **Note that V might just be bounded by number of edges so expression might be further simplified**
  - Shortest path from source to all nodes: djikstra's
    - Dijkstra's algorithm doesn't work for graphs with negative weight cycles. It may give correct results for a graph with negative edges but you must allow a vertex can be visited multiple times and that version will lose its fast time complexity.
      - For graphs with negative weight edges and cycles, Bellman–Ford algorithm can be used
    - Similar to Prim's, uses heap
    - O(V log E + E log E) time and O(E + V) space
    - The process that underlies Dijkstra's algorithm is similar to the greedy process used in Prim's algorithm. Prim's purpose is to find a minimum spanning tree that connects all nodes in the graph Dijkstra is concerned with only two nodes. Prim's does not evaluate the total weight of the path from the starting node, only the individual path.
      - Wanna connect all cities with railyway tracks > Prim's
      - Wanna plan travel route starting from home > Djikstra's
  - Space depends on the sorting implementation which, usually, costs O(1)O(1) auxiliary space if heapsort is used.
  - Feel free to use python tricks like len(set()) etc.
  - Be smart when you have two arrays to process. Might be more efficient to process smaller array first.
  - While doing two-pointers, try to control the loop with the fast-moving or the more progressive pointer and try to restrict with a single outer while loop instead of having an internal loop as well. This will result in a simpler implementation. Opposite can be true sometimes as well.
  - Grouping cells in a 2D Matrix:
    - Left-to-right diagonal: r + c
    - Right-to-left diagonal: c - r
    - Boxes of size k: (r // k, c // k)
  - Arrays:
    - # speed up the rotation
    - k %= len(nums)
  - To optimize space, using bits might be more efficient
  - Beware: even if using an array or hashmap or set, if the size is gonna remain constant with respect to input size than we don't count it in space complexity.
  - **Use a hash table instead of a fixed size counter. Imagine allocating a large size array to fit the entire range of unicode characters, which could go up to more than 1 million. A hash table is a more generic solution and could adapt to any range of characters.**
    - **This is contradicting to my understanding above.**
      - **Actually not. I think the main point here. In this question Valid Anagram, we preallocate memory for storing freqenices of ASCIIs which aer only 26. So hashing them is useless and slow.**
      - **If it were all the Unicode characters (1million), it will result to a useless sparse vector and we may start hitting memory limits.**
    - **In this issue for SparseVector question, we keep increasing the size of either hashmap or list. For very large, collisions may start occurring in hashmap thus reducing performance and, although both hashmap and list will need to resize (hashmap resizes at 0.75 load factor by default),**  **the resizing is cheaper in case of arrays.**
      - **The performance of dot product is still far more efficient so might depend whether insertions are more frequent or dot-products.**
        - **If we go with the array of tuples route AND one of the vectors is not sparse enough, do binary search instead of linear scan**
  - Don't jump into using a trie if you see prefix. That depends if the query will be repeated or not. If yes, trie will be more efficient as it compresses the information.
    - For complete English dict, 70% compression
  - If messing up with input such as linked list or matrix, see if you can restore it
  - **to retrieve the ** _ **right-most** _** bit in an integer n, one could either apply the modulo operation (**_ **i.e.** _** n % 2) or the bit AND operation (**_ **i.e.** _** n &amp 1). Add binary numbers using &amp or OR.**
  - Trying to do 2 Pass over a single array?
    - Either you are doing duplicating work
    - Or if not, see if you can reduce the space required.
  - While processing string, check if dropping irrelevant characters reduces runtime
  - Instead of comparing dictionaries of counters, can we just keep a count of how many characters have been found?
    - formed_count
    - instead of comparing dicitonaries, compare arrays
  - but there is popular Facebook variation of this problem when interviewer provides you two numbers and asks to sum them up without using addition operation. No addition? OK, bit manipulation then. How to start? There is an interview tip for bit manipulation problems: if you don't know how to start, start from computing XOR for your input data. Strangely, that helps to go out for quite a lot of problems, Single Number II, Single Number III, Maximum XOR of Two Numbers in an Array, Repeated DNA Sequences, Maximum Product of Word Lengths, etc.
  - Inverse Ackermann Function:
    - I couldn't comprehend what Ackerman function really is but looks something that is even worse than exponential
    - It's inverse is really slow with an upper bound of O(logN)
      -  that it doesn't exceed 4 for all reasonable N_N_ (approximately N < 10^{600}_N_<10600).
  - XOR is addition without taking into account carry
    - Take XOR of x and y to get sum without carry
    - Get carry as AND and shifted one bit to the left
    - Make carry your new Y and continue until carry dies down
  - BFS will have nodes of at most two unique distances on the queue at any one time
  - Different anagrams are same in sorted order but an even better way to show similarity is to create a 26 letter array and store counts and hash the tuple.
  - While consiiderig complexity of strings, also take into account their length
  - In complexity, talk about maximum lengths etc for worst case
  - A approach adds heuristics to the standard BFS/Djikstra's to optimize
  - Whenever you do cum_sum, almost always reduce it to a single variable.
  - 2-passes are often manageable in a single pass.
  - When dealing with integer keys, think Arrays first instead of hashmaps
  - With arrays, think about precomputation:
    - Prefix/suffix sum/max/min
    - See if starting from start makes sense or from the end e.g.
      - For cum sum, start
      - If wanna see max to the right >, starting from the end makes more sense
  - For 2D matrix based questions:
    - Sometimes we may need to have a matrix of similar dimensions to store intermediate results
    - See if using input matrix is feasible and allowed
  - **A bipartite graph is an undirected graph whose both vertices of all edges belong to different sets. Or a graph which we can color alternatively with 2 colors.**
    - **Doesn't have to be connected**
    - **Formal definition:**
      - **A bipartite graph, also called a bi-graph, is a set of graph vertices decomposed into two disjoint sets such that no two graph vertices within the same set are adjacent.**
  -  N + N/2 + N/4 + … 1 = 2N
    - Do not confuse this with traditional Binary Search where we do halve the space at every iteration but at every iteration we do O(1) time
  - At each recursive branching of the QuickSort function, we can ignore the partition which does not include the k^{th}k value. This is the basis for the QuickSelect algorithm. An immediate benefit of being able to ignore one of the two resulting partitions at each step is that we no longer need to use recursion to branch the process. We can instead convert the function to a more space-friendly iterative solution that uses only a constant amount of space.
  - Wanna merge something or combine something > Connected Components
  - **Intervals Overlap if: a[0] <= b[1] and b[0] <= a[1]**
  - Whenever calculation required, think about running calculation to optimize
  - ALWAYS think about prefix sums. ALWAYS.
  - Do not jump into dfs backtracking to find something. Think about simpler solutions first.
    - Remember dfs backtracking is just an easy bruteforce method to explore all options that are difficult to find other than dfs backtracking.
  - If n < 0, we can substitute x with 1/x and keep n >= 0
  - If need to track depth, the cur_level/next_level or looping through original size of queueu inside outer loop might be appropriate
  - Insidea loop, should not re-make string every time. use list instead to avoid making it O(n^2)
  - When you think that there is no other freaking way to optimize the solution and you've exhausted throwing all data structures and algorithms:
    - Take a step back and try to take a different perspective to the problem
      - Look at it differently
      - Try to frame it differently
    - Does reversing help?



**Time and Space Complexity Analysis:**
  - Average case analysis makes assumptions about the input that may not be met in certain cases. Therefore, if your input is not random, in the worst case the actual performace of an algorithm may be much slower than the average case.
    - Amortized analysis makes no such assumptions, but it considers the total performance of a sequence of operations instead of just one operation.
    - Dynamic array insertion provides a simple example of amortized analysis. One algorithm is to allocate a fixed size array, and as new elements are inserted, allocate a fixed size array of double the old length when necessary. In the worst case a insertion can require time proportional to the length of the entire list, so in the worst case insertion is an O(n) operation. However, you can guarantee that such a worst case is infrequent, so insertion is an O(1) operation using amortized analysis. Amortized analysis holds no matter what the input is.
    - Example:
      - When analyzing amortized time complexities, I find it easiest to reason that each node gets pushed and popped exactly once in next() when iterating over all N nodes.
That comes out to 2N * O(1) over N calls to next(), making it O(1) on average, or O(1) amortized.


  - When things are constant, the big O is constant e.g. if we know properties of an object are 4, then looping over its properties will not be O(p) but O(1)
  - Always drop constants O(n)
  - With two lists, with binary search, the time complexity becomes L1log(L2) instead of L1 + L2. Let's say, L2 is few orders of magnitude bigger than L1, like L1=5 and L2 = 1024. L1log(L2) = 5log(1024) = 50, whereas L1 + L2 = 5 + 1024 = 1029, so it does make a difference.
    - If L1 and L2 sizes are different, then L1logL2 is less than L1 + L2
      - If A = B = 6:
        - A + B = 12
        - In base 2, 6 log 6 = 6  2.58 > 12
      - If A = B = 1024:
        - A + B = 2048
        - A log B = 1024  10 = 10,024
      - If A = 5, B = 1024:
        - A + B = 1029
        - A log B = 5 10 = 5
  - Keep it simple.
  - Quote the space complexity as well. Remember recursive calls means more space
  - If a problem involves multiple queries, just quote for a single query/iteration
  - Keep variables as separate as possible
    - At the end, may simplify by combining them (approximating them for worst case)
    - For example, keep edges E and vertices V separate

|
 | Graph (Time – Space) | Tree (Time – Space) |
 |
| --- | --- | --- | --- |
| DFS | O(V + E) explore all vertices and edges – O(V) Need to maintain visited set | O(V) Edges become redundant in a tree – O(V) O(h) but for a skewed tree, will end up holding all the nodes on stack. **O(branching^m) where m is max depth is another notation for time - O(bm) since gotta store all siblings along the max path**. |
 |
| BFS | O(V + E) explore all vertices and edges – O(V) hold all vertices in the queue | O(V) Edges become redundant in a tree – O(V) skewed is best case as only one node per level but for a balanced, last level will result in n / 2 nodes |
 |
|
 | Both time and space become O(v^2) if adjacency matrix is used instead of adj. list. |
 | **To summarize for trees where height is less than max width, DFS uses less space asymptotically. For trees where max width is less than height BFS uses less space asymptotically.** |
 
**Matrix:**
  - **Number of diagonals in a matrix are (ROWS + COLS - 1)**
  - In matrices, for time complexity, we may not be allowed to go back to the parent cell so branches might actually be branches minus 1.
- For intermediate calculations, create a temporary matrix but it will take more space
- Try to use sentinel values:
  - To assign IDs of components
  - Indicators etc.
    - In matrice traversals, if wanna go to point B from A. It is the same as going to A from B.



    
**Greedy Algorithms:**:
- Greedy problems usually look like Find minimum number of something to do something or Find maximum number of something to fit in some conditions, and typically propose an unsorted input.
- The idea of greedy algorithm is to pick the locally optimal move at each step, that will lead to the globally optimal solution.
- How to prove that your greedy algorithm provides globally optimal solution? Usually you could use the proof by contradiction.
    

**Dynamic Programming**:

Facebook said no need for ML :D

**1D:**
- dynamic programming -> observe if any redundant operations are being peformed.
- think brute force, visualize tree or graph (decision tree can be visualized as options or a binary tree), understand subproblems, think saving results in an array in bottom up approach (memoization is top-down approach but less efficient and easier to come up with). Also, trees or graphs may be difficult so can also think of two parallel timelines (using a max operation). think whether to start from end or start of array. there's one problem for which dp was not done so implemented dfs backtracking coz had to maintain all the combinations.
- think logically. try to fill in a dp matrix or dp array manually, from left to right or right to left. In many cases, it's bottom up.
- Some dp solutions of bottom up approach might be O(n^2) instead of O(n) for example when at every position, we depend on every following position possibly. Think if there's a greedy solution.
- Write a base equation to understand dependency. That helps decide if we wanna go reverse or forward. Usually we define default values of the right-most or left-most. Many times, an additional index is required to hold the base case.
- Depending on equation, it may be possible to store a few variables instead of entire array.
- think dynamically while coming up with logic before coming up with equation
- equtaions are normally adding something or taking max/min of sth.
- Some "DP" problems are actually just window expansion problem that avoid repetitive work
- Some "DP" problems require keeping track of max and min over time.
- DP bruteforce tree may possibly be visualzied in more than one way. For example, instead of "do or not do" branches, can visualize by "which index to start". May be beneficial to directly visualize in array as well.
-  subsequences can be modelled as "starting at index" or "ending at index".
-  Stair base case 1 why?

**2D:**
-  Try bottom-up (from end) and define base case. in 2d, can go left to right and bottom to top.
-  Define appropriate value for out of bound (like 0 of inf)
-  May not need to store entire 2D array. Maybe just selected rows.
-  Default values can be set for entire row or column, etc.
-  Decision Tree with Memoization will mostly be possible. Memoization requires thinking what the function call input (also, the cache key/s) will be. In 2D, there might be two keys.
-  Sometimes I try to visualize by resulting array which is okay for all the possible combinations but for dynamic programming, try to think in terms of iindex i or in 2D, i + j.
-   Most 2D can be done with a table approach. Sometimes visualizing arrays is good enough instead of a tree.
-   Remember to cache the results. Memoization can easily be converted to Bottom-up DP. Core conditions mostly remain the same.
-   Even when defining the DFS conditions and recursive calls, do think about simple equations that would be easily possible in 2D array (like looking at i + 1, j + 2, max/sum, etc) 



**Data Structures Udacity Course:**
    - Linked Lists make inserting and deleting so easy but Arrays are good in terms of having indices.
      - Index vs Reference to the next element
      - In particular, arrays are contiguous memory blocks, so large chunks of them will be loaded into the cache upon first access. This makes it comparatively quick to access future elements of the array. Linked lists on the other hand aren't necessarily in contiguous blocks of memory, and could lead to more cache misses, which increases the time it takes to access them.
      - Typically, when using an array you access items near each other. This is especially true when accessing an array sequentially.
        - When you access memory, chunks of it are cached at various levels. Cache locality refers to the likelihood of successive operations being in the cache and thus being faster. In an array, you maximize the chances of sequential element access being in the cache.
        - With linked lists, by counter-example, there's no guarantee that items that appear sequentially in the list are arranged near eachother in memory. This means fewer cache hits, and degraded performance.
    - Doubly Linked List: reference to previous as well
    - While inserting in linked list, first set the next of the new element. This will reduce 1 additional line of code instead of saving tmp pointer.
    - Recent most important but still wanna keep the rest? Use stacks e.g. News Feed
      - Stack can be implemented with linked lists
      - LIFO
    - Queue: can implement using LL
      - Keep a ref to head and tail so constant time access
      - Deques have dequeuer and enqueuer at both ends
    - Priority Queue: if same priority, oldest removed
    - **BS: for worst case, assume test element to be largest and always favor lower when middle is a tie in case of even numbers
      - Not really significant.**
    - If don't know big 0, create n vs n_iterations table and notice patterns
    - Remember there might be a space vs time trade-off
    - Talk about all possible options in an interview
    - Improved version of bubble sort could stop doing comparisons for the very last elements
    - Average Case:
      - All possible case time (sum) / no. of cases on average
    - Space Complexity: If no extra i.e. in place, O(1) Auxillary
      - Assumes space released after every step so just look at single step
      - In recursion, you'll always be in a single branch of the call tree so calculate space complexity accordingly.
    - Merge sort, the recursive approach is called top-down.
      - Bottom up is iterative and starts from bottom
    - Please no quick sort on nearly sorted arrays if using standard Lomuto parittion scheme
    - Improve quick sort by median
    - Space complexity of Quick Sort can be O(1) if in-place using swaps
      - But the recursion stack will be used still
    - Hash functions might be used for optimizing a solution
      - Commonly divide numbers by a number let's say 10
        - mod and use the remainder as the index in an array
      - Why use the last digits? Because they are more random than the significant digits
      - Buckets to resolve collision
        - Still need to iterate through the collection O(n)
      - No perfect way to define a hash function
      - Compromise between hash function size: that spreads out values but doesn't use a lot of space vs one that uses less buckets but might have to do some searching within each bucket
      - Can use another hash function (double hashing)
      - Load Factor = Number of Entries / Number of Buckets
      - We can use our load factor as an indicator for when to rehash—as the load factor approaches 0, the more empty, or sparse, our hash table is.
      - On the flip side, the closer our load factor is to 1 (meaning the number of values equals the number of buckets), the better it would be for us to rehash and add more buckets. Any table with a load value greater than 1 is guaranteed to have collisions.
      - If hash function is simply mod than the divisor is simply the number of buckets
      - Dividing a bunch of multiples of 5 by another multiple of 5 will cause a lot of collisions
      - HashMaps:
        - You can store <k, v> in the bucket determined by hash(k)
        - For string keys, ASCII values to get integer value
        - Just a convention, s[0]31^(n-1) + s[1]31^(n-2) + ….
        - As long as you space, a unique hash key can be very useful for constant lookups
      - Tree is an extension of a linked list essentially (having several next elements)
        - A tree must be completely connected ALWAYS and no cycles
        - Height of leaf is 0 but depth is X (opposite relation)
      - BFS: Can do level Order traversal
      - DFS: Preorder, inorder, post-order
      - Perfect binary trees (all non-leaves have two children)
      - BST: Unbalanced is a problem (the worst case)
      - Heaps don't have to be binary
      - A binary heap must be a complete tree:
        - All levels except the last level must be full
      - Binary Tree: log(n) > Height of the tree
      - If heap implemented through Tree like structure, it will require saving more stuff (left, right, bla bla bla)
        - Commonly implemented with an array
      - The most unbalanced tree is kinda like a linked list
      - Red Back Tree Rules:

1. Each node can be either red or black
2. Each node has null black nodes (if it doesn't have 2 children)
3. If parent is red, both children are black
4. Root is black
5. All paths from root to null nodes have the same number of black nodes
      - Graphs (Networks) to be used for showing connections
        - Trees are actually types of graphs
      - Cycles allowed
      - No roots but we can have a starting point based on the problem
      - DAG: Directed, Acyclic, Graph
      - Connectivity:
        - Disconnected: if we can't reach a vertex or a group of vertices from another
        - Min number of elements to be removed for a graph to become disconnected > shows how strong connection is
        - A weakly connected component is a maximal group of nodes that are mutually reachable by violating the edge directions.
      - Implementation:
        - OOP (Edge, Vertex objects)
        - List of edges
        - Adjacency List
        - Adjacency Matrix
        - If you're looking for node degree or no. of edges for a vertex > Adjacency list
      - DFS: Can be implemented with stack:
        - If not seen, put in stack
        - If hit a seen vertex, go back and try another one
        - Recursion is technically a stack as well
      - BFS: Queue
      - **Eulerian Path:**
        - Passes through every edge at least once( I think its exactly once)
        - Eulerian Cycle:
          - Each edge only once
          - End up at the same node
          - Possible only if all nodes have even degree or even number of edges connected to them.
        - Paths are a bit lenient:
          - Start and end nodes can have odd degree
      - **Hamiltonian Path**
        - Must go through every vertex once
        - Cycle:
          - Start and end at the same vertex
      - If you're storing a disconnected graph, not every node will be tied to an edge, so you should store a list of nodes.
      - We could probably leave it there, but storing an edge list will make our lives much easier when we're trying to print out different types of graph representations.
      - Unfortunately, having both makes insertion a bit complicated
      - Shortest Path:
        - **Unweighted: BFS**
        - **Weighted, Undirected: Dijiktra's (Min Heap Implementation)**
          - **Djiktra's should work for directed as well**
      - Knapsnack: Brute Force is O(2^n)
      - A problem may have both DFS and BFS solution like the count_islands problem
  

**Final Interview Tips**:
  - In my current job, I've successfully done this and that.
    - Guide your interviewer, take the steering wheel
      - Project:
        - Architecture, What did you do?
        - Mistakes, What would you do differently
        - Hardest bugs
        - Challenges (Missing data, limited compute, ambiguity, etc.)
        - Successes
    - Relevant Hobbies
