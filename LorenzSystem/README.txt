Intro to Project01

The main functions are in the files 'FirsProj_DynamicSystem.py', 'ModifiedProj.py' and 'ModifiedProj2'.

'FirstProj_DynamicSystem':
- You can choose the number of bursts K and sample size m on line 90 and 91. 
- You can set the values for parameters of Lorenz system sigma, rho, beta on the lines 85,86,87. 
- You can use the function 'checkDer()' (on the line 95)to compare the calculated derivative (by x(t)'=(x(t)-x(t-1))/(t-(t-1))) and theoretical derivative (plug in the x values into the Lorenz system and get derivatives directly). It will show the error matrix to measure the accuracy of derivative matrix V. More detail can be found on line 46 and file 'check.py'.
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

'ModifiedProj.py':
- Change 01: The number of initials is fixed to five, instead of picking different initials to get different bursts, we chop the long function up and get K bursts per initial.
- Change 02: New added chopUp function (line 72), which chop the original single burst into K bursts.
- Change 03: You can use function graph1 and graph2 to paint the graphs of bursts before chopped and after chopped.

'ModifiedProj2.py'(Final Version):
- Change 04: The number of initial is limited to only one.
- Change 05: The parameters are assigned to be 10, 28, and 8/3 (see lines 82/83/84) in order to keep the chaotic status.
- Change 06: You can use the graph function from 'Graph.py' to paint the graph of x1x2x3 before and after chopped. Details can be found on line 97 and the file 'Graph.py'.
- Change 07: You can compare the calculated coefficient matrix C1 and actual matrix C2 visionally by using function graphM. Details can be found in the file 'Graph.py'.