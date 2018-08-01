
class Checkout:
    class Discount:
        def __init__(self, req_items, price):
            self.req_items = req_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.cart = {}
        self.discounts = {}

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item not in self.prices:
            raise NameError("Item not found.")
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1

    def calculate_current_total(self):
        total = 0
        for item, cnt in self.cart.items():
            total += self._calculate_item_total(item, cnt)
        return total

    def _calculate_item_total(self, item, cnt):
        total = 0
        discount_applied = False
        if item in self.discounts:
            discount = self.discounts.get(item)
            if discount.req_items <= cnt:
                discount_applied = True
                total += self._calculate_item_discounted_total(item, cnt, discount)
        if not discount_applied:
            total += self.prices[item] * cnt
        return total

    def _calculate_item_discounted_total(self, item, cnt, discount):
        total = (cnt // discount.req_items) * discount.price
        total += self.prices[item] * (cnt % discount.req_items)
        return total

    def add_discount(self, item, req_items, price):
        discount = self.Discount(req_items, price)
        self.discounts[item] = discount
