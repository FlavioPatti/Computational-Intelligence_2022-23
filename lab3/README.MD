# LAB 3

## Contributors
-  Leonardo Rolandi (301216)
-  Flavio Patti (301104)
-  Giuseppe Pellegrino (303999) 

### Problem
Write agents able to play Nim, with an arbitrary number of rows and an upper bound "k" on the number of objects that can be removed in a turn (a.k.a., subtraction game).
The nim is a math game for two players. You start with a series of piles containing a certain number of elements (the number of piles and the elements of each pile are freely agreed between the players at the beginning of the game). Players take turns removing any number of elements from any pile, from one to all. Whoever removes the last element from the competition field wins. It is not possible to pass (skip the move).

### Task 3.1 - An agent using fixed rules based on nim-sum (i.e., an expert system)
We develop an hardcoded agent function that follows some fixed rules (you can see the code for more details) and use an iterative loop with 2 steps (0 and 1), so the agent can see one step ahead in future re-calling itself, noticing if the propose move can give an advantage to his opponent. The opponent can play in a fixed way using the dump_PCI function or he can play manually by entering moves from the command line.

### Task3.2 - An agent using evolved rules
For this task we used fixed rules again but this time it is the genome that decides which strategy to use based on its alpha and beta parameters.
At each turn we generate new offsprings and return the best genome based on his fitness which in this case is the winrate.

### Task3.3 - An agent using minmax
Given the high amount of computational overhead required in the development of the tree of possible choices of the two challengers, we have implemented the minmax using two types of pruning: the classic alpha-beta pruning seen during the lessons and a further pruning based on the depth of the tree. Below you can find our results.

NB: no results were reported that required a computation time greater than 2 minute.

## Results

|  NUM_SIZE | NUM_MATCHES |   OPPONENT       |  WIN_RATE  |
| --------- | ----------- | --------------   | ---------  |
|    5      |      10     |   pure_random    |     1.0    |
|    5      |      10     |    dump_PCI      |     1.0    |
|    5      |      10     | optimal_strategy |     0.0    |
|    6      |      10     |   pure_random    |     1.0    |
|    6      |      10     |    dump_PCI      |     1.0    |
|    6      |      10     | optimal_strategy |     0.0    |

### Task3.4 - An agent using reinforcement learning
We decided to train the agent through TRAINING_MATCHES = 1000 matches against the optimal_strategy, in order to update the rewards. Subsequently the final agent is tested by playing with different strategies. Below you can find our results.

NB: no results were reported that required a computation time greater than 2 minute.

|  NUM_SIZE | NUM_MATCHES  |   OPPONENT       |  WIN_RATE   |
| --------- | -----------  | --------------   | ---------   |
|    5      |      100     |   pure_random    |     0.93    |
|    5      |      100     |    dump_PCI      |     0.92    |
|    5      |      100     | optimal_strategy |     0.0     |
|    6      |      100     |   pure_random    |     0.87    |
|    6      |      100     |    dump_PCI      |     0.91    |
|    6      |      100     | optimal_strategy |     0.0     |
|    7      |      100     |   pure_random    |     0.9     |
|    7      |      100     |    dump_PCI      |     0.9     |
|    7      |      100     | optimal_strategy |     0.0     |
|    8      |      100     |   pure_random    |     0.78    |
|    8      |      100     |    dump_PCI      |     0.92    |
|    8      |      100     | optimal_strategy |     0.0     |