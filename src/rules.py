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
    
    return