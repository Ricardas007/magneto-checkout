class HeaderPage:

    def __init__(self, page):
        self.page = page
        self.basket_counter = page.locator(".counter-number")

    def cart_icon(self):
        self.basket_counter.click()


# get_by_role("link", name="1")