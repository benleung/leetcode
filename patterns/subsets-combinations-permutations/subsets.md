# complexity
- Time complexity: O(N*2^N) to generate all subsets and then copy them into output list.
  - think of decision tree, it would be depth of N, with 2^N branches at the end

- Space complexity: O(N*2^N)
  - This is exactly the number of solutions for subsets multiplied by the number NN of elements to keep for each subset.

For a given number, it could be present or absent (i.e. binary choice) in a subset solution. As as result, for NN numbers, we would have in total 2^N2 
N
  choices (solutions).


# knowledge to know
Heap's algorithm can produce all possible permutations of n objects
