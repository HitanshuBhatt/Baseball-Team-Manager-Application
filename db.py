import os
import sqlite3

base_dir = os.path.dirname(__file__)
DB_FILE = os.path.join(base_dir, "baseball_sql.db")





def get_connection():
    return sqlite3.connect(DB_FILE)

def get_player(player_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT playerID, batOrder, firstName, lastName, position, atBats, hits FROM Player WHERE playerID=?", 
                   (player_id,))
    player = cursor.fetchone()
    conn.close()
    return player

def update_player(player_id, bat_order, first_name, last_name, position, at_bats, hits):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """UPDATE Player
             SET batOrder=?, firstName=?, lastName=?, position=?, atBats=?, hits=?
             WHERE playerID=?"""
    cursor.execute(sql, (bat_order, first_name, last_name, position, at_bats, hits, player_id))
    conn.commit()
    conn.close()


#  function to add player 
def add_player(player_id,bat_order,first_name, last_name,position,at_bats,hits):
    # adding a new player to the database
    conn = get_connection()
    cursor=conn.cursor()
    sql = """INSERT INTO Player 
             (playerID, batOrder, firstName, lastName, position, atBats, hits) 
             VALUES (?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(sql,(player_id,bat_order,first_name, last_name,position,at_bats,hits))
    conn.commit() # saving changes in the database
    conn.close()

def delete_player(player_id):
    # Deleting a player record based on the playerID
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Player WHERE playerID = ?"
    cursor.execute(sql, (player_id,))
    conn.commit()
    conn.close()