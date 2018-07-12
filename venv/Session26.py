"""
K-Means Clustering

Data Set
---------
P	X 	Y
---------
A 	1	1
B	1 	0
C	0	2
D	2	4
E	3	5
---------

Step1
Draw the Points on Graph

Step2
Take any 2 Random Points
eg: A and C as two Random Points, name them C1 and C2
where C1 and C2 are known as Centroids

C1 1,1   (A)
C2 0,2 	 (C)

Step3
Calculate Distance between Points from C1 and C2
Euclidean Distance -> sqRt  sq(y2-y1) + sq(x2-x2)

Eg:

P 	dist from C1 		dist from C2
A   0 					1.4
B 	1 					2.2
C 	1.4 				0
D 	3.2 				2.8
E 	4.5 				4.2

Observation:
A and B have less distance from C1
C, D and E have less distance from C2

Draw the Graph Again and encircle the points in C1 and C2

Step4
Caluclate Mean of Points in C1 and C2

x1+x2+...xn/n , y1+y2+...yn/n

C1 Mean: 1,.5
C2 Mean: 1.7,3.7

Step5
---------
P	X 	Y
---------
A 	1	1
B	1 	0
C	0	2
D	2	4
E	3	5
---------

Recalculate distance from new C1 Mean and C2 Mean for all points
NC1 : 1, .5
NC2 : 1.7,3.7

P 	dist from NC1 		dist from NC2
A   .5					2.7
B 	.5 					3.7
C 	1.8 				2.4
D 	3.6					0.5
E 	4.9					1.9

Observation:
A, B and have less distance from NC1
D and E have less distance from NC2

Draw the Graph Again and encircle the points in NC1 and NC2


Step6
Recalculate the mean of A, B and C name it as NC3
Recalculate the mean of D and E name it as NC3

Calculate Distances
and draw them on graph..


"""