import csv
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from models import TruckData
from app import db
import os.path

db.create_all()

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

data_file = "Mobile_Food_Facility_Permit.csv"
csv_file = csv.DictReader(open(data_file, 'rb'), delimiter=',')
for row in csv_file:
        table_entries = {}
        for key, value in row.items():
                table_entries[key] = value

        table_row = TruckData(table_entries['locationid'],table_entries['Applicant'],table_entries['FacilityType'],table_entries['cnn'],table_entries['LocationDescription'],table_entries['Address'],table_entries['blocklot'],table_entries['block'],table_entries['lot'],table_entries['permit'],table_entries['Status'],table_entries['FoodItems'],table_entries['X'],table_entries['Y'],table_entries['Latitude'],table_entries['Longitude'],table_entries['Schedule'],table_entries['dayshours'],table_entries['NOISent'],table_entries['Approved'],table_entries['Received'],table_entries['PriorPermit'],table_entries['ExpirationDate'],table_entries['Location'])

        db.session.add(table_row)
        db.session.commit()