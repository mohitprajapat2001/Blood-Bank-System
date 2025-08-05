from database import *
from Inventory import Inventory

class BloodBank:

    @staticmethod
    def donor_details(donor_name, donor_age, donor_blood_type):
        try:
            if not donor_name or not donor_blood_type or donor_age <= 0:
                print("Invalid donor details.")
                return

            query = """
                INSERT INTO donor (donor_name, donor_age, donor_blood_type)
                VALUES (%s, %s, %s)
            """
            values = (donor_name, donor_age, donor_blood_type)
            db_cursor.execute(query, values)
            mydb.commit()
            print(f"[INFO] Donor {donor_name} added successfully.")
        except Exception as e:
            print(f"[ERROR] Failed to add donor: {e}")

    @staticmethod
    def request_blood(hospital_name, patient_name, patient_age, patient_blood_type,
                      donor_name, donor_age, donor_blood_type):
        try:
            if not all([hospital_name, patient_name, patient_blood_type, donor_name, donor_blood_type]):
                print("[ERROR] Missing required fields.")
                return

            if patient_age <= 0 or donor_age <= 0:
                print("[ERROR] Invalid age input.")
                return

            # Check blood availability before proceeding
            if not Inventory.check_availability(patient_blood_type):
                print(f"[ERROR] Blood type '{patient_blood_type}' is not available.")
                return

            # Insert into request table
            query = """
                INSERT INTO request (
                    hospital_name, patient_name, patient_age, patient_blood_type,
                    donor_name, donor_age, donor_blood_type)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (hospital_name, patient_name, patient_age, patient_blood_type,
                      donor_name, donor_age, donor_blood_type)
            db_cursor.execute(query, values)
            mydb.commit()

            print("[INFO] Blood request recorded successfully.")

            # Update donor table and inventory
            BloodBank.donor_details(donor_name, donor_age, donor_blood_type)
            Inventory.add_blood(donor_blood_type)
            Inventory.deduct_blood(patient_blood_type)
        except Exception as e:
            print(f"[ERROR] Failed to process blood request: {e}")
