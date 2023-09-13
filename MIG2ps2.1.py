import pulp
import time

from pulp import value

start = time.time()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
problem = pulp.LpProblem('0',pulp.LpMaximize)
problem += x1 +x2, "Функция цели"
problem +=5*x1+ 6*x2 == 2, "1"
problem +=11*x1- 14*x2 == 2, "2"
problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Прибыль:")
print (value(problem.objective))
stop = time.time()
print ("Время :")
print(stop - start)




from cvxopt.modeling import variable, op
import time
start = time.time()
x = variable(2, 'x')
z=-(x[0] +1*x[1])#Функция цели
mass1 = (5*x[0] + 6*x[1] == 2) #"1"
mass2 = (11*x[0] -14*x[1] == 2) # "2"
x_non_negative = (x >= 0) #"3"
problem =op(z,[mass1,mass2,x_non_negative])
problem.solve(solver='glpk')
problem.status
print ("Прибыль:")
print(abs(problem.objective.value()[0]))
print ("Результат:")
print(x.value)
stop = time.time()
print ("Время :")
print(stop - start)


from scipy.optimize import linprog
import time
start = time.time()
c = [1,1] #Функция цели
A_ub = [[6,5]] #'1'
b_ub = [2]#'1'
A_eq = [[11,-14]] #'2'
b_eq = [2] #'2'
print (linprog(c, A_ub, b_ub, A_eq, b_eq))
stop = time.time()
print ("Время :")
print(stop - start)



from matplotlib import pyplot as plt
#ploting our canvas
plt.title('График')
plt.xlabel('Значение Х1')
plt.ylabel('Значение X2')
plt.xlim(0,1)
plt.ylim(0,1)

plt.scatter(0.29411765,0.088235294, c= 'blue')
# plt.plot([0,0.088235294],[0.29411765, 0])

plt.show()