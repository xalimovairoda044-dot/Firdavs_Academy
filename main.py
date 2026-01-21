from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import webbrowser

# Mobil oyna rangini oq qilish
Window.clearcolor = (1, 1, 1, 1)

class FirdavsMobile(App):
    def build(self):
        self.title = "Firdavs Xabibullayev Academy"
        
        # Asosiy konteyner
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Sarlavha
        title = Label(
            text="FIRDAVS ACADEMY", 
            font_size='32sp', 
            bold=True, 
            color=(0.1, 0.45, 0.9, 1),
            size_hint_y=None,
            height=80
        )
        layout.add_widget(title)

        # Balans (Haqiqiy reyting asosi)
        self.coins = 0
        self.balance_lbl = Label(
            text=f"Hisobingiz: {self.coins} 💰", 
            font_size='22sp', 
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.balance_lbl)

        # Ijtimoiy tarmoqlar
        btn_yt = Button(text="YouTube", background_color=(1, 0, 0, 1), size_hint_y=None, height=60)
        btn_yt.bind(on_release=lambda x: webbrowser.open("https://www.youtube.com/channel/UCjxWgZ-x8xHQc-V0gNyccBA"))
        layout.add_widget(btn_yt)

        btn_web = Button(text="Mening Vebsaytim", background_color=(0, 0.7, 0.3, 1), size_hint_y=None, height=60)
        btn_web.bind(on_release=lambda x: webbrowser.open("https://www.canva.com/design/DAG9iFdux8M/sBNayIUw46hYk7RKAmXXYQ/edit"))
        layout.add_widget(btn_web)

        # Darslar qismi
        lbl_lessons = Label(text="Darslar ro'yxati:", color=(0.5, 0.5, 0.5, 1), size_hint_y=None, height=40)
        layout.add_widget(lbl_lessons)

        scroll = ScrollView()
        lessons_list = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        lessons_list.bind(minimum_height=lessons_list.setter('height'))

        # Darslarni yaratish
        for i in range(1, 16):
            btn = Button(
                text=f"{i}-Dars: Dasturlashni o'rganish", 
                size_hint_y=None, 
                height=70,
                background_normal='',
                background_color=(0.9, 0.9, 0.9, 1),
                color=(0,0,0,1)
            )
            lessons_list.add_widget(btn)

        scroll.add_widget(lessons_list)
        layout.add_widget(scroll)

        return layout

if __name__ == "__main__":
    FirdavsMobile().run()