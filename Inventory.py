from database import *

class Inventory:

    @staticmethod
    def add_blood(blood_type, quantity=1):
        query = f"""SELECT quantity from inventory WHERE
        blood_type = "{blood_type}";"""
        result = db_query(query)[0][0]
        print(result)
        result = result + quantity
        query = f"""UPDATE inventory SET quantity = {result} WHERE
                blood_type = "{blood_type}";"""
        db_query(query)
        mydb.commit()

    @staticmethod
    def deduct_blood(blood_type, quantity=1):
        query = f"""SELECT quantity from inventory WHERE
                blood_type = "{blood_type}";"""
        result = db_query(query)[0][0]
        print(result)
        if result < quantity:
            print(f"Sorry Not Sufficient Blood Available {blood_type}")
        else:
            result = result - quantity
            query = f"""UPDATE inventory SET quantity = {result} WHERE
                                    blood_type = "{blood_type}";"""
            db_query(query)
            mydb.commit()

# Inventory.deduct_blood("A+",10)