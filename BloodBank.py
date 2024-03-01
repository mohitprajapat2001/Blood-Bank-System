from database import *
from Inventory import Inventory

class BloodBank:

    @staticmethod
    def donor_details(donor_name, donor_age, donor_blood_type):
        query = f"""
        INSERT INTO donor ( donor_name, donor_age, donor_blood_type )
        VALUES ( "{donor_name}", {donor_age}, "{donor_blood_type}" )
"""
        db_query(query)
        mydb.commit()

    @staticmethod
    def request_blood(hospital_name,
                      patient_name,patient_age,patient_blood_type,
                      donor_name, donor_age, donor_blood_type):
        query = f"""INSERT INTO request 
        (hospital_name,patient_name,patient_age,patient_blood_type,
                      donor_name, donor_age, donor_blood_type)
        VALUES ( "{hospital_name}",
        "{patient_name}",{patient_age},"{patient_blood_type}",
                      "{donor_name}", {donor_age}, "{donor_blood_type}" );"""
        db_query(query)
        BloodBank.donor_details(donor_name,donor_age,donor_blood_type)
        Inventory.add_blood(donor_blood_type)
        Inventory.deduct_blood(patient_blood_type)
        mydb.commit()


