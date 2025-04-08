class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.product_item = page.locator("li.product-item")
        self.item_name = page.locator(".product-item-name")
        self.item_price = page.locator(".product-item .price")
        self.cheapest_product = page.locator(".product-item").first
        self.sort_by_btn = page.get_by_label("Sort By")
        self.products_amount_displayed = page.locator(".toolbar-amount").first
        self.open_filter_btn = page.get_by_role("tab", name="Price ")
        self.filter_cheapest_products_prices = page.get_by_role("link", name="$30.00 - $39.99")

    def select_item_by_name(self, query):
        self.item_name.get_by_text(query).click()

    def sort_by_price_descending(self):
        self.sort_by_btn.select_option("price")

    def open_price_filter(self):
        self.open_filter_btn.click()

    def filter_cheapest_products_range(self):
        self.filter_cheapest_products_prices.click()

    def select_cheapest_product(self):
        self.cheapest_product.click()
