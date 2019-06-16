import db


def find_topic(topic_name: str):
    sql_query = f"select tag_name from tag_md where tag_name = '{topic_name}'"
    rows = (db
            .conn
            .cursor()
            .execute(sql_query)
           )
    return [r for r in rows]


def create_topic(topic_name: str):
    sql_query = f"insert into tag_md(tag_name) values ('{topic_name}')"
    cur = db.conn.cursor()
    cur.execute(sql_query)
    db.conn.commit()
    return f"Created topic: {topic_name}"
