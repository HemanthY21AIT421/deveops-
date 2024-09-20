emp={'eno':[1,2,3],'ename':['A''B''C'],'esal':[100000,200000]}
print("\n The employee data set is:")
print(emp)
print("---------------------------------")
print("\n The employee name are:",emp['ename'])
print("---------------------------------")
print("\n the employee salaries are:")
print("---------------------------------")
for i in emp['esal']:
    print(i)