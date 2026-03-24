import sqlite3
DB_FILE="players.db"
def get_connection():
    return sqlite3.connect(DB_FILE)
def get_player(player_id):
    # fetch player data for given players id 
    conn= get_connection()  #connecting to database
    cursor = conn.cursor() # creartin cursor to execute sql commands 
    cursor.execute("SELECT * FROM Player WHERE PlayerID=?", (player_id,))
    player=cursor.fetchone()
    conn.close()
    return player

def Update_player(player_id, first_name, last_name, position, at_bats, hits):
    # updating a player infomation for a spesific id 
    conn = get_connection()
    cursor=conn.cursor 
    sql="""UPDATE Player 
         set firstName=?, lastName=?, position=?, atbats=?,hits=?
         WHERE playerid=?"""
    cursor.excute(sql,(first_name,last_name,position,at_bats,hits, player_id))
    conn.commit()
    conn.close()
