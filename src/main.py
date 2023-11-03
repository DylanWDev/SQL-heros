from database.db_connection import execute_query, execute_modify

def read_heroes_table():
    query = "SELECT * FROM heroes"

    returned_items = execute_query(query)
    for item in returned_items:
        print(item)
    return returned_items

def create_new_character(name, about_me, biography):
    check_query = "SELECT id FROM heroes WHERE name = %s;"
    result = execute_query(check_query, (name,))

    if not result:
        insert_query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s);"
        execute_modify(insert_query, (name, about_me, biography))
    else:
        print(f"Character with the name '{name}' already exists in the database.")

def update_existing_character():
    name = input("Enter the character's name you want to update: ")
    check_query = "SELECT id FROM heroes WHERE name = %s;"
    result = execute_query(check_query, (name,))
    
    if result:
        new_name = input("Enter the character's new name: ")
        about_me = input("Enter the updated about me information: ")
        biography = input("Enter the updated biography: ")
        update_query = "UPDATE heroes SET about_me = %s, biography = %s, name = %s WHERE name = %s;"
        execute_modify(update_query, (about_me, biography, new_name, name))
    else:
        print(f"Character '{name}' not found in the database.")

def delete_character(name):
    check_query = "SELECT id FROM heroes WHERE name = %s;"
    result = execute_query(check_query, (name,))

    if result:
        delete_query = "DELETE FROM heroes WHERE name = %s;"
        execute_modify(delete_query, (name,))
        print(f"Character '{name}' has been deleted from the database.")
    else:
        print(f"Character '{name}' not found in the database.")
    

user_continue = True
while user_continue:
    func = ["create", "read", "update", "delete"]
    select_functionality = input("CREATE, READ, UPDATE, DELETE: ").lower()
    if select_functionality == "read":
        read_heroes_table()
    elif select_functionality == "create":
        name = input("Enter the character's name: ")
        about_me = input("Enter info about the character: ")
        biography = input("Enter the character's biography: ")
        create_new_character(name, about_me, biography)
    elif select_functionality == "update":
        update_existing_character()
    elif select_functionality == "delete":
        name = input("Enter the character's name you want to delete: ")
        delete_character(name)