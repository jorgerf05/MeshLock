import flet as ft
import pyotp
import qrcode
from io import BytesIO
import base64


class LockCard(ft.Card):
    def __init__(self, lockname: str, lock_token: str, description: str, page: ft.Page):
        super().__init__()
        self.lockname = lockname
        self.lock_token = lock_token
        self.description = description
        self.totp = pyotp.TOTP(self.encode_utf8_to_base32(self.lock_token))
        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.LOCK),
                        title=ft.Text(self.lockname),
                        subtitle=ft.Text(self.description),
                    ),
                    ft.Row(
                        [ft.TextButton("Unlock", on_click=self.show_bs)],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
        self.bs = ft.BottomSheet(
            ft.Container(
                ft.Column(
                    [
                        ft.Text("This is sheet's content!"),
                        ft.ElevatedButton("Close bottom sheet", on_click=self.close_bs),
                    ],
                    tight=True,
                ),
                padding=10,
            ),
            open=False,
        )
        page.overlay.append(self.bs)
        page.add(ft.ElevatedButton("Display bottom sheet", on_click=self.show_bs))

    def test(self, _):
        print(self.totp.now())

    def get_qr(self, token: str):
        qr = qrcode.make(token)
        buffer = BytesIO()
        qr.save(buffer)
        encoded_image = base64.b64encode(buffer.getvalue())
        base64_string_image = encoded_image.decode("utf-8")

        return base64_string_image

    def show_bs(self, e):
        now = self.totp.now()
        img_str = self.get_qr(token=now)
        self.bs.content = ft.Image(src_base64=img_str)
        self.bs.open = True
        self.bs.update()

    def close_bs(self, e):
        self.bs.open = False
        self.bs.update()

    def encode_utf8_to_base32(self, utf8_string):
        # Convert the UTF-8 string to bytes
        utf8_bytes = utf8_string.encode("utf-8")
        # Encode the bytes to Base32
        base32_bytes = base64.b32encode(utf8_bytes)
        # Convert the Base32 bytes back to a string
        base32_string = base32_bytes.decode("utf-8")
        return base32_string
