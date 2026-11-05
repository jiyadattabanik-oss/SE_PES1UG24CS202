import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# Ticket price: seat validation
def test_valid_seat_types():
    assert ticket_price("regular", 25, 15, False) == 150
    assert ticket_price("premium", 25, 15, False) == 250
    assert ticket_price("recliner", 25, 15, False) == 400


def test_invalid_seat():
    with pytest.raises(ValueError):
        ticket_price("balcony", 25, 15, False)


# Ticket price: show-hour validation
def test_negative_show_hour():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, -1, False)


def test_show_hour_above_23():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, 24, False)


# Ticket price: morning, afternoon and evening
def test_morning_show():
    assert ticket_price("regular", 25, 11, False) == 100


def test_afternoon_show():
    assert ticket_price("regular", 25, 12, False) == 150


def test_evening_show():
    assert ticket_price("regular", 25, 18, False) == 180


# Ticket price: weekend and weekday
def test_weekend_price():
    assert ticket_price("regular", 25, 15, True) == 190


def test_weekday_price():
    assert ticket_price("regular", 25, 15, False) == 150


# Ticket price: age conditions
def test_child_below_three():
    assert ticket_price("regular", 2, 15, False) == 0


def test_child_age_three():
    assert ticket_price("regular", 3, 15, False) == 75


def test_senior_age_sixty():
    assert ticket_price("regular", 60, 15, False) == 75


def test_adult_age():
    assert ticket_price("regular", 25, 15, False) == 150


# Group discount: ticket-count conditions
def test_zero_tickets():
    with pytest.raises(ValueError):
        group_discount(0, False)


def test_small_group():
    assert group_discount(2, False) == 0


def test_medium_group():
    assert group_discount(5, False) == 10


def test_large_group():
    assert group_discount(10, False) == 15


# Group discount: student and non-student conditions
def test_small_student_group():
    assert group_discount(2, True) == 0


def test_medium_student_group():
    assert group_discount(5, True) == 15


def test_large_student_group():
    assert group_discount(10, True) == 20


# Snack combo: all size conditions
def test_small_snack():
    assert snack_combo("small", False) == 120


def test_medium_snack():
    assert snack_combo("medium", False) == 180


def test_large_snack():
    assert snack_combo("large", False) == 250


# Snack combo: coupon conditions
def test_coupon_applied():
    assert snack_combo("small", True) == 70


def test_no_coupon():
    assert snack_combo("small", False) == 120
