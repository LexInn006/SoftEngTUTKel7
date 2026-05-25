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
    
    if stay_duration < 1 or stay_duration > 14:
        raise ValueError("Invalid stay duration: Must be between 1 and 14 nights.")
    
    if room_type not in ["standard", "family"]:
        raise ValueError("Invalid room type: Must be 'standard' or 'family'.")
    
    if booking_day not in ["weekday", "weekend", "holiday"]:
        raise ValueError("Invalid booking day: Must be 'weekday', 'weekend', or 'holiday'.")

    
    return 