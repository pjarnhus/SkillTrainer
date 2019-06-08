"""Overall script for running the solution."""
print('Welcome to the Skill Trainer')
while True:
    print('Please select an option:')
    print('1) Add content to library')
    print('2) Add new topic')
    print('3) Add new tag to topic')
    print('4) Select training content')
    print('x) Exit')
    print('')
    choice = input('Selected option: ')
    if choice.lower() == 'x':
        break

