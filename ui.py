import os
import io_funcs
import web


def print_status(msg: str):
    os.system('clear')
    print('-'*(6+len(msg)))
    print(f"-  {msg}  -")
    print('-'*(6+len(msg)))
    print()


def print_levels():
    print('-  Levels  -')
    print('\n'.join([f'{id}) {name}'
                     for id, name in io_funcs.get_all_levels()]))

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


def add_item():
    print_status('Add new item to library')
    url = input('Enter URL of new item (empty to abort): ')
    if url == '':
        return 'No item added'
    web_item = web.WebItem(url)
    suggested_title = web_item.get_title()
    print(f'Suggested title: {suggested_title}')
    use_title = input('Use suggested title [y]/n? ')
    if use_title.lower() == 'y' or use_title == '':
        title = suggested_title
    else:
        title = input('Enter title (empty to abort): ')
    if title == '':
        return 'No item added'
    read_item = input('Have you read the item before y/[n]? ')
    if read_item.lower() == 'n' or read_item == '':
        return io_funcs.create_item(title, url)

    topic_name = input_topic('Which topic should the item be registered under'
                             + ' (empty to abort)? ')
    if len(topic_name) == 0:
        return 'No item added'

    topic = io_funcs.find_topic(topic_name)
    if not topic:
        return 'Topic does not exists'

    print_levels()
    low_level = input('What is the lowest level this item is suited for'
                      + ' (empty to abort)? ')
    if low_level == '':
        return 'No item added'

    high_level = input('What is the highest level this item is suited for'
                       + ' (empty to abort)? ')

    if high_level == '':
        return 'No item added'
    return io_funcs.create_item(title, url, topic, low_level, high_level)
