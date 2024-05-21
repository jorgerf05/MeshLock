import flet as ft
from .home import Home


class AddLock(ft.View):
    def __init__(self, home: Home, page: ft.Page):
        super().__init__("/addlock")
        self.home = home
        self.page = page
        self.name_field = ft.TextField(label="Lock name")
        self.totp_field = ft.TextField(label="Lock TOTP token")
        self.description = ft.TextField(label="Description")

        self.controls.append(
            ft.AppBar(
                title=ft.Text("Add a lock"),
                bgcolor=ft.colors.SURFACE_VARIANT,
            )
        )
        self.controls.append(
            ft.Column(
                [
                    self.name_field,
                    self.totp_field,
                    self.description,
                    ft.ElevatedButton("Add", on_click=self.add_lock),
                ]
            ),
        )

    def add_lock(self, e):
        self.home.add(
            self.name_field.value, self.totp_field.value, self.description.value
        )
        self.page.go("/")
