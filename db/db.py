import aiosqlite
import discord

async def connect():
    db_connect = await aiosqlite.connect("pokedex.sqlite")
    connect.row_factory = aiosqlite.Row
    return connect

# Encounter wild pokemon
async def wild_encounter(randomPoke):
    connect = await db_connect()
    cursor = await connect.cursor()
    sql = """
    SELECT id, identifier
    FROM pokemon
    HERE id=?;"""
    await cursor.execute(sql, (randomPoke,))
    fetched_data = await cursor.fetchall()
    await connect.close()
    for tuple in fetched_data:
        num, name = tuple
    return name

def test():
    print("import works")