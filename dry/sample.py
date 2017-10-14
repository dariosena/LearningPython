def nav_menu():
    print('<a href="#">Home</a>')
    print('<a href="#">About</a>')
    print('<a href="#">Contact</a>')


def header():
    print('<div class="header">')
    nav_menu()
    print('</div>')


def footer():
    print('<div class="footer">')
    nav_menu()
    print('</div>')


def homePage():
    header()
    print('<p>Welcome to our Home Page</p>')
    footer()


def aboutPage():
    header()
    print('<p>Welcome to our About Page</p>')
    footer()


def contactPage():
    header()
    print('<p>Welcome to our Contact Page</p>')
    footer()


homePage()
