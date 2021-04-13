# TSP-Simulated-Annealing-SA-Python

Using Simulated Annealing(SA) 

## Parameters

Initial Temperature: 100

Ending Temperature: 1e-4

Annealing Factor: 0.99

Number of Iterative: 1000


## 1. Run the program ：
	python3 hw3.py

## 2. Two files will be generated：
 	a. draw.txt —> x and y cooridinates
	b. output.txt —>include path, total path distance and execution time

## 3. gunplot mode
	gnuplot

## 4. Draw path：
	load “draw.plt”
After load “draw.plt”, it will generate output.svg-->picture of the path. You can use Chrome or Safari to oppen it.

![image](https://github.com/tommy3713/tommy/blob/main/example.png)

## 6. Result：
Optimal Visit Order: 

1  32  11  5  33  45  15  44  37  17  4  18  14  6  23  48  27  46  38  9  49  10  39  30  34  21  50  16  2  29  20  35  36  3  22  28  31  8  26  7  43  24  25  13  41  40  19  42  47  12  51  1  

Optimal Distance：  488.61846060861626

Execution Time:  157.6130816936493  (s)
