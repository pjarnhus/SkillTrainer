import db


def find_topic(topic_name: str):
    sql_query = f"select tag_id, tag_name from tag_md where tag_name = '{topic_name}'"
    rows = (db
            .conn
            .cursor()
            .execute(sql_query)
            .fetchall()
           )
    return [r for r in rows]


def get_all_topics():
    sql_query = 'select tag_name from tag_md order by tag_name'
    rows = (db
            .conn
            .cursor()
            .execute(sql_query)
            .fetchall()
           )
    return [r[0] for r in rows]


def get_all_levels():
    sql_query = 'select level_id, level_name from levels'
    rows = (db
            .conn
            .cursor()
            .execute(sql_query)
            .fetchall()
           )
    return rows


def create_topic(topic_name: str):
    sql_query = f"insert into tag_md(tag_name) values ('{topic_name}')"
    cur = db.conn.cursor()
    cur.execute(sql_query)
    db.conn.commit()
    return f"Created topic: {topic_name}"


def create_tag(topic, tag):
    sql_test_exists = (f"select * from tags where child_id = {topic[0]}"
                       + f" and parent_id = {tag[0]}")
    rows = (db
            .conn
            .cursor()
            .execute(sql_test_exists)
            .fetchall()
           )
    if rows:
        return f'{topic[1]} is already tagged with {tag[1]}'

    sql_create_tag = (f"insert into tags(child_id, parent_id)"
                      + f" values ({topic[0]}, {tag[0]})")
    cur = db.conn.cursor()
    cur.execute(sql_create_tag)
    db.conn.commit()
    return f'{topic[1]} tagged under {tag[1]}'


def create_item(title,
                reference,
                topic = None,
                low_level = None,
                high_level = None):
    if topic:
        sql_query = ('insert into library(title, reference,'
                     + ' tag_id, level_low, level_high)'
                     + ' values('
                     + f"'{title}', '{reference}', {topic[0][0]},"
                     + f" {low_level}, {high_level})"
                    )
        return_string = f'{title} was inserted under {topic[0][1]}'
    else:
        sql_query = ('insert into library(title, reference)'
                     + f"values ('{title}', '{reference}')"
                    )
        return_string = f'{title} was inserted in To Read'
    cur = db.conn.cursor()
    cur.execute(sql_query)
    db.conn.commit()
    return return_string


def get_to_read(n_items: int = 1):
    sql_query = ('select item_id, title, reference from library'
                 + ' where tag_id is null'
                 + f' order by random() limit {n_items}')

    rows = (db
            .conn
            .cursor()
            .execute(sql_query)
            .fetchall()
           )
    return list(rows)


def update_item(item_id, **update_fields):
    update_string = ', '.join([str(k)
                               + '='
                               + ("'" + str(v) + "'" if isinstance(v, str)
                                  else str(v))
                               for k, v in update_fields.items()])
    sql_query = ('update library set '
                 + update_string
                 + f' where item_id = {item_id}')
    cur = db.conn.cursor()
    cur.execute(sql_query)
    db.conn.commit()
    return 'Updated something'
