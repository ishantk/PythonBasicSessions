import matplotlib.pyplot as plt
from scipy import stats

X = [1,2,3,4,5]
Y = [2,4,5,4,5]

data = stats.linregress(X,Y)
print(data[0]) # b1
print(data[1]) # b0

plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.plot(X, Y, "ro")
plt.show()

"""

DATA
-----


X	Y    X-MX	 Y-MY   sq(X-MX)   (X-MX)(Y-MY)
--------------------------------------------------
1 	2     -2  	  -2		4 		4
2 	4     -1       0		1 		0
3 	5      0  	   1		0 		0
4 	4      1       0		1		0
5	5      2       1		4		2
-------------------------------------------------
							10 		6
						-----------------	
Mean X : 3
Mean Y : 4

To Find Slope of Line 
Y = b0 + b1X

b1 = 6/10 = 0.6

Y = b0 + (0.6)X
4 = b0 + (0.6)(3)
b0 = 2.2

-------------------

Calculate Square Mean Error

X	Y   Y'  	X-MX	 Y-MY   sq(X-MX)   (X-MX)(Y-MY)
--------------------------------------------------
1 	2    2.8	 -2  	  -2		4 		4
2 	4    3.4	 -1        0		1 		0
3 	5    4 	  	  0  	   1		0 		0
4 	4    4.6 	  1        0		1		0
5	5    5.2 	  2        1		4		2
-------------------------------------------------

Y = 2.2 + (0.6)X
Y' is calculated by substituting the original value of X
Y' is predicted Value

Mean X : 3
Mean Y : 4

Y     Y'    Y-MY   sq(Y-MY)  Y'-MY  sq(Y'-MY)
--------------------------------------------------
2    2.8	-2		4        -1.2	  1.44
4    3.4	 0		0		 -.6	   .36
5    4 	  	 1		1 		   0        0
4    4.6 	 0		0		  .6	   .36
5    5.2 	 1		1 		  1.2     1.44
-------------------------------------------------
					6				   3.6
				---------------------------	
				MSE = 3.6/6  =   0.6


"""
