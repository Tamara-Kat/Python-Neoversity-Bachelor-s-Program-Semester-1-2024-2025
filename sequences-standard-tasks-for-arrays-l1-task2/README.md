# Sequences. Standard tasks for arrays. Task 2 - Level 1

Implement a function `get_pairs(lst: List) -> List[Tuple]` that returns a list of tuples containing pairs of elements. The pairs should be formed as in the example. If there is only one element in the list, return `[]` instead.


__Example:__
```python
>>> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]
>>> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')] 
>>> get_pairs([1])
[]
```

___*Please keep in mind the following___:
 
- _Do not use the "input" function to enter initial parameters for your task solution._  
- _Do not use the "print" function to return results from your task solution. Do not delete code from the template or change predefined - functions._
- _Put your solution in the section marked with the comment "Put your code here." You can still use your own functions and define them outside the predefined function._
