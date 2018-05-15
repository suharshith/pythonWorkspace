# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 16:04:12 2017

@author: Suharshith
"""

"""
Plotting
"""
import pylab as plt


mySamples= []
myLinear= []
myQuadratic= []
myCubic= []
myExponential= []

for i in range(0, 30):
    
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
#plt.figure('lin')
#plt.xlabel('sample points')
#plt.ylabel('linear function')
#plt.title('Linear')
#plt.clf()
#plt.plot(mySamples, myLinear)
#plt.figure('quad')
#plt.ylabel('quadratic function')
#plt.xlabel('sample points')
#plt.title('Quadratic')
#plt.clf()
#plt.plot(mySamples, myQuadratic)
#plt.figure('cube')
#plt.xlabel('sample points')
#plt.ylabel('cubic function')
#plt.title('Cubic')
#plt.plot(mySamples, myCubic)
#plt.figure('expo')
#plt.xlabel('sample points')
#plt.ylabel('expo function')
#plt.title('Expo')
#plt.plot(mySamples, myExponential)
   
    """
   Changing axes range 
plt.figure('lin')
plt.clf()
plt.ylim(0,900)
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.ylim(0,900)
plt.plot(mySamples, myQuadratic)
plt.figure('lin')
plt.title('Linear')
plt.figure('quad')
plt.title('Quadratic')

"""
"""
    Using legends and comapring graphs

plt.figure('linquad')
plt.clf()
plt.plot(mySamples, myLinear, label = 'linear')
plt.plot(mySamples, myQuadratic, label = 'quadratic')
plt.legend(loc= 'upper left')
plt.title('Linear vs. Quadratic')
plt.figure('cube exp')
plt.clf()
plt.plot(mySamples, myCubic, label = 'cubic')
plt.plot(mySamples, myExponential, label = 'exponential')
plt.legend()
plt.title('Cubic vs. Exponential')

"""
"""
    Changing Data Display Color, Type, Size
plt.figure('linquad')
plt.clf()
plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
plt.plot(mySamples, myQuadratic,'ro', label = 'quadratic', linewidth = 3.0)
plt.legend(loc= 'upper left')
plt.title('Linear vs. Quadratic')
plt.figure('cube exp')
plt.clf()
plt.plot(mySamples, myCubic, 'g^', label = 'cubic', linewidth = 4.0)
plt.plot(mySamples, myExponential, 'r--',label = 'exponential', linewidth = 5.0)
plt.legend()
plt.title('Cubic vs. Exponential')

"""
"""
    Subplots
plt.figure('linquad')
plt.clf()
plt.subplot(211)
plt.ylim(0,900)
plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth= 2.0)
plt.subplot(212)
plt.ylim(0,900)
plt.plot(mySamples, myQuadratic,'r', label = 'quadratic', linewidth= 3.0)
plt.legend(loc= 'upper left')
plt.title('Linear vs. Quadratic')
plt.figure('cube exp')
plt.clf()
plt.subplot(121)
plt.ylim(0, 140000)
plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth= 4.0)
plt.subplot(122)
plt.ylim(0, 140000)
plt.plot(mySamples, myExponential, 'r',label= 'exponential', linewidth= 5.0)
plt.legend()
plt.title('Cubic vs. Exponential')
"""
    #CHANGING SCALES
plt.figure('cube explog')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth= 2.0)
plt.plot(mySamples, myExponential, 'r',label= 'exponential', linewidth= 4.0)
plt.yscale('log')
plt.legend()
plt.title('Cubic vs. Exponential')
plt.figure('cube explinear')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth= 2.0)
plt.plot(mySamples, myExponential, 'r',label= 'exponential', linewidth= 4.0)
plt.legend()
plt.title('Cubic vs. Exponential')
