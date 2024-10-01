**Calculating Average Runtime Complexity Mathematically for Non-Random Pivot Quicksort**
We must take into account the following in order to calculate the average-case time complexity of quicksort with a non-random pivot (let's say we always select the last element as the pivot):
For an input of size n, let T(n) represent the average number of comparisons.
We make n-1 comparisons at every stage of partitioning.
We partition and then sort the left and right subarrays recursively.
For the typical instance, the recurrence relation is expressed as follows:
For each i between 0 and n-1, T(n) = (n-1) + (1/n) * Σ(T(i) + T(n-1-i)).
Where: (n-1) represents the comparisons in the current partition step (1/n) is the probability of each element being chosen as the pivot Σ(T(i) + T(n-1-i)) represents the sum of all possible recursive calls
Making this equation simpler:
T(n) = (n-1) + (2/n) * Σ T(i) for i = 0 to n-1
This recurrence relation is intricate. We can apply the substitution method to solve it:
Determine the form of the solution: T(n) = a log n + bn
This should be replaced in the recurrence relation.
Determine the constants a and b.
Substitution and algebraic manipulation (which need a number of difficult procedures) lead us to:
T(n) = 2n ln n + O(n)
Natural log to log base 2 conversion:
T(n) = 2n log₂ n + O(n)
Consequently, **O(n log n)**is the average-case time complexity of quicksort with a non-random pivot.