# Python program to illustrate 
# Stripplot using inbuilt data-set  
# given in seaborn 
  
# importing the required module 
import matplotlib.pyplot as plt 
import seaborn as sns 
import os
os.environ['QT_QPA_PLATFORM']='offscreen' 
# use to set style of background of plot 
sns.set(style ="whitegrid") 
  
# loading data-set 
iris = sns.load_dataset('iris'); 
  
# plotting strip plot with seaborn 
# deciding the attributes of dataset on which plot should be made 
ax = sns.stripplot(x = 'species', y = 'sepal_length', data = iris); 
  
# giving title to the plot 
plt.title('Graph') 
  
# function to show plot 
plt.show()