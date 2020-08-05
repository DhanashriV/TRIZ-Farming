from scipy.optimize import linprog
obj = [-18,-67.5,-16.5]

lhs_ineq = [[1.6,8.5,2.5],[1,0,0],[0,1,0],[0,0,1]]  # Coefficient of constraints

rhs_ineq = [70000,16000,4000,5000] #maximum values 

lhs_eq = [[1,1,1]] 
rhs_eq = [24000]
bnd = [(0, float("inf")),(0, float("inf")),(0, float("inf"))]  # Bounds of y
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,method="revised simplex")
print(opt)