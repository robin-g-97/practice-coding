# -*- coding: utf-8 -*-
'''
This (inefficient) python script is my attempt at creating a perceptron from scratch
It can learn to function as either an AND or an OR gate.
'''
import matplotlib.pyplot as pt
import random as rnd
import numpy as np

theta = 2
w1 = rnd.random()
w2 = rnd.random()
x = np.array(range(20))

#for printing in the plot
def myformat(x):
    return ('%.2f' % x).rstrip('0').rstrip('.')

#formatting of the plot
def showinputspace():
    pt.plot(0,0,'--bo')
    pt.plot(0,1,'--bo')
    pt.plot(1,0, '--bo')
    pt.plot(1,1, '--bo')
    pt.xlim(0,1)
    pt.ylim(0,1)
    pt.xlabel('x value, either 0 or 1')
    pt.ylabel('y value, either 0 or 1')
    pt.suptitle('This perceptron is an {} gate'.format(gatetype))
    pt.title('the current perceptron is {}*x + {}*y'.format(myformat(w1), myformat(w2)))
    
#these are the learning rules for first w1, secondly w2
def learningrulex(U, D, w1, xin):
    w1 = w1 + (D-U)*xin
    return w1

def learningruley(U, D, w2, yin):
    w2 = w2 + (D-U)*yin
    return w2

#for checking whether the randomly generated input either results in a 0 or 1, depending on the type of gate chosen
def correctconditions(inputvar, selection):
    # and gate
    if selection == 0:
        if inputvar[0] == 1 and inputvar[1] == 1:
            return 1
        else:
            return 0
    #or gate
    if selection == 1:
        if inputvar[0] == 1 or inputvar[1] == 1:
            return 1
        else:
            return 0
        
        
if __name__ == "__main__":
    print('what kind of gate would you like the perceptron to learn? Type 0 for an AND gate, or 1 for an OR gate')
    selected = int(input())
    if selected == 1:
        gatetype = 'OR'
    if selected == 0:
        gatetype = 'AND'
    print('Do you want to save the plots? Y/N \nThese can be used to create a gif of the learning process.')
    save = input()
    perceptron = -(w1/w2) * x + (theta / w2)
    pt.plot(x,perceptron)
    pt.xlim(0, 1)
    pt.ylim(0, 1)
    print('perceptron: theta = {}x + {}*y'.format(myformat(w1), myformat(w2)))
    pt.show()
    iteration = 0
    for i in range(20):
        coord = (int(2*rnd.random()),int(2*rnd.random()))
        correct = correctconditions(coord, selected)
        
        if w1*coord[0] + w2*coord[1] > theta:
            guess = 1
        else:
            guess = 0
         
        print('The coordinate is {}, which is  {}. The perceptron guessed {}.'.format(coord, correct, guess))
        if guess != correct:
            w1 = learningrulex(guess,correct, w1, coord[0])
            w2 = learningruley(guess,correct, w2, coord[1])
            print('WRONG!, the perceptron has learned from this.')
        perceptron = -(w1/w2) * x + (theta / w2)
        pt.plot(x,perceptron)
        showinputspace()
        print('perceptron: theta = {}x + {}*y'.format(myformat(w1), myformat(w2)))
        iteration += 1
        if save == 'Y':
            pt.savefig('{}{}'.format(gatetype, iteration))
        pt.show()
