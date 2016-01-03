from app import db
from datetime import datetime

class TruckData(db.Model):
    __tablename__ = "foodtruck"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    locationid = db.Column(db.Integer)
    Applicant = db.Column(db.String)
    FacilityType = db.Column(db.String)
    cnn = db.Column(db.Integer)
    LocationDescription = db.Column(db.String)
    Address = db.Column(db.String)
    blocklot = db.Column(db.String)
    block = db.Column(db.String)
    lot = db.Column(db.String)
    permit = db.Column(db.String)
    Status = db.Column(db.String)
    FoodItems = db.Column(db.String)
    X = db.Column(db.Float , nullable=True)
    Y = db.Column(db.Float , nullable=True)
    Latitude = db.Column(db.Float , nullable=True)
    Longitude = db.Column(db.Float , nullable=True)
    Schedule = db.Column(db.String)
    dayshours = db.Column(db.String)
    NOISent = db.Column(db.String, nullable = True)
    Approved = db.Column(db.String)
    Received = db.Column(db.String)
    PriorPermit = db.Column(db.Integer)
    ExpirationDate = db.Column(db.String)
    Location = db.Column(db.String)

    def __init__(self, locationid,Applicant,FacilityType,cnn,LocationDescription,Address,blocklot,block,lot,permit,Status,FoodItems,X,Y,Latitude,Longitude,Schedule,dayshours,NOISent,Approved,Received,PriorPermit,ExpirationDate,Location):
            self.locationid = int(locationid.strip())
            self.Applicant = Applicant
            self.FacilityType = FacilityType
            self.cnn = int(cnn.strip())
            self.LocationDescription = LocationDescription
            self.Address = Address
            self.blocklot = blocklot
            self.block = block
            self.lot = lot
            self.permit = permit
            self.Status = Status
            self.FoodItems = FoodItems
            if X.strip() is not "":
                self.X = float(X.strip())
            else:
                self.X = None

            if Y.strip() is not "":
                self.Y = float(Y.strip())
            else:
                self.Y = None

            if Latitude.strip() is not "":
                self.Latitude = float(Latitude.strip())
            else:
                self.Latitude = None

            if Longitude.strip() is not "":
                self.Longitude = float(Longitude.strip())
            else:
                self.Longitude = None

            self.Schedule = Schedule
            self.dayshours = dayshours


            self.NOISent = NOISent.strip()


            self.Approved = Approved.strip()
            self.Received = Received
            self.PriorPermit = int(PriorPermit.strip())
            self.ExpirationDate = ExpirationDate.strip()
            self.Location = Location
            #self.__dict__.update(kwargs)


    def __repr__(self):
        return '<TruckData %r>' % (self.locationid)