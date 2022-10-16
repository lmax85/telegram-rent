import psycopg2

# data = [('0x18f9f00a432F50c6E2429d31776724d3cB873BEF', '1000', 'mot ngan'),
#         ('0x06471C53CE649Eb4dA88b792D500544A7E5C9635', '2000', 'hai ngan')]

def connect():
    return psycopg2.connect(user="max",
        password="Qwer1234",
        host="127.0.0.1",
        port="5432",
        database="test")

def bulkInsert(table, data, insertColumns, updateColumns, conflictColumns):
    try:
        connection = connect()
        cursor = connection.cursor()

        # Update single record now
        args = [cursor.mogrify('(%s, %s, %s)', x).decode('utf-8') for x in data]
        args_str = ', '.join(args)

        cursor.execute('''INSERT INTO {table} (address, id, description) VALUES'''
                    + args_str +
                    '''ON CONFLICT (address) DO UPDATE SET
                (address, id, description) = (EXCLUDED.address, EXCLUDED.id, EXCLUDED.description)''')
        print("Upsert was successfully finshed")

    except (Exception, psycopg2.Error) as error:
        print("Error in bulkInsert operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

async def upsertAuthors(id, type, first_name, last_name, description):
    try:
        conn = connect()
        curs = conn.cursor()

        args = curs.mogrify('(%s, %s, %s, %s, %s)', (id, type, first_name, last_name, description)).decode('utf-8')

        curs.execute('''INSERT INTO authors (id, type, first_name, last_name, description)
                    VALUES'''
                    + args +
                    '''ON CONFLICT (id) DO UPDATE SET
                (type, first_name, last_name, description) = (EXCLUDED.type, EXCLUDED.first_name, EXCLUDED.last_name, EXCLUDED.description)''')
        conn.commit()
        print("Upsert was successfully finshed")

    except Exception as error:
        print("Error in upsertAuthors operation", error)

    finally:
        # closing database connection.
        if conn:
            curs.close()
            conn.close()
            print("PostgreSQL connection is closed")