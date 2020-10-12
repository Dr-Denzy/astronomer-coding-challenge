import pytest
from acme.cart import Cart
from acme.products import Product


@pytest.fixture()
def cart():
    r1 = Product('Red Widget', 'R01', 32.95)
    g1 = Product('Green Widget', 'G01', 24.95)
    b1 = Product('Blue Widget', 'B01', 7.95)

    c1 = Cart()
    c1.add_to_cart(b1, 1)
    c1.add_to_cart(g1, 1)

    c2 = Cart()
    c2.add_to_cart(r1, 2)

    c3 = Cart()
    c3.add_to_cart(r1, 1)
    c3.add_to_cart(g1, 1)

    c4 = Cart()
    c4.add_to_cart(b1, 2)
    c4.add_to_cart(r1, 3)

    return c1, c2, c3, c4


def test_total_bill(cart):
    c1, c2, c3, c4 = cart

    assert c1.get_total_bill() == 37.85
    assert c2.get_total_bill() == 54.38
    assert c3.get_total_bill() == 60.85
    assert c4.get_total_bill() == 98.28



def test_red_widget_offer():
    r = Product('Red Widget', 'R01', 32.95)

    c1 = Cart()

    assert c1.red_widget_offer(r, 1) == 32.95
    assert c1.red_widget_offer(r, 2) == 49.43
    assert c1.red_widget_offer(r, 3) == 82.38
    assert c1.red_widget_offer(r, 4) == 98.85
    assert c1.red_widget_offer(r, 5) == 131.8
