# data-structures
Data Structures and Algorithms

-	Data Structures
o	Hash Tables
o	Linked Lists
o	Stacks
o	Queues
o	Trees
	Binary Tree
o	Tries
o	Graphs
o	Vectors
o	Heaps
o	Tree Algos:
	Binary Search
	Breadth-First
	Depth-First
o	Sorting
	Quick Sort 
	Merge Sort
	Quick Select Algorithm


-	Concepts
o	Integer Divison
o	Divide and Conquer
	Merge Sort
o	Recursion vs Iteration
o	Graph Theory
o	Tree Traversal
o	Combinatorial Problems
o	Flyod’s algorithm to detect cycles in linked lists (the rabbit turtle thing). If there’s a cycle, the rabbit and turtle will meet at some point other than starting point.
o	Abstract (lists, stacks) vs Concrete data types (linked lists, heap)
o	DP/memorization (Facebook said no need for ML) :D
o	Prefix Sum (I guess cumulative sums)
o	Might vary by implementation so talk about approximations
o	When things are constant, the big O is constant e.g. if we know properties of an object are 4, then looping over its properties will not be O(p) but O(1)

-	Big O things:
o	Keep it simple. 
o	Quote the space complexity as well. Remember recursive calls means more space
o	If a problem involves multiple queries, just quote for a single query/iteration
o	Keep variables as separate as possible
	At the end, may simplify by combining them (approximating them)
	For example, keep edges E and vertices V separate

Programming
-	Asking clarifying questions
o	Input Null
o	Input data types
-	Confirm solution verbally and then start coding after confirmation
-	Discuss time and space complexity
-	Practice more problem types than a lot of one type
-	15 minutes, medium and hard leetcode
-	Technical Tips
o	Revise highlights of the Cracking the coding Interview book
o	Can use depth-first or breadth first to traverse a tree
o	Depth first is recursive to write a function that takes depth itself as input
o	Design a basic class for example, a Node Class with value, right child and left child in a binary tree
o	Think about running sums
o	Python functions argguments passed by reference
o	Maximize use of hash
o	Instead of maintaining a list, try to see if you can store running/sum and number of items in a tuple
o	When n^2 to get combinations look the first solution, see if dict can be used for linear type
o	If implementing an equation, see if problem can be simplified using equation manipulation
o	Substring is contiguous, subsequence is contiguous, combinations is not and its completely differnet
o	Look at constraints and handle all base cases
o	When encounter a situation where you have to traverse something till end, use stack
o	Recursion quite often makes tree methods quite simple
o	A class can have an object of its own class
o	When you get an indication that we need to perform addition stuff based on how much travel, this indicates a simple recursive solution
o	Try to see problems as sub-problems instead of complicated logics
o	When to use recursion and when not to?
o	If it is known that answer lies nearby the source node in graph, or to get optimal answer, BFS should be used.
	BFS is ideal when we wanna find optimal path to take. We can make branches that can represent “next potential steps” and all of them would have the same cost as they all are siblings. In other words, we can label each solution and keep the label in the BFS’s queue.
o	DFS if answer lies quite far away or if backtracking is needed or if entire graph has to be traversed.
	Cycle detection in a graph
	Solving a maze because in DFS you explore every possible path before backtracking.
	Checking if a graph is bipartite or not
	Finding out strongly connected components of a graph.
	Longest path between two nodes in a graph etc.
o	Lists / Arrays:
	See if sorting helps reduce runtime prior to logic
	Are there any cycles involved? Visualizing a complex problem and simplify for a simple yet elegant solution.
	Often list problems involve sorting, reversal, math (equation manipulation)
o	Instead of repeatedly subtracting, take mod 
o	Corner Cases: negative, null, repeated/duplicates, non-continuous, too big, too homogeneous
o	VISUALIZE. VISUALIZE. VISUALIZE. A simple solution can always come up after visualizing the problem.
o	Strings:
	Two pointers (Expand and Contract)
o	Many times keeping counts in dictionary will help
o	Why maintain two lists when you can maintain a list of tuples (with corresponding elements) for association
o	Minor: use _ for variables that are not required, such as loop iterator to pretend you’re a pro-grammer.
o	Feel like popping multiple items from the queue just because its FIFO? Why not just slice and dice
o	Applications of algorithms like binary search don’t have to be EXACT. Sometimes minor modifications might be required to get the correct answer such as modified/adding a new base case, modifying how points ideally move etc.
	There can be ways that you first apply the general algorithm and then do some corrections to match the problem statement
