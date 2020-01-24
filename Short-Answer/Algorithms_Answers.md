#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) A is O(n). It will grow linearly as your input increases. If you just have one good ol' loop, not nested, it will be O(n).


b) B is O(n log n). The use of a while loop instead of a for loop keeps it out of O(n^c) territory. It's still not great, and it'll slow down a bit as your input gets larger.


c)C is O(n). The fact that the function only calls itself once within itself, rather than multiple times, and that it only does basic multiplication on each repeat, keeps things linear.

## Exercise II

To find f-floor, you are going to do a binary sort, an O(log(n)) function; it's super time- and space-efficient, which will give you plenty of time to drop eggs from the appropriate floors.
#### Part A:
- [ ] Sweet! Your floors are already sorted.
- [ ] Divide the number of floors by two. Grab that middle floor.
- [ ] If f is that middle floor, awesome. Move on to part B.
- [ ] Not floor F? If floor F is above that middle index, find the halfway point between the middle index and the end. If floor F is below the middle index, find the halfway point between the first floor and the middle index.
- [ ] Keep finding your halfway points until, MIRACLE OF MIRACLES, you find Floor F. 
- [ ] Move on to part B as soon as you locate Floor F.

#### Part B:
- [ ] If you are on Floor F or above, DO NOT DROP THOSE EGGS. 
- [ ] If you below Floor F, you can drop eggs to your happy heart's content.

