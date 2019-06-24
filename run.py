#!/home/phigit/anaconda3/bin/python

"""Overall script for running the solution."""
import os
import ui

ui.print_status('Welcome to the Skill Trainer')
while True:
    print('Please select an option:')
    print('1) Add content to library')
    print('2) Add new topic')
    print('3) Add new tag to topic')
    print('4) Select training content')
    print('5) Pick item from To Read')
    print('x) Exit')
    print('')
    choice = input('Selected option: ')

    if choice.lower() == 'x':
        break

    elif choice.lower() == '1':
        ui.print_status(ui.add_item())

    elif choice.lower() == '2':
        ui.print_status(ui.add_topic())

    elif choice.lower() == '3':
        ui.print_status(ui.add_tag())

    elif choice.lower() == '5':
        ui.print_status(ui.to_read_item())
