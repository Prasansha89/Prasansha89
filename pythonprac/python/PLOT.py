import matplotlib.pyplot as plt
import numpy as np
x=np.array([2012,2013,2014,2015])
y=np.array([12000,16610,8000,20000])
z=np.array([16000,10000,12000,18000])
#For adding marker (marker='o')
#for adding pattern ('o:') and can use --,-etc.
plt.plot(x,y,'o:')
plt.plot(x,z,'*-')
#plt.scatter(x,y)
#for simple text use x.xlabel()
#for customize text fontdict={'family':'type','color':'','size':fontsize}
plt.xlabel("Year")
plt.ylabel("Salaries in rs.")
plt.title('Growth of Employee',fontdict={'family':'serif','color':'violet','size':15})
#for naming two data for same x
plt.legend(['Pawan','Rahul'])
plt.grid()
#plt.bar(x,y)
#plt.pie(x)
plt.show()