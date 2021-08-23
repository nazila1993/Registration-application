def longer_than_one (a) :
    return len (a) > 1

def ver_age (age):
    return 0 < int(age) < 120

def ver_yes_no(b):
    return b.strip().lower() in "yn"



def us_citizen(state):
    states = ["AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", 
    "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MI", 
    "MA", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
    "MP", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VT",
    "VA", "VI", "WA", "WV", "WI", "WY"]
    return state.upper() in states

def ver_zip(zipcode):
    return True
