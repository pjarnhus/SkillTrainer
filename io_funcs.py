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
