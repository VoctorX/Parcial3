import sqlite3
conexion = sqlite3.connect("database.db")

# Create the table if it doesn't exist, now with AUTOINCREMENT
create_query="""
CREATE TABLE if not exists contactos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
phone TEXT NOT NULL,
image_path TEXT
);
"""
conexion.execute(create_query)

# Add the image_path column to existing tables that don't have it
# This is no longer needed with the new table definition, but we'll keep it
# just in case there are very old databases.
try:
    cursor = conexion.cursor()
    cursor.execute("PRAGMA table_info(contactos)")
    columns = [row[1] for row in cursor.fetchall()]
    if 'image_path' not in columns:
        conexion.execute("ALTER TABLE contactos ADD COLUMN image_path TEXT;")
except sqlite3.Error as e:
    # Avoid crashing if the ALTER fails for other reasons.
    print(f"Could not update table schema: {e}")

conexion.commit()
