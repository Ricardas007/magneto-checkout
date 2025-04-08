class LandingPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://magento.softwaretestingboard.com"

    def navigation(self):
        self.page.goto(self.url)