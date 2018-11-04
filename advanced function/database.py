# coding=utf-8
import sqlite3
import unittest
import os

"""
THIS VERSION WILL USE SQLITE3 INSTEAD OF LEAN CLOUD DATABASE!
TIME: 2018-11-3 19:20:37
AUTHOR: Jakie Peng
"""

# 1. 确定数据库存储位置
# 2. 确定数据库名称以及键位名称

root_dir = os.path.abspath(".")  # default root directory

# usable parameters for creating tables
INT = "INTEGER"                         # 整数
TEXT = "TEXT"                       # 文本格式，为了简便，这里省略使用Char
BLOB = "BLOB"                       # 根据数据内容调整格式
NULL = "NULL"                       # 空值
PRIMARY = "PRIMARY KEY"             # 主键
NOT = "NOT"                         # 否
AUTOINCREMENT = "AUTOINCREMENT"     # 递增（数字）
REAL = "REAL"                       # 其规则基本等同于NUMERIC，唯一的差别是不会将"30000.0"这样的文本数据转换为INTEGER存储方式。


# util functions
# -----------------------
# generate the format of keys
def database_key(key_name: str, *args)->dict:
    r = dict()
    r["key_name"] = key_name
    r["parameters"] = [i for i in args]
    return r


# query info data dict
def database_dict_struct(name: str, value)->dict:
    return {"name": name, "value": value}


# parse the config info to the SQL language
def parse_database_config(config: dict)->str:
    r = "CREATE TABLE " + config.get("name") + "("
    for i in config.get("keys"):
        r = r + i.get("key_name") + " " + " ".join(i.get("parameters")) + ","
    r = r[:-1] + ")"
    return r


# 将表示系列{键，值}的条件用某个条件连接起来，可以是and也可以是or
def parse_database_condition(junction: str, info_list)->str:
    r = ""
    for i in info_list:
        if isinstance(i.get("value"), str):
            r = r + " " + i.get("name") + "=" + "\"" + i.get("value") + "\" " + junction
        else:
            r = r + " " + i.get("name") + "=" + str(i.get("value")) + " " + junction
    length = len(junction) + 1
    return r[:-length]


# parse_database_values with insert and update
def parse_database_insert_values(info_list)->str:
    keys = " ("
    values = " VALUES ("
    for i in info_list:
        keys = keys + i.get("name") + ", "
        if isinstance(i.get("value"), str):
            values = values + "\"" + i.get("value") + "\", "
        else:
            values = values + str(i.get("value")) + ", "
    r = keys[:-2] + ")" + values[:-2] + ")"
    return r


config_example = {
    "name": "EXAMPLE_TABLE",
    "keys":
        [database_key("id", INT, PRIMARY, AUTOINCREMENT, NOT, NULL),  # id
         database_key("name", TEXT, NOT, NULL),                       # 姓名
         database_key("description", TEXT, NULL)                      # 描述信息
         ]
}


class Database:
    # 数据库
    def __init__(self, name: str):  # name refers to the name of the database rather than the table!
        self.name = root_dir + os.path.sep + name + ".db"
        self.conn = sqlite3.connect(self.name)  # 连接数据库
        self.cursor = self.conn.cursor()

    # 关闭与数据库的连接
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    # establish the TABLE in the database
    def create_tables(self, config):
        sql = parse_database_config(config) + ";"
        self.cursor.execute(sql)
        self.conn.commit()

    # show all the tables
    def show_table_info(self, table_name: str)->list:
        self.cursor.execute("PRAGMA table_info(%s)"% table_name)
        r = self.cursor.fetchall()
        return r

    # query the table with condition
    # ---------
    # | keywords: junction = "AND" | "OR"
    # | SELECT * FROM table_name WHERE args[0]["name"]=args[0]["value"] (junction) args[1]["name"]= ...
    # ---------
    def query(self, table_name: str, *args, **kwargs)->list:
        junction = kwargs.get("junction", "AND")
        condition = parse_database_condition(junction, args)
        sql = "SELECT * FROM %s" % table_name
        if condition.replace(" ", "") != "":
             sql = sql + " WHERE " + condition
        sql += ";"
        self.cursor.execute(sql)
        r = self.cursor.fetchall()
        return r

    # insert the table
    # --------
    # | INSERT INTO table (a, b) VALUES ("d", "c")
    # --------
    def insert(self, table_name: str, *args):
        sql = "INSERT INTO %s" % table_name
        sql += parse_database_insert_values(args)
        sql += ";"
        self.cursor.execute(sql)
        self.conn.commit()

    # update the database
    # --------
    # | condition = where ""
    # | UPDATE TABLE SET a=b WHERE condition;
    # --------
    def update(self, table_name: str, *args, **kwargs):
        condition = kwargs.get("condition")
        set_values = parse_database_condition(",", args)
        sql = "UPDATE %s SET" % table_name + set_values
        if condition:
            sql = sql + " WHERE" + condition
        sql += ";"
        self.cursor.execute(sql)
        self.conn.commit()

    # delete the elements in table
    # +-------
    # + DELETE FROM TABLE WHERE a = b;
    # --------
    def delete(self, table_name: str, *args, **kwargs):
        junction = kwargs.get("junction", "AND")
        condition = parse_database_condition(junction, args)
        sql = "DELETE FROM %s" % table_name
        if condition.replace(" ", "") != "":
             sql = sql + " WHERE " + condition
        sql += ";"
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()


# Function UNITTEST
class TestDatabase(unittest.TestCase):
    def test_database_key(self):
        target = {"key_name": "abc", "parameters": [TEXT, PRIMARY, NOT, NULL]}
        self.assertEqual(target, database_key("abc", TEXT, PRIMARY, NOT, NULL))

    def test_parse_database_config(self):
        target = "CREATE TABLE EXAMPLE_TABLE(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,name TEXT NOT NULL,description TEXT NULL)"
        self.assertEqual(target, parse_database_config(config_example))

    def test_database_query_dict(self):
        target = {"name": "name", "value": "uozoyo"}
        self.assertEqual(target, database_dict_struct("name", "uozoyo"))

    def test_parse_database_condition(self):
        c = [database_dict_struct("a", "b"), database_dict_struct("c", "d")]
        d = [database_dict_struct("a", 1), database_dict_struct("c", "d")]
        r = parse_database_condition("AND", c)
        r2 = parse_database_condition("AND", d)
        target = " a=\"b\" AND c=\"d\""
        target2 = " a=1 AND c=\"d\""
        self.assertEqual(target2, r2)
        self.assertEqual(target, r)

    def test_parse_database_insert_values(self):
        c = [database_dict_struct("a", "b"), database_dict_struct("c", "d")]
        target = " (a, c) VALUES (\"b\", \"d\")"
        self.assertEqual(target, parse_database_insert_values(c))
        d = [database_dict_struct("a", 1), database_dict_struct("c", "d")]
        target2 = " (a, c) VALUES (1, \"d\")"
        self.assertEqual(target2, parse_database_insert_values(d))


# boot the unit test
if __name__ == "__main__":
    # unittest.main()
    d = Database("uozoyo")
    # d.create_tables(config_example)
    # d.show_table_info("EXAMPLE_TABLE")
    d.insert("EXAMPLE_TABLE", database_dict_struct("name", "b"), database_dict_struct("description", "d"))
    d.update("EXAMPLE_TABLE", database_dict_struct("name", "peng"), database_dict_struct("description", "d"),
             condition=parse_database_condition("AND", [database_dict_struct("name", "b"), database_dict_struct("description", "d")]))
    d.delete("EXAMPLE_TABLE")
    print(d.query("EXAMPLE_TABLE"))
