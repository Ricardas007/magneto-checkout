class ProductPage:
    def __init__(self, page):
        self.page = page
        self.product_item = page.locator(".product-item-link")
        self.items_per_page = page.locator("#limiter").nth(1)
        self.breadcrumbs_category = page.locator(".breadcrumbs")
        self.items_selected_size = page.locator(".size .swatch-attribute-selected-option")
        self.items_size_btn = page.locator(".size")
        self.items_color_btn = page.locator(".color")
        self.items_quantity_option = page.locator(".control .qty")
        self.add_to_cart_btn = page.get_by_role("button", name="Add to Cart")
        self.add_qty_filed = page.get_by_role("spinbutton", name="Qty")
        self.suggested_list_items = page.locator(".products-upsell .product-item-name")


    def select_items_per_page(self, displayed_number):
        self.items_per_page.select_option(displayed_number)

    def select_item_size(self, item_size):
        self.items_size_btn.get_by_role("option", name=item_size, exact=True).click()

    def select_item_color(self, item_color):
        self.items_color_btn.get_by_role("option", name=item_color).click()

    def select_item_quantity(self, quantity):
        self.add_qty_filed.fill(str(quantity))

    def add_to_cart(self):
        self.add_to_cart_btn.click()

    def select_breadcrumbs_category(self, category_name):
        self.breadcrumbs_category.get_by_role("link", name=category_name).click()

    def select_item_from_suggested(self, select_item):
        self.suggested_list_items.nth(select_item).click()



