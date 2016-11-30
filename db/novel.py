import pysql
columns_1 = ['name', 'url', 'title']
key_1 = ['url', 'title']

def get():
    return pysql.table('novels', columns_1, key_1)

