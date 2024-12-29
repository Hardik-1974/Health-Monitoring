import utils.connection as connection

def execute_query(query):
    # get connection
    conn = connection.get_connection()

    # create cursor
    cur = conn.cursor()

    # execute query
    cur.execute(query)

    # commit your changes
    conn.commit()

    # close the cursor
    cur.close()

    # close the connection
    conn.close()

def execute_select_query(query):
    # get connection
    conn = connection.get_connection()

    # create cursor
    cur = conn.cursor()

    # execute query
    cur.execute(query)

    # extract data from cursor
    data = cur.fetchall()

    # close the cursor
    cur.close()

    # close the connection
    conn.close()

    # return data
    return data