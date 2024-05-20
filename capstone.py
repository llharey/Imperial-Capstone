import numpy as np
!pip install pyplot
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

x = np.linspace(0, 6000, 1000) # generate 1000 equaly spaced values between 0 and 6000 
y = np.linspace(0, 4000, 1000 ) # generate 1000 equaly spaced values between 0 and 4000

# determine the plot size
plt.figure(figsize= (15, 10))
# Plot the constraint equation
plt.plot(x, 140*(40 - x/200), label="x/200 + y/140 = 40 ---> C1")
# Plot the constraint lines
plt.axvline(x=6000, color='k', linestyle='--', label="x = 6000")
plt.axhline(y=4000, color='brown', linestyle='--', label="y = 4000")
# # limits
plt.title('Graph of Constraints')
plt.xlabel('Type X', fontsize = 20)
plt.ylabel('Type Y', fontsize = 20)
# # legend
plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)

plt.show();
