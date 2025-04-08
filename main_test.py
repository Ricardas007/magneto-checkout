from models.magneto.header_page import HeaderPage
from models.magneto.navbar_page import NavbarPage
from models.magneto.landing_page import LandingPage
from models.magneto.products_page import ProductsPage
from models.magneto.product_page import ProductPage
from models.magneto.mini_cart_page import MiniCartPage
from models.magneto.checkout_page import CheckoutPage

from playwright.sync_api import Page, expect
# Scenario one:
# ▪ Using navigation menu, find mens Hoodies & Sweatshirts section.
# ▪ Check/Assert that the displayed number of jackets matches the selected
# number of jackets displayed per page.
# ▪ Select “Frankie Sweatshirt” and open its details.
# ▪ Select size, colour and quantity.
# ▪ Add product to cart and check that cart icon is updated with product quantity.
# ▪ Open cart and check if product match the one You added to the cart.
# ▪ Proceed to checkout
# ▪ Complete the order.

def test_scenario_one(page: Page) -> None:
    landing_page = LandingPage(page)
    landing_page.navigation()
    navbar_page = NavbarPage(page)
    navbar_page.hover_over_men()
    product_page = ProductPage(page)
    product_page.select_items_per_page("12")
    expect(product_page.product_item).to_have_count(12)
    products_page = ProductsPage(page)
    products_page.select_item_by_name("Frankie Sweatshirt")
    product_page.select_item_size("S")
    expect(product_page.items_selected_size).to_have_text("S")
    product_page.select_item_color("Green")
    product_page.select_item_quantity(3)
    product_page.add_to_cart()
    header_page = HeaderPage(page)
    expect(header_page.basket_counter).to_have_text("3")
    header_page.cart_icon()
    mini_cart_page = MiniCartPage(page)
    expect(mini_cart_page.minicart_product_name).to_have_text("Frankie Sweatshirt")
    mini_cart_page.checkout_btn()
    checkout_page = CheckoutPage(page)
    checkout_page.email_field("test@test.com")
    checkout_page.password_field("test_user123&")
    checkout_page.username_field("Loch")
    checkout_page.user_last_name_field("Mond")
    checkout_page.street_address_field("Marimaris, 27 -16")
    checkout_page.country_field("LT")
    checkout_page.user_city_field("Vilnius")
    checkout_page.province_field("Vilniaus Apskritis")
    checkout_page.user_phone_field("37067767678")
    checkout_page.user_zip_code_field("44352")
    expect(checkout_page.shipping_checkbox_btn).to_be_visible()
    checkout_page.shipping_method_checkbox_fixed()
    checkout_page.next_button()
    checkout_page.place_order_button()
    expect(checkout_page.page_title).to_have_text("Thank you for your purchase!")


# ➢ Scenario two:
# ▪ Using navigation menu, find women pants section.
# ▪ Filter section to show the cheapest products available.
# ▪ Select the cheapest pants and add them to the cart.
# ▪ Add 2 more products to the cart. Check that cart icon is updated with each
# product.
# ▪ Remove product from the cart.
# ▪ Add product to the cart from suggested products.
# ▪ Proceed to checkout.
# ▪ Complete the order.

def test_scenario_two(page: Page) -> None:
    landing_page = LandingPage(page)
    landing_page.navigation()
    navbar_page = NavbarPage(page)
    navbar_page.hover_over_women()
    products_page = ProductsPage(page)
    products_page.open_price_filter()
    products_page.filter_cheapest_products_range()
    products_page.sort_by_price_descending()
    products_page.select_cheapest_product()
    product_page = ProductPage(page)
    product_page.select_item_size("28")
    product_page.select_item_color("blue")
    product_page.add_to_cart()
    header_page = HeaderPage(page)
    expect(header_page.basket_counter).to_have_text("1")
    product_page.select_breadcrumbs_category("Pants")
    products_page.select_item_by_name("Sahara Leggings")
    product_page.select_item_color("blue")
    product_page.select_item_size("28")
    product_page.add_to_cart()
    expect(header_page.basket_counter).to_have_text("2")
    product_page.select_breadcrumbs_category("Pants")
    products_page.select_item_by_name("Aeon Capri")
    product_page.select_item_color("orange")
    product_page.select_item_size("28")
    product_page.add_to_cart()
    expect(header_page.basket_counter).to_have_text("3")
    header_page.cart_icon()
    mini_cart_page = MiniCartPage(page)
    # page.pause()
    mini_cart_page.delete_item_from_cart()
    mini_cart_page.confirm_or_cansel_item_from_cart("OK")
    expect(header_page.basket_counter).to_have_text("2")
    product_page.select_item_from_suggested(1)
    product_page.select_item_size("28")
    product_page.select_item_color("blue")
    product_page.add_to_cart()
    expect(header_page.basket_counter).to_have_text("3")
    header_page.cart_icon()
    mini_cart_page.checkout_btn()
    checkout_page = CheckoutPage(page)
    checkout_page.email_field("test@test.com")
    checkout_page.password_field("test_user123&")
    checkout_page.username_field("Loch")
    checkout_page.user_last_name_field("Mond")
    checkout_page.street_address_field("Marimaris, 27 -16")
    checkout_page.country_field("LT")
    checkout_page.user_city_field("Vilnius")
    checkout_page.province_field("Vilniaus Apskritis")
    checkout_page.user_phone_field("37067767678")
    checkout_page.user_zip_code_field("44352")
    expect(checkout_page.shipping_checkbox_btn).to_be_visible()
    checkout_page.shipping_method_checkbox_fixed()
    checkout_page.next_button()
    checkout_page.place_order_button()
    expect(checkout_page.page_title).to_have_text("Thank you for your purchase!")


    # count and filter the cheapest product by price range
    # prices = products_page.count_all_prices()
    # expect(len(prices) > 0, "No prices found")


    # page.get_by_role("link", name=" Set Ascending Direction").click()
    # page.get_by_role("link", name="Emma Leggings").first.click(button="right")
