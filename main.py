#!/bin/sh

print('Hello world!')

name = input('What is u name, man?')
print(f'Hi, {name}!')

age = input(f'How old are you, {name}?')

if int(age)>18:
    print('You are not allowed to be here')
else:
    print('Welcome')
