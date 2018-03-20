# coding = utf-8
# @modified: 2018-3-20 22:40:05
# @author: Jakie Peng
# @description: a script to auto generate a text content for github markdown
#          content
# +-------------------------+
# | [headings](#headings)   |
# +-------------------------+
# | [headings2](#headings2) |
# +-------------------------+
#

# import textwrap
import re
import unicodedata  # to calculate the width of the chars
from typing import List

# patterns to parse the titles writes in MD
def parse_markdown(markdown_string) -> List[str]:
    pattern = re.compile("(\#+\s.+\n)")
    pattern2 = re.compile("(\#\s.+)")  # 如果没有换行符使用这个进行匹配
    if "\n" not in markdown_string:
        temp = re.findall(pattern2, markdown_string)
    else:
        # format it normally 
        temp = re.findall(pattern, markdown_string)
    return temp

# generate a table-like string above
class Table():
    def __init__(self, width:int):
        self.width = width
    
    def _calculate_width(self, x:str) -> int:
        # calculate the width of the string converyed in
        # this table is from [urwid](http://excess.org/urwid/)
#        widths = [(126, 1), (159, 0), (687, 1), (710, 0), (711, 1), 
#                  (727, 0), (733, 1), (879, 0), (1154, 1), (1161, 0), 
#                  (4347, 1), (4447, 2), (7467, 1), (7521, 0), (8369, 1), 
#                  (8426, 0), (9000, 1), (9002, 2), (11021, 1), (12350, 2), 
#                  (12351, 1), (12438, 2), (12442, 0), (19893, 2), (19967, 1),
#                  (55203, 2), (63743, 1), (64106, 2), (65039, 1), (65059, 0),
#                  (65131, 2), (65279, 1), (65376, 2), (65500, 1), (65510, 2),
#                  (120831, 1), (262141, 2), (1114109, 1)]
        def get_single_with(base) -> int:
            if unicodedata.east_asian_width(u"%s"%base) in ("F", "W"):
                return 2
            else:
                return 1
            
        total = sum(list(map(lambda j: get_single_with(j), [i for i in x])))
        return total
        
    def _generate_horizental_line(self, width:int=0) -> str:
        # width here is semi-operator
        if width == 0:
            width = self.width
        bridge = ["-" for i in range(width)]
        return "+" + "".join(bridge) + "+"
    
    def row(self, data: str, indent=0, first=False, noNewline=True) -> str:
        # default the len(data) < self.width
        if noNewline:
            # replace newline operator to none
            data = data.replace("\n", "")
        temp = ""
        if first:
            # headers
            temp = self._generate_horizental_line() + "\n"
            
        temp += "|" + \
        "".join([" "] for j in range(indent)) + \
        data + \
        "".join([" " for i in range(self.width - self._calculate_width(data))]) + \
        "|\n"
        # 这里的长度计算似乎出了点问题，比原来计划的长1
        temp += self._generate_horizental_line() + "\n"
        return temp
    
    def colunm(self):
        pass
    
    def generate(self, data:List[str]) -> str:
        # generate the finally result
        last = "" + self.row(data[0], first=True)
        for i in range(1, len(data)):
            last += self.row(data[i])
        return last
    

class MarkdownTable(Table):
    # speciliaze in Markdown table make
    def __init__(self, width):
        super().__init__(width)
    
    # override the row func
    # cause we can't calculate the length of chars using to build the url
    def row(self, data: List[str], indent=0, first=False, noNewline=True) -> str:
        # default the len(data) < self.width
        # List(str1, str2)
        # str1 is the original str: as Title
        # str2 is the proceesed str: as [Title](#title)
        data_length, data = data
        if noNewline:
            # replace newline operator to none
            data = data.replace("\n", "")
            data_length = data_length.replace("\n", "")
#            print(data_length)
        temp = ""
        if first:
            # headers
            temp = self._generate_horizental_line() + "  \n"
            
#        print("%s---%s"%(self.width,self._calculate_width(data_length)))
        temp += "|" + \
        "".join("&nbsp;" for j in range(indent)) + \
        data + \
        "".join("&nbsp;" for i in range(self.width - self._calculate_width(data_length) - indent)) + \
        "|  \n"
        # 这里的长度计算似乎出了点问题，比原来计划的长1
        temp += self._generate_horizental_line() + "  \n"
        return temp
    
    def _countSharp(self, x: str) -> int:
        # count the number of # in x
        total = len(x.split(" ")[0])
        return total
    
    def processToMarkdownUrl(self, x: str) -> List[str]:
        # process the string to markdown-like url
        pattern = re.compile("#+\s")
        x = re.sub(pattern, "", x)
        processed = "[" + x + "]" + \
        "(#" + x.replace(" ", "-") + ")"
        count = self._countSharp(x)
        return [x, processed, count]
    
    # override the generate func
    def generate(self, data:List[str]) -> str:
        # generate the finally result
        # data = [x, processed, count]
        data = [self.processToMarkdownUrl(i) for i in data]
        print(data[0][0:1])
        last = "" + self.row(data[0][0: 2], indent=data[0][2],first=True)
        for i in range(1, len(data)):
            last += self.row(data[i][0: 2], indent=data[i][2])
        return last
    
        
    
b = """
# R Tutorial

1. [Introduction and preliminaries](https://github.com/poetlife/JUFE-demos/blob/master/R/README.md#simple-manipulations-numbers-and-vectors)
2. [Simple manipulations; numbers and vectors](#simple-manipulations-numbers-and-vectors)
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
"""
a = MarkdownTable(80)
c = a.generate(parse_markdown(b))
d = c.replace("+", "\+")
print(d)