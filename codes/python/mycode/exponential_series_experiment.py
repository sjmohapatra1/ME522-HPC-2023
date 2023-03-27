#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def exp_series(x, n=100):
    """
    Calculates the exponential of x using the exponential series with n terms.

    Args:
        x (float): The number to calculate the exponential of.
        n (int, optional): The number of terms in the series. Default is 100.

    Returns:
        float: The exponential of x.
        
        
    The algorithm calculates the exponential function using the Taylor series expansion, which is a mathematical formula that expresses a function as an infinite sum of terms. The Taylor series for the exponential function is:

scss
Copy code
e^x = 1 + x + (x^2)/2! + (x^3)/3! + (x^4)/4! + ...
The algorithm approximates the value of e^x by summing the first n terms of the series. The x parameter is the input to the exponential function and n is the number of terms used in the approximation.

The algorithm starts by initializing the value of exp to 1.0 and the value of term to 1.0. Then, it iterates n times, each time updating the value of term to include the next term of the series (i.e., term *= x / i) and adding this new term to the current value of exp. This process continues until all n terms have been added to exp.

Finally, the algorithm checks the convergence of the series by comparing the absolute value of the last term to a small threshold value (1e-15). If the absolute value of the last term is greater than this threshold, it means that the series may not have converged properly and the function prints a warning message.

Overall, the algorithm provides an efficient way to approximate the value of e^x using the Taylor series expansion, and can be useful in situations where calculating the exponential function directly may be computationally expensive or impossible.
    """
    # Initialize variables
    exp = 1.0
    term = 1.0

    # Calculate the series
    for i in range(1, n+1):
        term *= x / i
        exp += term

    # Check convergence
    if abs(term) > 1e-15:
        print("Warning: Series may not have converged.")

    return exp



# In[3]:


# Generate x values
x = np.linspace(0, 100, 1000)


# In[4]:


y_np = np.exp(x)
y_my = np.array([exp_series(xi) for xi in x])


# In[6]:


# Plot the results
plt.plot(x, y_np, label="numpy exp()")
plt.plot(x, y_my, label="exp_series()")
plt.legend()
plt.show()


# In[7]:


get_ipython().run_line_magic('timeit', 'y_np = np.exp(x)')


# In[9]:


get_ipython().run_line_magic('timeit', 'y_my = np.array([exp_series(xi) for xi in x])')
##34.9 ms ± 433 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)


# In[ ]:




