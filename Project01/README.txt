Intro to Project01

The main function is in the file 'FirsProj_DynamicSystem.py'. 
- You can choose the number of bursts K and sample size m on line 80 and 81. 
- You can set the values for parameters of Lorenz system sigma, rho, beta on the lines 75,76,77. 
- You can use the function 'checkDer()' to compare the calculated derivative (by x(t)'=(x(t)-x(t-1))/(t-(t-1))) and theoretical derivative (plug in the x values into the Lorenz system and get derivatives directly). It will show the error matrix to measure the accuracy of derivative matrix V. More detail can be found on line 45 and file 'check.py'.
- You can generate bursts by using function 'burst()', input parameters sigma, rho, beta, K and m.
- You can obtain the matrix A (a K*m by 10 dictionary matrix) and matrix V (a K*m by 3 derivative matrix) by using function 'constructMatrixA()' and 'constructMatrixB()'. More detail can be found in the file 'Experiment.py'.
- You can obtain the coefficient matrix C by using function 'optMatrix()'. It uses the python package 'cvxpy' to do the L1 optimization. It minimizes the L1 norm of matrix C under the constraint 'AC = V'. More detail can be found in the file 'Optimization.py'.
- According to Lorenz equations system, C should be a 10 by 3 matrix looks like
0	0	0
-sigma	rho	0
sigma	-1	0
0	0	beta
0	0	0
0	0	1
0	-1	0
0	0	0
0	0	0
0	0	0

Note: The initialization of measurements are uniformly picked from -1 to 1 with precision 100.