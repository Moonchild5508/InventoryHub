import sqlite3

def get_inventory():
    conn = sqlite3.connect('inventoryhub.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, quantity FROM Inventory")
    items = [{"id": row[0], "name": row[1], "quantity": row[2]} for row in cursor.fetchall()]
    conn.close()
    return items

def add_item(item):
    conn = sqlite3.connect('inventoryhub.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Inventory (name, quantity) VALUES (?, ?)", (item['name'], item['quantity']))
    conn.commit()
    conn.close()
