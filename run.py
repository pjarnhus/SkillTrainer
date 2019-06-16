"""Overall script for running the solution."""
import os
import ui

print('Welcome to the Skill Trainer')
os.system('clear')
while True:
    print('Please select an option:')
    print('1) Add content to library')
    print('2) Add new topic')
    print('3) Add new tag to topic')
    print('4) Select training content')
    print('x) Exit')
    print('')
    choice = input('Selected option: ')

    os.system('clear')
    if choice.lower() == 'x':
        break

    elif choice.lower() == '2':
        ui.print_status(ui.add_topic())

    elif choice.lower() == '3':
        ui.print_status(ui.add_tag())
