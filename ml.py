# import matplotlib.pyplot as plt
# import numpy as np
# from scipy import stats as st
# # mean --> avg
# # median --> mid Value
# # mode --> most repeated Value
# salary=[65000,85000,90000,70000,80000,65000]
# print(np.min(salary),"min")
# print(np.median(salary),"median")
# print(st.mode (salary),"mode")
#          # standard devitation
# print(np.std(salary)) 
#         # variance
# print(np.var(salary),"variance")
# data = np.random.randint(0,10,100)
# print(data)
# plt.hist(data)
# plt.show()
# #normal and uniform data distribution
# plt.uniform(data)
# plt.show()



#orediction Regression :- it is a relation between variables or dataset
#y=mx+c 
import matplotlib.pyplot as plt 
age=[20,25,45,30,50,40]
salary=[20000,25000,45000,30000,50000,40000]

#plotting the data
plt.scatter(age,salary)
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age and Salary')
plt.show()