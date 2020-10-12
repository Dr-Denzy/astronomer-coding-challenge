from acme.products import Product


class Cart:

    def __init__(self):
        self.widgets_cost = 0
        self.widgets = {}

    def add_to_cart(self, product, quantity):
        self.widgets[product] = quantity

        if product.code == 'R01':
            self.widgets_cost += self.red_widget_offer(product, quantity)
        else:
            self.widgets_cost += product.price * quantity

    @staticmethod
    def red_widget_offer(product, quantity):
        if quantity == 1:
            total = product.price
            return round(total, 2)

        if quantity > 1:
            if quantity % 2 == 0:
                total = ((quantity / 2) * product.price) + ((quantity / 2) * (product.price / 2))
                return round(total, 2)
            else:
                total = (((quantity - 1) / 2) * product.price) + (
                        ((quantity - 1) / 2) * (product.price / 2)) + product.price
                return round(total, 2)

    def get_total_bill(self):
        total_bill = 0
        if self.widgets_cost < 50:
            return round((total_bill + self.widgets_cost + 4.95), 2)
        elif self.widgets_cost < 90:
            return round((total_bill + self.widgets_cost + 2.95), 2)
        elif self.widgets_cost >= 90:
            return round((total_bill + self.widgets_cost + 0), 2)

    def __repr__(self):
        return f"widgets: {self.widgets}"


if __name__ == "__main__":
    r = Product('Red Widget', 'R01', 32.95)
    g = Product('Green Widget', 'G01', 24.95)
    b = Product('Blue Widget', 'B01', 7.95)
    cart = Cart()
    # cart.add_to_cart(r, 2)
    # cart.add_to_cart(g, 1)
    cart.add_to_cart(b, 1)
    cart.add_to_cart(b, 1)
    cart.add_to_cart(r, 3)
    # cart.add_to_cart(r, 1)
    # cart.add_to_cart(r, 1)
    # print(cart)
    print(cart.get_total_bill())
