import mysql.connector

def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="antitheft"
    )

def insert_event(
    image_path,
    hash_value,
    tx_hash
):

    conn = get_connection()

    cursor = conn.cursor()

    sql = """
    INSERT INTO events
    (
        image_path,
        hash_value,
        tx_hash,
        timestamp
    )
    VALUES
    (%s,%s,%s,NOW())
    """

    cursor.execute(
        sql,
        (
            image_path,
            hash_value,
            tx_hash
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

def get_events():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM events
        ORDER BY id DESC
        """
    )

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data