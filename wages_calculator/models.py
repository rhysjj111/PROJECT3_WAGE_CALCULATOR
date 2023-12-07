from wages_calculator import db

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    second_name = db.Column(db.String(30), nullable=False)
    base_wage = db.Column(db.Integer, nullable=False)
    bonus_percentage = db.Column(db.Integer, nullable=False)
    day_end_days = db.relationship("Day_end", backref="driver", cascade="all, delete", lazy=True)


    def __repr__(self): 
        #represents itself in form of string
        return f"Driver: {self.first_name} {self.last_name}"

class Day_end(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    earned = db.Column(db.Integer, nullable=False)
    overnight = db.Column(db.Boolean, nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey("driver.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        #represents itself in form of string
        return f"Enry for: {driver.first_name} {driver.last_name} on {self.date}"
