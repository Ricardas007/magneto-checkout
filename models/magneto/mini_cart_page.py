class MiniCartPage:
    def __init__(self, page):
        self.page = page
        # self.mini_cart_product_name = page.locator("#mini-cart")
        self.minicart_product_name = page.locator(".block-minicart .product-item-name")
        self.minicart_delete_item_btn = page.get_by_role("link", name=" Remove")
        self.minicart_checkout_btn = page.get_by_role("button", name="Proceed to Checkout")
        self.minicart_delete_message_option_btn = page.locator(".modal-footer")


    def get_product_title(self):
        return self.minicart_product_name.text_content()


    def checkout_btn(self):
        self.minicart_checkout_btn.click()

    def delete_item_from_cart(self):
        self.minicart_delete_item_btn.nth(0).click()

    def confirm_or_cansel_item_from_cart(self, select_option):
        self.minicart_delete_message_option_btn.get_by_role("button", name=select_option).click()
