'''
Created on Apr 18, 2018

@author: dario
'''

import time


def calcProd():
    # Calculate the product of the first 100,000 numbers
    product = 1
    
    for i in range(1, 100000):
        product = product * i
        
    return product


startTime = time.time()
prod = calcProd()
endTime = time.time()

print('The result is {} digits long.'.format(len(str(prod))))
print('Took {} seconds to calculate.'.format(endTime - startTime))
