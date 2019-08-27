# Data-Structures 
Small programs implementing various data structures, in python 3 for the moment but may expand.

Circular Queue  
A simple implementation following pseudocode I read whilst revising A' level computer science before the start of my degree.
Unfortunately, certain aspects of the queue (e.g size) are hard-coded. Future Jasper, please do fix this.  
Includes a rudimentary interface to print the queue's state on the commandline.
  
Dijkstra implementation  
An implementation of Dijkstra's shortest path algorithm that I wrote when revising A' level computer science before my degree.  
An example adjacency list and start/end nodes are provided, but the algorithm should work for any.  
  
Binary Tree  
A recursive binary tree implementation whipped up during the introductory python lectures in the first year of my degree.
Thankfully, I was already knowledgable with python, so I wrote this for fun whilst the lectures went through if statements....  
You'll notice comments that I have left challenging my coursemates to make a method to print out the tree.  
  
Hash Table  
A simple hashing algorithm that uses string folding to generate keys, and linear probing to handle collisions.  
This algorithm is generalised, but an example case is provided demonstrating deterministic hashing and collisions handling.  
  
Merge Sort  
Simple implementation of this standard log-linear sorting algorithm. See the end of the file for example cases, including a random list generator.  
  
Snake  
An early demo showing snake running on pygame. Pygame is a third party that is required to be installed in order to run this program.  
This game was written during my A' level computer science course, for the purpose of python and pygame training. The debug  
messages visibile in the console relate to a countdown before the next "superfood" appears. This features is not functional.  
  
Magic Square  
A magic square is an n by n grid containing all numbers 1 through n*n and no duplicates, where all rows, columns,  
and diagonals individually add up to the same figure. This is an algorithm to solve a magic square of any ODD size.  
Feel free to try with different sizes, it should work up to the limits of... well, your memory capacity.  
  
Number Base Converter  
Provide this program with any number, its base (currently up to 36, using 0-9 and A-Z as symbols), and a target base,  
and the program will convert it for you using base 10 as an intermediary. I believe i even added base one support.  
In the future, I'd like to add support for custom symbol sets.
