from flask import render_template, request, redirect, url_for
from wages_calculator import app, db
from wages_calculator.models import Driver, DayEnd


@app.route("/")
def home():
    return render_template("data_entry.html")

@app.route("/add_driver", methods=["GET", "POST"])
def add_driver():
    drivers = list(Driver.query.order_by(Driver.first_name).all())
    # reformat numbers
    for driver in drivers:
        driver.base_wage = driver.base_wage/100
        driver.bonus_percentage = driver.bonus_percentage*100
    if request.method == "POST":
        driver = Driver(
            start_date=request.form.get("start_date"),
            first_name=request.form.get("first_name"),
            second_name=request.form.get("second_name"),
            base_wage=float(request.form.get("base_wage"))*100,
            bonus_percentage=float(request.form.get("bonus_percentage"))/100
            )
        db.session.add(driver)
        db.session.commit()
        return redirect(url_for("add_driver", drivers=drivers))
    return render_template("add_driver.html", drivers=drivers)

@app.route("/delete_driver/<int:driver_id>")
def delete_driver(driver_id):
    entry = Driver.query.get_or_404(driver_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for("add_driver"))

@app.route("/edit_driver/<int:driver_id>", methods=["POST"])
def edit_driver(driver_id):
    driver = Driver.query.get_or_404(driver_id)
    driver.start_date = request.form.get("start_date")
    driver.first_name = request.form.get("first_name")
    driver.second_name = request.form.get("second_name")
    driver.base_wage = float(request.form.get("base_wage"))*100
    driver.bonus_percentage = float(request.form.get("bonus_percentage"))/100
    db.session.commit()
    return redirect(url_for("add_driver"))

@app.route("/add_day_end", methods=["GET", "POST"])
def add_day_end():
    drivers = list(Driver.query.order_by(Driver.first_name).all())
    day_end_entries = list(DayEnd.query.order_by(DayEnd.date).all())
    if request.method == "POST":
        day_end_entry = DayEnd(
            date = request.form.get("date"),
            earned = request.form.get("earned"),
            overnight = bool(True if request.form.get("overnight") else False),
            driver_id = request.form.get("driver_id")
        )
        db.session.add(day_end_entry)
        db.session.commit()
        return redirect(url_for("add_day_end", drivers=drivers, day_end_entries=day_end_entries))
    return render_template("add_day_end.html", drivers=drivers, day_end_entries=day_end_entries)

@app.route("/delete_day_end/<int:day_id>")
def delete_day_end(day_id):
    entry = DayEnd.query.get_or_404(day_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for("add_day_end"))

@app.route("/edit_day_end/<int:day_id>", methods=["POST"])
def edit_day_end(day_id):
    entry = DayEnd.query.get_or_404(day_id)
    entry.date = request.form.get("date")
    entry.earned = request.form.get("earned")
    entry.overnight = bool(True if request.form.get("overnight") else False)
    entry.driver_id = request.form.get("driver_id")
    db.session.commit()
    return redirect(url_for("add_day_end"))




