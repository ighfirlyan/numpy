import matplotlib.pyplot as plt
import seaborn as sns

#Distplot stands for distribution plot, 
#it takes as input an array and plots a curve corresponding to the distribution of points in the array.
sns.distplot([0,1,2,3,4,5], hist=False) #menonaktifkan histogram 

#menampilkan plot
plt.show()