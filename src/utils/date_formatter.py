from datetime import date

def build_date():
    today = date.today()
    return today.strftime("%y/%m/%d")

def build_date_eliot():
    today = date.today()
    return today.strftime("%y%m%d")
