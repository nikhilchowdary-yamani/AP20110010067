import requests

# Register your company
register_url = "http://20.244.56.144/train/register"
company_details = {
    "companyName": "Train Central",
    "ownerName": "Rahul",
    "rollNo": "1",
    "ownerEmail": "rahul@abc.edu",
    "accessCode": "FKDLjg"
}
response = requests.post(register_url, json=company_details)
client_id = response.json()["clientID"]  # Corrected key
client_secret = response.json()["clientSecret"]  # Corrected key

# Obtain an authorization token
auth_url = "http://20.244.56.144/train/auth"
auth_data = {
    "companyName": "Train Central",
    "clientID": client_id,
    "clientSecret": client_secret,
    "ownerName": "Rahul",
    "ownerEmail": "rahul@abc.edu",
    "rollNo": "1"
}
auth_response = requests.post(auth_url, json=auth_data)
access_token = auth_response.json()["access_token"]

# Get train schedules, seat availability, and pricing
trains_url = "http://20.244.56.144/train/trains"
headers = {"Authorization": f"Bearer {access_token}"}
trains_response = requests.get(trains_url, headers=headers)
train_data = trains_response.json()

# Process and display train information
for train in train_data:
    train_name = train["trainName"]
    train_number = train["trainNumber"]
    departure_time = train["departureTime"]
    sleeper_price = train["price"]["sleeper"]
    sleeper_seats = train["seatsAvailable"]["sleeper"]
    ac_price = train["price"]["AC"]
    ac_seats = train["seatsAvailable"]["AC"]
    
    # Display train information
    print(f"Train: {train_name} ({train_number})")
    print(f"Departure: {departure_time['Hours']}:{departure_time['Minutes']}")
    print(f"Sleeper: Price: {sleeper_price}, Seats available: {sleeper_seats}")
    print(f"AC: Price: {ac_price}, Seats available: {ac_seats}")
    print("-----------------------------------")
