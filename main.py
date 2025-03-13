import flet as ft
from Páginas.pag1 import home_view

def main(page: ft.Page):
    page.title = "Multi-View App"
    page.update()

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(home_view(page))
        elif page.route == "/about":
            pass
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)