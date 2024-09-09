ename=input("Enter the Name: ")
dept=input("Enter the Department: ")
basic=int(input("Entter the basic salary: "))
pf=basic*12//100
da=basic*50//100
ta=basic*5//100
it=basic*3//100


net=(basic+pf+da+ta)-it
print=("pf:",pf)
print=("da:",da)
print=("ta:",ta)
print=("it:",it)
print=("The next month salary is:",net)
