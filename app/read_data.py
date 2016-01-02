import csv
from app import db
from models import TruckData
data_file = "Mobile_Food_Facility_Permit.csv"
csv_file = csv.DictReader(open(data_file, 'rb'), delimiter=',')
db.create_all()
for row in csv_file:
        table_entries = {}
        for key, value in row.items():
                table_entries[key] = value

        table_row = TruckData(table_entries['locationid'],table_entries['Applicant'],table_entries['FacilityType'],table_entries['cnn'],table_entries['LocationDescription'],table_entries['Address'],table_entries['blocklot'],table_entries['block'],table_entries['lot'],table_entries['permit'],table_entries['Status'],table_entries['FoodItems'],table_entries['X'],table_entries['Y'],table_entries['Latitude'],table_entries['Longitude'],table_entries['Schedule'],table_entries['dayshours'],table_entries['NOISent'],table_entries['Approved'],table_entries['Received'],table_entries['PriorPermit'],table_entries['ExpirationDate'],table_entries['Location'])

        db.session.add(table_row)
        db.session.commit()