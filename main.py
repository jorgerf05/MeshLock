import flet as ft
from views.home import Home  # Main view class
from views.add_lock import AddLock  # View for adding a lock class


def main(page: ft.Page):
    page.title = "Chapavision"
    page.theme = ft.Theme(color_scheme_seed="blue")
    main_view = Home(
        lock_name="Laboratorio de Redes",
        lock_token="tokenn",
        description="Edificio 400",
        page=page,
    )

    def route_change(route):
        page.views.clear()
        page.views.append(main_view)

        if page.route == "/addlock":
            page.views.append(AddLock(main_view, page=page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
