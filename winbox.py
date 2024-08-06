# import asyncio
import flet as ft

class ChatApp:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)
        self.update_chat()

    def update_chat(self):
        self.chat_list.controls.append(ft.Text(self.messages[-1], size=16))
        self.chat_list.scroll = ft.ScrollMode.AUTO

    def build(self):
        return ft.Column(
            controls=[
                ft.ListView(
                    # # id="chat_list",
                    # scroll="auto",
                    auto_scroll=True,
                    width=400,
                    height=400,
                    padding=10,
                    # vertical_alignment="start",
                ),
                ft.Row(
                    controls=[
                        ft.TextField(
                            # id="input_message",
                            hint_text="Введите ваше сообщение",
                            width=300,
                        ),
                        ft.IconButton(
                            icon=ft.icons.SEND,
                            on_click=lambda e: self.send_message(),
                        ),
                    ],
                ),
            ],
            alignment="center",
        )

    def send_message(self):
        message = self.input_message.value.strip()
        if message:
            self.add_message(message)
            self.input_message.value = ""  # Очистить поле ввода
            self.input_message.focus()  # Сфокусироваться на поле ввода


def main(page: ft.Page):
    page.title = "Чат на Flet"
    page.vertical_alignment = ft.MainAxisAlignment.END

    chat_app = ChatApp()
    page.add(chat_app.build())

if __name__ == "__main__":
    ft.app(target=main)