# R Tutorial

1. Introduction and preliminaries
2. Simple manipulations; numbers and vectors
3. Objects, their modes and attributes
4. Ordered and unordered factors
5. Arrays and matrices
6. Lists and data frames
7. Reading data from files
8. Probability distributions
9. Grouping, loops and conditional execution
10. Writing your own functions
11. Statistical models in R
12.  Graphical procedures
13. Packages
14. OS facilities
15. Appendix A: A sample session
16. Appendix B: Invoking R
17. Appendix C: The command-line editor
18. Appendix D: Function and variable index
19. Appendix E: Concept index
20. Appendix F: References

## Simple manipulations: numbers and vectors
### assign a vector
`c()` function can assign abitrary number of vertor arguments and whose value is a vector got by concatenating its arguments end to end.
using "<-" operator
```
> x <- c(1, 2, 3, 4, 5)
> x
[1] 1 2 3 4 5
```
using "->" operator
```
> c(1, 2, 3, 4, 5) -> x
> x
[1] 1 2 3 4 5
>
```
using `assign()` function
```
> assign("y", c(1, 3, 5, 7, 9))
> y
[1] 1 3 5 7 9
```
### Vector arithmetic
The elementary arithmetic operators are the usual +, -, *, / and ^ for raising to a power.
In addition, all of the common arithmetic functions are available. `log`, `exp`, `sin`, `cos`, `tan`, `sqrt`, and so on, all have theiru usual meaning.  
`range` is a function whose value is a vector of length two, namely c(min(x), max(x)).  
length(x) is the number of elements in x, sum(x) gives the total of the elements of a vector respectively.  
### Generating regular sequences
#### using colon to assign a regular sequence
```
> 1:20
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
```
additionly, the colon operator has high priority within an expression
```
> 2*1:5
[1]  2  4  6  8 10
```
#### using `seq()` function to get a sequence
`seq()` has **five** arguments
1. from
2. to
3. by: steps, default=1
4. length
5. along = vector is normally used as the only argument to create the sequence 1, 2, ... , length(vector) 

using only __two__ arguments
```
> seq(from=1, to=4)
[1] 1 2 3 4
```
using `along` param
```
> v <- c(1, 2, 3)
> seq(along=v)
[1] 1 2 3
> v <- c(4, 5, 6)
> seq(along=v)
[1] 1 2 3
```
#### using `rep()` function to replicate an object in various complicated ways.
```
(v, times=2)
[1] 4 5 6 4 5 6
```
### Logical vectors
`TRUE` means true;
`FALSE` means false;
`NA` means not available  

operator|meanings
-----|-----
==| equality
!=| inequality
\> | more than
\< | less than
& | and
\| | or
!c1 | not c1

### Missing values
In some cases, missing values may be reserved using "NA". In general any operation on an NA becomes an NA.
Another kind of "missing" values which are produced by numerical coputation, the so-called __Not a Number, NaN__
```
> 0/0
[1] NaN
```
judging a NaN or NA
```
> is.na(NA)
[1] TRUE
> is.na(0/0)
[1] TRUE
> is.nan(NA)
[1] FALSE
> is.nan(0/0)
[1] TRUE
```
### Character vectors
The `paste()` function takes an arbitrary number of arguments and concatenates them one by one into character strings.
```
> paste(c("X", "Z"), 1:5, sep="")
[1] "X1" "Z2" "X3" "Z4" "X5"
> paste(c("X", "Z"), 1:5)
[1] "X 1" "Z 2" "X 3" "Z 4" "X 5"
```
### Index vectors; selecting and modifying subsets of a data set
1. A Logical Vector
2. A vector of positive integral quantities
include
3. A vector of negative integral quatities
exclude
4. A vector of character strings
### Other types of objects
1. **array**: multi-dimensional generalizations of vectors
2. **factors**: handle categorical data
3. **list**: a general form of vector in which the various elements need not be of the same type, and are often themselves vectors or lists.
4. **data frame**: matrix-like structures, in which the columns can be of different types.
5. **function**

## Objects, their modes and attributes
### Intrinsic attributes: mode and length
### Changing the length of an object
### Getting and setting attributes
### The class of an object