o	For recursive calls, if we are “searching” something, we just need to do “return recursive calls” until we reach a base case and it returns 1.
	There are cases where we are trying to backtrack essentially from the last failure with the help of a for loop to explore other “solutions” (similar to a graph structure / DFS for example). To “catch” a “failed attempt” and to continue exploring other options, catch the “return False” using an if condition and return True inside the if condition.
o	For recursive calls, remember to explore the option of “sending” original arrays, original pointers or pointers with “original reference” while making recursive calls. E.g. binary search.
o	Equation involved? HAVE to do some manipulation like log/anti-log and stuff.
o	Would’ve been nicer if an upper bound was given so a search could be performed optimally? Try to estimate the upper bound using given info.
o	If a slightly complicated operation is actually a sub-problem that will repeat more than once, remember to implement a separate function for it.
o	Pointers suck. Might just use stack for reversing linked lists.
o	Often with lists, when we wanna find something that satisfies a certain condition, sorting will often make this simple. Also see whether starting index from beginning of the array has more chances to “detect something” or if you start from the last in reverse.
o	Don’t try to apply algos right away. There could be simple array swapping/other operations that can be used for a simpler solution.
o	All immutables like tuples are hashable. So can use them as dict keys. Sometimes, you might wanna convert list elements to a  joint string for hashing.
o	Using dict if you wanna get unique keys is okay but no need to write extra code for incrementing counts if you don’t need counts
o	Can two problems have the same solution? For example, # of visible nodes from left-side is the same as returning height of the tree.
o	Safe to assume that a binary search tree is balanaced or not? Is it a binary search tree or just a binary tree?
o	Read the question properly. Does it have anything that tells you to reuse past information?
o	 When you need ALL the recursive calls to maintain/update something, just keep it outside the function (global variables).
o	Dictionaries and lists are mutable objects which also imply that if they are defined outside “ANY” function, they can still be modified by function f or any inside f -> f(g(h(…))) so no real need to pass by reference.
o	Mutable objects have a tricky copy mechanism (a = [2], b = a, b[0] = 1 -> a = 1)
o	All About Sorting:
	Insertion would work best if an array is already sorted / small array
•	I guess because it will quickly break the for loops
	Bucket sort needs to have distributed data to be useful, otherwise, it’s just a waste of time to achieve the same thing with extra steps.
•	More memory
•	Good for parallel
	Counting sort won’t make sense when n <<<< range
	Quick Sort requires less space than merge sort since there is no merging. Worst case is O(n^2) but randomizing pivot leads to O(nlogn)
o	Sometimes it’s just easier separating two functions, one for calling and one for recursion
o	Adjacency matrix MAY sometimes be helpful than adjacency list (0 indicates self or disconnected).
	Mayube tree tuple of edge as a key if nothing works
o	Instead of deleting from heap, might just be better off not considering it when its time comes during popping.
o	Defining graph: If you need unique edges, defining a graph using a dict (adjacency list) will cause additional overhead.
	Better to create a class with add_edge method.
	Choose format according to the problem. Do you even need a dictionary mapping or just a list of edges will work?
o	Hashing: h(large_value) = large_value % size_of_hash
o	Data Structures Udacity Course:
	Python list is more than just a list
	Linked Lists make inserting and deleting so easy but Arrays are good in terms of having indices.
•	Index vs Reference to next element
•	Doubly Linked List: reference to previous as well
	While inserting in linked list, first set the next of the new element. This will reduce 1 additional line of code instead of saving tmp pointer.
	Recent most important but still wanna keep the rest? Use stacks e.g. News Feed
	Stack can be implemented with linked lists
	LIFO
	Queue: can implement using LL
•	Keep a ref to head and tail so constant time access
	Deques have dequeuer and enqueuer at both ends
	Priority Queue: if same priority, oldest removed
	BS: for worst case, assume test element to be largest and always favor lower when middle is a tie in case of even numbers
	If don’t know big 0, create n vs n_iterations table and notice patterns
	Remember there might be a space vs time trade-off 
	Talk about all possible options in an interview
	Improved version of bubble sort could stop doing comparisons for the very last elements
	Average Case:
•	All possible case time (sum) / no. of cases “on average”
	Space Complexity: If no extra i.e. in place, O(1) “Auxillary”
•	Assumes space released after every step so just look at single step
•	In recursion, you’ll always be in a single branch of the call tree so calculate space complexity accordingly.
	Merge sort, the recursive approach is called top-down.
