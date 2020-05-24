# CSE3310-Lessons

A _recursive algorithm_ calls itself with smaller or simpler
input values. All recursive algorithms have a _base case_, 
which receives the simplest input values. Then there is a subprocess
that takes more complex inputs and simplifies them. That simplified
input is then entered into another instance of the same algorithm
, which will then further simplify the inputs until the base case
is achieved.

##example of recursion
```
// check if a value is converted to an int

def chkInt(var):
    try: //Base case
        var = int(var)
        return var
    except TypeERROR: //simplifies input and sends it through
    //function again
        var = input("enter a valid number")
        return chkInt(var)

```

## iteration vs recursion

all iterative algorithms can be written as recursive algorithms
and vice versa. Depending on the function, one algorithm type
will be more easy to program than the other.

In general, iterative algorithms require more lines of code and
more variables. It relies on while and for loops to complete the
process, whereas recursive algorithms do not use as many variables
or loops because return values are re entered into a new instance 
of the same function. Therefore recursion requires more physical
memory than iterative algorithms because each instance of the
recursive function stays in memory until the base case is 
achieved.
 
 Iterative algorithms tend to be faster than exclusivly
 recursive algorithms, however; hybrid algorithms that use both
 are often faster than iterative algorithms.
 
 ## Ex. 1 factorials
 ###calculate 7!

7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 * 1

ASIDE: what is 6!

6! = 6 * 5 * 4 * 3 * 2 * 1 * 1

rewrite 7! as 7 * 6!

going along,

7! = 7 * (6 * (5 * (4 * (3 * (2 * (1 *( (1)))))))

looking at the brackets you see that it gotta finish before
it pumps out an answer. same as recursive algorithms. This means
you either run out of mem or finish the ting at it's base


Generalizing factorials,
we can say that the function to calculate a factorial

f(x) = x * f(x-1)

## Sorting
Recursive sorting uses both recursive and iterative processes.
In general, these hybrid sorts are exponentially faster with longer
lists. They are also a complete mind (lemme drop an f bomb).
They are measured in the logarithmic scale. 

###Merge Sort
Merge Sort follows a divide and conquer method of sorting where
the array is split into it's base length and then rebuilt by
combining progressively larger sorted lists together. The
recursive portion is the splitting of the list and the iterative
processes is the actual merging. 

Often times this function is separated into splitting and merging
functions. 

### 2QuickSorts
Quick sort also followed a divide and conquer method of sorting.
It places an arbitrarily chosen value in it's correct position
in the list by placing all values less than the value to it's left,
while keeping all the values greater than it on it's right.
Effectively, the ```pivot value``` splits the array into two sections.
then the recursive program moves to the left section and repeats.
Then finishes the right sections.

Quick sort is one of the fastest sorting algorithms used today.
*cough* mergeSortSucks *cough*

### HeapSort
Heap sort uses a binary tree organization of an array, to sort
higher values to the top of the tree. The process of moving larger
values higher in a binary tree is called ```heapifying```
(or heapify).

To build a binary tree, each index starting from zero will have
a left child and a right child branch. Hence a binary tree (2branch)
The index values can be calculated from the following.

```
leftChild = 2 * parentIndex + 1
rightChild = 2 * parentIndex + 2


//  sameple tree
li = [5, 17, 13, 11, 1, 7, 3]

                 5[0]
                /    \
             17[1]   13[2]
            /  \      /  \
          11[3] 1[4] 7[5] 3[6]
             
```

##### Heapify
To heapify the binary tree, the value of the parent index
must be higher than the two children values. Therefore, the
proc starts at te bottom of the tree and works its way to the
top. If the parent is smaller than one of the children values,
it will swap with the child with the higher value. As heapifying
moves throughout the tree, the higher values will progressivly 
move to the top which is index 0.

When the heapifying proc reaches the top, the top value swaps
with the lowest value (highest index) and the heapifying proc
begins with one less value in the list.

Like bubbleSort, heapSort sorts from tail to head which is from
the end of the list to the start. 




