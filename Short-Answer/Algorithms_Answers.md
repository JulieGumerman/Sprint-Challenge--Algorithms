#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)


b)


c)

## Exercise II

To find f-floor, you are going to do a binary sort, an O(log(n)) function; it's super time- and space-efficient, which will give you plenty of time to drop eggs from the appropriate floors.
#### Part A:
[ ] Sweet! Your floors are already sorted.
[ ] Divide the number of floors by two. Grab that middle floor.
[ ] If f is that middle floor, awesome. Move on to part B.
[ ] Not floor F? If floor F is above that middle index, find the halfway point between the middle index and the end. If floor F is below the middle index, find the halfway point between the first floor and the middle index.
[ ] Keep finding your halfway points until, MIRACLE OF MIRACLES, you find Floor F. 
[ ] Move on to part B as soon as you locate Floor F.

#### Part B:
[ ] If you are on Floor F or above, DO NOT DROP THOSE EGGS. 
[ ] If you below Floor F, you can drop eggs to your happy heart's content.