•	Bottom down is iterative and starts from bottom
	Please no quick sort on nearly sorted arrays
	Improve quick sort by median
	Space complexity of Quick Sort can be O(1) if in-place using swaps
	Hash functions might be used for optimizing a solution
•	Commonly divide numbers by a number let’s say 10
o	mod and use remainder as the index in an array
•	Why used the last digits? Because they are more random than the significant digits
•	“Buckets” to resolve collision
o	Still need to iterate through the collection O(n)
•	No perfect way to define a hash function
•	Compromise between hash function size: that spreads out values but doesn’t use a lot of space vs one that uses less buckets but might have to do some searching within each bucket
•	Can use another hash function (double hashing)
•	Load Factor = Number of Entries / Number of Buckets
•	We can use our load factor as an indicator for when to rehash—as the load factor approaches 0, the more empty, or sparse, our hash table is.
•	On the flip side, the closer our load factor is to 1 (meaning the number of values equals the number of buckets), the better it would be for us to rehash and add more buckets. Any table with a load value greater than 1 is guaranteed to have collisions.
•	If hash function is simply mod than the divisor is simply the number of buckets
•	Dividing a bunch of multiples of 5 by another multiple of 5 will cause a lot of collisions
•	HashMaps:
o	You can store <k, v> in the bucket determined by hash(k)
•	For string keys, ASCII values to get integer value
•	Just a convention, s[0]*31^(n-1) + s[1]*31^(n-2) + ….
•	As long as you space, a unique hash key can be very useful for constant lookups
•	Tree is an extension of a linked list essentially (having several next elements)
o	A tree must be completely connected ALWAYS
o	No cycle (even ignoring the directions)
o	Height of leaf is 0 but depth is X (opposite relation)
•	BFS: Can do level Order traversal
•	DFS: Preorder, inorder, post-order
•	Perfect binary trees (all non-leaves have two children)
•	BST: Unbalanced is a problem (the worst case)
•	Heaps don’t have to be binary
•	A binary heap must be a complete tree:
o	All levels except the last level must be full
•	Binary Tree: log(n) -> Height of the tree
•	If heap implemented through Tree like structure, it will require saving more stuff (left, right, bla bla bla)
•	The most unbalanced tree is kinda like a linked list
•	Red Back Tree Rules:
1.	Each node can be either red or black
2.	Each node has null black nodes (if it doesn’t have 2 children)
3.	If parent is red, both children are black
4.	Root is black
5.	All paths from root to null nodes have the same number of black nodes

•	Graphs (Networks) to be used for showing connections
o	Trees are actually types of graphs
•	Cycles allowed
•	No roots but we can have a starting point based on the problem
•	DAG: Directed, Acyclic, Graph
•	Connectivity:
o	Disconnected: if we can’t reach a vertex or a group of vertices from another
o	Min number of elements to be removed for a graph to become disconnected -> shows how strong connection is
o	A weakly connected component is a maximal group of nodes that are mutually reachable by violating the edge directions.
•	Implementation:
o	OOP (Edge, Vertex objects)
o	List of edges
o	Adjacency List
o	Adjacency Matrix
o	If you’re looking for node degree or no. of edges for a vertex -> Adjacency list
•	DFS: Can be implemented with stack:
o	If seen, put in stack
o	If hit a seen vertex, go back and try another one
o	Recursion is technically a stack as well
•	BFS: Queue
•	Eulerian Path:
o	Passes through every edge at least one once
o	Eulerian “Cycle”:
	Each edge only once 
	End up at the same node
	Possible only if all nodes have even degree or even number of edges connected to them. 
o	Paths are a bit lenient:
	Start and end nodes can have odd degree
•	Hamiltonian Path
o	Must go through every vertex once
o	Cycle:
	Start and end at the same vertex
•	If you're storing a disconnected graph, not every node will be tied to an edge, so you should store a list of nodes
•	We could probably leave it there, but storing an edge list will make our lives much easier when we're trying to print out different types of graph representations.
•	Unfortunately, having both makes insertion a bit complicated
•	Shortest Path:
o	Unweighted: BFS
o	Weighted, Undirected: Dijiktra’s (Min Heap Implementation)
•	Knapsnack: Brute Force is O(2^n)
•	A problem may have both DFS and BFS solution like the count_islands problem
•	# need a deep copy for 2d lists. can't use slicing or .copy().

-	Clarifications to ask the interviewer / small talk:
o	Is the input sorted?
o	Do I need to implement classes?
o	Subsequence will be contiguous or just a subset?
