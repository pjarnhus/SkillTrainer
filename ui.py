import os
import io_funcs


def print_status(msg: str):
    os.system('clear')
    print('-'*(6+len(msg)))
    print(f"-  {msg}  -")
    print('-'*(6+len(msg)))
    print()


def add_topic():
    os.system('clear')
    print('Add new topic')
    while True:
        topic_name = input('Topic (empty to abort): ')

        if len(topic_name) == 0:
            return "No new topic was added"

        if len(io_funcs.find_topic(topic_name)) > 0:
            print(f"Topic {topic_name} already exists")
        else:
            return io_funcs.create_topic(topic_name)
            break

