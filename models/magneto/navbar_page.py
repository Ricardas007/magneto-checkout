class NavbarPage:

    def __init__(self, page):
        self.page = page
        self.men_menu_btn= page.get_by_role("menuitem", name=" Men")
        self.tops_menu_btn = page.get_by_role("menuitem", name=" Tops")
        self.hoodies_and_sweatshirts_menu_btn = page.get_by_role("menuitem", name="Hoodies & Sweatshirts")
        self.women_menu_btn = page.get_by_role("menuitem", name=" Women")
        self.bottom_menu_btn = page.get_by_role("menuitem", name=" Bottoms")
        self.womens_pants_menu = page.get_by_role("menuitem", name="Pants")

    def hover_over_men(self):
        # self.men_menu_btn.wait_for(state="visible", timeout=500)
        self.men_menu_btn.hover()
        # self.tops_menu_btn.wait_for(state="visible")
        self.tops_menu_btn.hover()
        # self.hoodies_and_sweatshirts_menu_btn.wait_for(state="visible")
        self.hoodies_and_sweatshirts_menu_btn.click()

    def hover_over_women(self):
        self.women_menu_btn.hover()
        self.bottom_menu_btn.hover()
        self.womens_pants_menu.click()
