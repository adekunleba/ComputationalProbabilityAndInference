# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 07:41:01 2017

@author: ADEKUNLE
"""
#This is a good example of coding probability just write the exercice out and
#discuss your answer
#Doing a little bit on alice hunting dragon
X = {1,2,4}
Y = {1, 3}

#Create a tuple of possible combinations
possibilities = [(x, y) for x in X for y in Y]

#For the function f(x, y) = x **2 + y ** 2
sum_value = 0
for k, v in possibilities:
    sum_value += k**2 + v **2

#Get the probatility of each space
#Create a dictionary
#Get the probability of eact entry by summing over 

dictionary = {}

for k, v in possibilities:
    prob_value = (k**2 + v **2)/ sum_value
    dictionary[(k,v)] = prob_value

#probiblity of P(Y < X)
prob_v_less_k = 0
for k, v in dictionary.keys():
    if v < k:
        y_less_k = dictionary[(k,v)]
        prob_v_less_k += y_less_k
        
#probability of P(X < Y)
prob_k_less_v = 0
for k, v in dictionary.keys():
    if k < v:
        k_less_v = dictionary[(k,v)]
        prob_k_less_v += k_less_v
    
#Probability of P(Y = 3)
prob_y_3 = 0

for k, v in dictionary.keys():
    if v == 3:
        v_is_three = dictionary[(k,v)]
        prob_y_3 += v_is_three