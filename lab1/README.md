# LAB 1

## Contributors
-  Leonardo Rolandi (301216)
-  Flavio Patti (301104)
-  Giuseppe Pellegrino (303999)
-  Davide Aiello (303296) 

## Project
We have used a Dijkstra optimized approach.
Every state is a subset of the indeces of the list of lists ( problem(N) ), to avoid memory overflow.
Every state has a cost, that it is the number of repetitions of the numbers of that subset of lists, divided by the total length of that subset

## Results

| N   | W   | Nodes     |
| --- | --- | --------- |
| 5   | 5   | 3         |
| 10  | 10  | 3         |
| 20  | 23  | 1,350     |
| 50  | 65  | 1,011,738 |

