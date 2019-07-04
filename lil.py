import numpy as np 
import matplotlib.pyplot as plt 

probability = 0.5
path_length = 1000
num_simulations = 30
t = np.array(range(2,path_length))
boundary = (2*t*np.log(np.log(t)))**(1/2)


# add starting point equals (0,0)
t = np.insert(t, 0, 1)
t = np.insert(t, 0, 0)
boundary = np.insert(boundary, 0, 0)
boundary = np.insert(boundary, 0, 0)

processes = []
for i in range(num_simulations):
    steps = 2*np.random.binomial(1, probability, path_length-1) - 1
    process = np.cumsum(steps)
    # add starting point in 0
    process = np.insert(process, 0, 0)
    processes.append(process)

ax = plt.gca()
# ax.set_aspect(2)
plt.plot(t, boundary, 'b')
plt.plot(t, -boundary, 'b')
for process in processes:
    plt.plot(t, process, linewidth=0.5)
plt.savefig('lil.png')
plt.show()