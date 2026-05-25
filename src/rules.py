"""
    Compute the price of room based on multiple rules:
    - Children age < 5 : free
    - Standard room max : 2 guest
    - Family room max : 5 guest
    - Weekend booking adds 20%
    - Holiday booking adds 40%
    - Booking duration must be : 1 - 14 nightsother rules
"""

def compute_room_price(
    guest_age,
    room_type,
    booking_day,
    stay_duration,
):
    
    if guest_age < 0:
        raise ValueError("Invalid age: Age cannot be negative.")
    
    return int(base_price * stay_duration)