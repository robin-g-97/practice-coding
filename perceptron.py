# -*- coding: utf-8 -*-
import matplotlib.pyplot as pt
import random as rnd
import numpy as np

t = 2
w1 = rnd.random()
w2 = rnd.random()
x = np.array(range(20))

def myformat(x):
    return ('%.2f' % x).rstrip('0').rstrip('.')
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
def learningrulex(U, D, w1, xin):
    w1 = w1 + (D-U)*xin
    return w1

def learningruley(U, D, w2, yin):
    w2 = w2 + (D-U)*yin
    return w2

def correctconditions(inputvar, selection):
    # and gate
    if selection == 1:
        if inputvar[0] == 1 and inputvar[1] == 1:
            return 1
        else:
            return 0
    #or gate
    if selection == 2:
        if inputvar[0] == 1 or inputvar[1] == 1:
            return 1
        else:
            return 0
    #NOR gate
    if selection == 3:
        if inputvar[0] == 0 and inputvar[1] == 0:
            return 1
        else:
            return 0
        
        
if __name__ == "__main__":
    print('what kind of gate would you like? Type 0 for an AND gate, or 1 for an OR gate')
    selected = int(input()) + 1
    if selected == 2:
        gatetype = 'OR'
    if selected == 1:
        gatetype = 'AND'
    print('Do you want to save the files? Y/N')
    save = input()
    perceptron = -(w1/w2) * x + (t / w2)
    pt.plot(x,perceptron)
    pt.xlim(0, 1)
    pt.ylim(0, 1)
    print('perceptron = {}/{}*x + {}/{}'.format(w1, w1, t, w2))
    pt.show()
    iteration = 0
    for i in range(20):
        coord = (int(2*rnd.random()),int(2*rnd.random()))
        correct = correctconditions(coord, selected)
        
        if w1*coord[0] + w2*coord[1] > t:
            guess = 1
        else:
            guess = 0
         
        print('The coordinate is {}, which is  {}. The perceptron guessed {}.'.format(coord, correct, guess))
        if guess != correct:
            w1 = learningrulex(guess,correct, w1, coord[0])
            w2 = learningruley(guess,correct, w2, coord[1])
            print('WRONG!')
        perceptron = -(w1/w2) * x + (t / w2)
        pt.plot(x,perceptron)
        showinputspace()
        print('perceptron = -{}/{}*x + {}/{}'.format(w1, w2, t, w2))
        iteration += 1
        if save == 'Y':
            pt.savefig('{}{}'.format(gatetype, iteration))
        pt.show()
