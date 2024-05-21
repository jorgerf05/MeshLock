import flet as ft
from controls.LockCard import LockCard


class Home(ft.View):

    def __init__(
        self, lock_name: str, lock_token: str, description: str, page: ft.Page
    ):
        super().__init__("/")
        self.controls.append(ft.SafeArea(ft.Text("Chapavision", size=45)))
        self.page = page
        self.column = ft.Column()
        self.add(lock_name, lock_token, description)
        self.controls.append(self.column)
        self.controls.append(
            ft.ElevatedButton(
                "Add a lock",
                on_click=lambda _: page.go("/addlock"),
            )
        )

    def add(self, lock_name, lock_token, description):
        self.column.controls.append(
            LockCard(
                lockname=lock_name,
                lock_token=lock_token,
                description=description,
                page=self.page,
            )
        )
