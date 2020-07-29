#### Information
| Ord. | File                                                                                                                                   | Description & Links                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | [Union Find](https://open.kattis.com/problems/unionfind)                                                                               | Implementation of a data structure which tracks a set of elements partitioned into a number of disjoint subsets, also called Union Find. The *union* method is implemented using **union by size** which compares the size of the disjoints sets when union is performed. The *find* part of the data structure uses **path compression** to limit the height of the trees, created by union between elements, to speed up the process of determining wether two elements belong to the same set or not. By the use of path compression we speed up the find part of the algorithm significantly, from O(n) to constant time. [python](https://github.com/fr3632ho/kattis/blob/master/union-find/unionfind.py). |
| 2    | [All Pairs Shortest Path](https://open.kattis.com/problems/allpairspath)                                                               | Given a graph *G(V, E)* determine the shortest path between every pair of vertices present in the graph. Implementation is based on [Floyd-Warshall Algortihm](https://brilliant.org/wiki/floyd-warshall-algorithm) which is similar to that of Bellman-Ford or Dijkstra (which are single source shortest path). [python](https://github.com/fr3632ho/kattis/blob/master/all-pairs-path/all_pairs_path.py), [java](https://github.com/fr3632ho/kattis/blob/master/all-pairs-path/AllPairsPath.java).                                                                                                                                                                                               |
| 3    | [Arithmetic](https://open.kattis.com/problems/arithmetic)                                                                              | Determine the hexadecimal representation of a number when given the octal representation of that number. [python](https://github.com/fr3632ho/kattis/blob/master/arithmetic/arithmetic.py).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 4    | [Almost Perfect](https://open.kattis.com/problems/almostperfect)                                                                       | Builds on the idea of [*perfect numbers*](https://www.wikiwand.com/en/Perfect_number). A perfect number *i* is a number which the sum of its proper divisors add up to the number *i*. [python](https://github.com/fr3632ho/kattis/tree/master/almost-perfect).                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 5    | [List Game](https://open.kattis.com/problems/listgame)                                                                                 | Not much can be said about the problem more than that the solution lies in counting the amount of prime factors the given number as and adding those up. [python](https://github.com/fr3632ho/kattis/blob/master/list-game/list_game.py), [java](https://github.com/fr3632ho/kattis/blob/master/list-game/ListGame.java).                                                                                                                                                                                                                                                                                                                                                                           |
| 6    | [Virtual Friends](https://open.kattis.com/problems/virtualfriends)                                                                     | More use of the Union Find data structure, just a little simpler since the time constraints are not as harsh. Basically a modified version of the problem given above.  [python](https://github.com/fr3632ho/kattis/blob/master/virtual-friends/virtual_friends.py).                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 7    | [10 kinds of people](https://open.kattis.com/problems/10kindsofpeople)                                                                 | Pathfinding problem which can be solved using the union find datastructure.  [python](https://github.com/fr3632ho/kattis/blob/master/10-kinds-of-people/10_kinds_of_people.py).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 8    | [Prime sieve](https://open.kattis.com/problems/primesieve)                                                                             | Three different implementations of [Sieve of Eratosthenes](https://www.wikiwand.com/en/Sieve_of_Eratosthenes) using kattis data structures. One with the naive implementation, one using a segmented sieve and the third in Java using a BitSet. The problem has high demands on memory efficiency as well as speed. [python segmented sieve](https://github.com/fr3632ho/kattis/blob/master/prime-sieve/sieve_two.py), [java BitSet](https://github.com/fr3632ho/kattis/blob/master/prime-sieve/Sieve.java).                                                                                                                                                                                            |
| 9    | [Single Source Shortest Path - Negative](https://open.kattis.com/problems/shortestpath3)                                               | Shortest path problem with negative weights. Focus was on speed and implemented the SPF algorithm. [python](https://github.com/fr3632ho/kattis/blob/master/shortest-path/neg/sss_path_neg.py), [java](https://github.com/fr3632ho/kattis/blob/master/SSS-path/neg/SPFA.java).                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 10   | [Single Source Shortest Path - Non Negative](https://open.kattis.com/problems/shortestpath1)                                           | Implemented using dijkstras algorithm for shortest path. [python](https://github.com/fr3632ho/kattis/blob/master/shortest-path/non-neg/sss_path.py).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 11   | [Single Source Shortest Path - Time Table](https://open.kattis.com/problems/shortestpath2)                                             | Implemented using a modified dijkstra. [python](https://github.com/fr3632ho/kattis/blob/master/shortest-path/time-table/sss_path_table.py).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 12   | [Add 'Em Up!](https://open.kattis.com/problems/addemup)                                                                                | Given a set of cards, choose two that will add up to a certain sum. Trick is that cards are flippable and can then represent a different value. [python](https://github.com/fr3632ho/kattis/blob/master/add-em-up/add_em_up.py).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 13   | [Airconditioned Minions](https://open.kattis.com/problems/airconditioned)                                                              | For every range given as a preference for a minion, determine how many of these preferences you can combine into a larger preference range where the intersection of preference is not equal to the empty set. What is to be determined here is the number of larger sets one would need to cover all the preferences of the minions. [python](https://github.com/fr3632ho/kattis/blob/master/air-conditioned-minions/AC_minions.py).                                                                                                                                                                                                                                                                           |
| 14   | [Dominoes 2](https://open.kattis.com/problems/dominoes2)                                                                               | Count the number of dominoes that would fall over if given dominoe was to be tipped. Solved using a **BFS** to count all reachable nodes. [python](https://github.com/fr3632ho/kattis/blob/master/dominoes-2/dominoes_2.py)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 15   | [Mandlebrot](https://open.kattis.com/problems/mandelbrot)                                                                              | Determine if a number *c* is in the mandelbrot set or not. [python](https://github.com/fr3632ho/kattis/blob/master/mandelbrot/mandelbrot.py).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 16   | [Buying Coke](https://github.com/fr3632ho/kattis/blob/master/buying-coke/buying_coke.py)                                               | Dynamic programming problem. Solved using a 3-dimensional array to store pre-calculated values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
