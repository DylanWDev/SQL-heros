from database.db_connection import execute_query, execute_modify


def select_all_heroes():
    query = """
        SELECT * FROM heroes
    """

    returned_items = execute_query(query)
    for item in returned_items:
        print(item[1])
    return returned_items

select_all_heroes()


# def add_luffy():
#     prompt = input("Do you want to add Luffy? Y or N:")
#     if prompt == 'Y':
#         query = """
#             INSERT INTO heroes (name, about_me, biography)
#             VALUES ('Luffy', 'Captain of the Straw Hat Pirates', 'rubber man')
#             """
#         execute_modify(query)

# add_luffy()
    




def create_new_character(name, about_me, biography):
    check_query = "SELECT id FROM heroes WHERE name = %s;"
    result = execute_query(check_query, (name,))
    if not result:
        insert_query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s);"
        execute_modify(insert_query, (name, about_me, biography))


create_new_character("Sanji", "Chef of the Straw Hat Pirates", "His dream is to find the All Blue")
create_new_character("God Usopp", "Sniper of the Straw Hat Pirates/Liar", "His dream is to become a brave warrior of the sea!")

