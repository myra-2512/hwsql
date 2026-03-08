import sqlite3
import pandas as pd

database='basketball.sqlite'

conn=sqlite3.connect(database)

tables=tables=pd.read_sql("""SELECT *
                    FROM sqlite_master
                    WHERE type='table';""", conn)
print(tables)

player1=pd.read_sql("""SELECT *
                    FROM Player""", conn)

print(player1)

player_sal=pd.read_sql("""SELECT *
                    FROM Player_Salary""", conn)
print(player_sal)

join1=pd.read_sql("""SELECT nameTeam, namePlayer, value,is_active
                    FROM Player
                    JOIN Player_Salary
                    ON Player.full_name=Player_Salary.namePlayer""", conn)
print(join1)