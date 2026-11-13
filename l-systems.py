from turtle import *
import time
import keyboard
import math

with open('./l_system.txt') as l_sys:
    variables = []
    rules = []
    for line in l_sys:
        line = line.strip('\n').split(' ')
        if line[1] == '=':
            if line[2].isnumeric() == True:
                vars()[line[0]] = int(line[2])
            else:
                try:
                    float(line[2])
                    vars()[line[0]] = float(line[2])
                except:
                    vars()[line[0]] = line[2]
        else:
            variables.append(line[0])
            rules.append(line[2])

saved_position = []
saved_angle = []

tracer(int(speed_tracer))
bgcolor(bg_color)
pencolor(pen_color)

left(90)
penup()
right(0)
goto(x,y)
pendown()

speed(0)

for n in range(len(variables)):
    vars()['rule_'+variables[n]] = rules[n]

formula = list(axiom)
for n in range (times):
    axiom = formula.copy()
    del formula[:]
    for i in axiom:
        try:
            m = list(vars()['rule_'+i])
            for t in m:
                formula.append(t)
        except:
            formula.append(i)

def save():
    saved_position.append(position())
    saved_angle.append(heading())
    return (saved_position, saved_angle)

def recover():
    penup()
    goto(saved_position[len(saved_position)-1])
    del saved_position[len(saved_position)-1]
    setheading(saved_angle[len(saved_angle)-1])
    del saved_angle[len(saved_angle)-1]
    pendown()

def no_trail():
    penup()
    forward(size)
    pendown()

def multiply_length(size):
    size = size*length_scale_factor
    return (size)

def divide_length(size):
    size = size/length_scale_factor
    return (size)

formula = list(formula)

while True:
    if formula:
        if formula[count] == '-': right(int(angle));
        if formula[count] == '+': left(int(angle));
        if formula[count] == '|': left(180);
        if formula[count] == '>': size = multiply_length(size);
        if formula[count] == '<': size = divide_length(size);
        for n in range(len(variables)):
            if formula[count] == variables[n]: forward(size);
        if formula[count] == 'F' and 'F' not in variables: forward(size);
        if formula[count] == 'f': no_trail();
        if formula[count] == '[': saved_position, saved_angle = save();
        if formula[count] == ']': recover();
    if count + 1 >= len(formula): break
    else: count +=1

pressed = False
penup()
while not pressed:
    if keyboard.is_pressed('s'): pressed = True
    forward(10)