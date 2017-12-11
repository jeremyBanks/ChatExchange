from ._base import ParseHTML


class NavBar(ParseHTML):
    def __init__(self, page):
        super().__init__(page)

        topbar ,= self._dom.cssselect('.topbar-links')
        user_link ,= topbar.cssselect('a[href^=/users/]')[:1] or [None]
        if user_link:
            self.me_user_id = int(user_link.get('href').partition('/users/')[2].partition('/')[0])
        else:
            self.me_user_id = None
