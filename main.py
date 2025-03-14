import flet as ft
from Páginas.pag1 import login
from Páginas.pag2 import page_inicial
#from Páginas.pag3 import add

def main(page: ft.Page):
    page.title = "Multi-View App"
    page.update()
    page.route='/pag_inicial'

    def route_change(route):
        page.views.clear()
        if page.route == "/login":
            page.views.append(login(page))
        elif page.route == "/pag_inicial":
            page.views.append(page_inicial(page))
        #elif page.route == "/add_item":
            #page.views.append(add(page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)