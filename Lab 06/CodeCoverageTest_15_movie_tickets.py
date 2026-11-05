import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


def test_regular_afternoon():
    assert ticket_price("regular", 25, 15, False) == 150


def test_premium_morning_weekend():
    assert ticket_price("premium", 25, 10, True) == 240


def test_recliner_evening():
    assert ticket_price("recliner", 25, 19, False) == 430


def test_child_under_three():
    assert ticket_price("regular", 2, 15, False) == 0


def test_child_discount():
    assert ticket_price("regular", 10, 15, False) == 75


def test_senior_discount():
    assert ticket_price("premium", 65, 19, True) == 160


def test_invalid_seat():
    with pytest.raises(ValueError):
        ticket_price("balcony", 25, 15, False)


def test_invalid_show_hour():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, 24, False)


def test_negative_show_hour():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, -1, False)


def test_small_group():
    assert group_discount(2, False) == 0


def test_medium_group():
    assert group_discount(5, False) == 10


def test_large_student_group():
    assert group_discount(10, True) == 20


def test_no_tickets():
    with pytest.raises(ValueError):
        group_discount(0, False)


def test_small_snack_without_coupon():
    assert snack_combo("small", False) == 120


def test_medium_snack_with_coupon():
    assert snack_combo("medium", True) == 130


def test_large_snack_without_coupon():
    assert snack_combo("large", False) == 250
