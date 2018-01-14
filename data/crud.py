import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

conn = r.connect( "rethinkdb", 28015).repl()
try:
        print(r.db_create('crypto').run(conn))
except RqlRuntimeError:
        print('db crypto exists!')

def __create_table__(table):
        try:
                print(r.db("crypto").table_create(table).run())
        except:
                pass
def update(collection,filter,data):
        __create_table__(collection)
        print(r.db("crypto").table(collection).insert(data).run(conn))


def save(collection,data):
        __create_table__(collection)
        print(f'data class:{data.__class__}')
        print(r.db("crypto").table(collection).insert(data).run(conn))


def read(collection):
        return r.db("crypto").table(collection).run(conn)

def read_one(collection,id):
        return r.db("crypto").filter(r.row["id"] == id).run(conn)


if __name__ == '__main__':
        save('test',[{'test':'test'}])