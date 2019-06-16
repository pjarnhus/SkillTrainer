import os
import io_funcs


def print_status(msg: str):
    os.system('clear')
    print('-'*(6+len(msg)))
    print(f"-  {msg}  -")
    print('-'*(6+len(msg)))
    print()


def input_topic(text:str):
    while True:
        print('-  Press ? to list all topics  -')
        topic_name = input(text)
        if topic_name == '?':
            print('-  Topics available  -')
            print('\n'.join(io_funcs.get_all_topics()))
            print()
            continue
        return topic_name

def add_topic():
    print_status('Add new topic')
    while True:
        topic_name = input_topic('Topic (empty to abort): ')

        if len(topic_name) == 0:
            return "No new topic was added"

        if len(io_funcs.find_topic(topic_name)) > 0:
            print(f"Topic {topic_name} already exists")
        else:
            return io_funcs.create_topic(topic_name)
            break

def add_tag():
    print_status('Add new tag to topic')
    while True:
        topic_name = input_topic('Topic that should be tagged: ')
        topic = io_funcs.find_topic(topic_name)
        if not topic:
            return 'Topic does not exist'
        tag_name = input_topic('Tag name (empty to abort): ')
        if len(tag_name) == 0:
            return 'No tag added'

        tag = io_funcs.find_topic(tag_name)
        if not tag:
            return 'Tag does not exist'
        return io_funcs.create_tag(topic[0], tag[0])

