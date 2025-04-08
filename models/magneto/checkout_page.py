class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.user_email = page.get_by_role("textbox", name="email")
        self.user_passwd = page.get_by_role("textbox", name="Password")
        self.user_name = page.get_by_role("textbox", name="First Name")
        self.user_last_name = page.get_by_role("textbox", name="Last Name")
        self.user_address = page.get_by_role("textbox", name="Street Address: Line 1")
        self.user_city = page.get_by_role("textbox", name="City")
        self.user_country = page.get_by_label("Country")
        self.user_province = page.locator("select[name='region_id']")
        self.user_phone_number = page.get_by_role("textbox", name="Phone Number")
        self.zip_code = page.get_by_role("textbox", name="Zip/Postal Code")
        self.shipping_checkbox_btn = page.get_by_role("radio", name="Fixed Flat Rate")
        self.next_btn = page.get_by_role("button", name="Next")
        self.place_order_btn = page.get_by_role("button", name="Place Order")
        self.page_title = page.locator("h1.page-title")

    def email_field(self, email):
        self.user_email.fill(email)

    def password_field(self, password):
        self.user_passwd.fill(password)

    def username_field(self, username):
        self.user_name.fill(username)

    def user_last_name_field(self, last_name):
        self.user_last_name.fill(last_name)

    def street_address_field(self, address):
        self.user_address.fill(address)

    def user_city_field(self, city):
        self.user_city.fill(city)

    def province_field(self, province):
        self.user_province.select_option(province)

    def country_field(self, country):
        self.user_country.select_option(country)

    def user_phone_field(self, number):
        self.user_phone_number.fill(number)

    def user_zip_code_field(self, postal_code):
        self.zip_code.fill(postal_code)

    def shipping_method_checkbox_fixed(self):
        self.shipping_checkbox_btn.check()

    def next_button(self):
        self.next_btn.click()

    def place_order_button(self):
        self.place_order_btn.click()

#     page.get_by_role("button", name="Place Order").click()
#     page.get_by_text("Thank you for your purchase!").click()
#     page.get_by_text("000048116").click()