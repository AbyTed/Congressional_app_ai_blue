from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

KV = """
ScreenManager:
    MenuScreen:
    SettingsScreen:

<MenuScreen>:
    name: 'menu'

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Menu'
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['menu', lambda x: None]]
        Widget:
        MDRaisedButton:
            text: "Go to Settings"
            pos_hint: {'center_x': 0.5}
            on_release: app.root.current = 'settings'
        Widget:

<SettingsScreen>:
    name: 'settings'

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Settings'
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['arrow-left', lambda x: app.root.current = 'menu']]
        Widget:
        MDLabel:
            text: "Settings Screen"
            halign: "center"
        Widget:
"""


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)


if __name__ == "__main__":
    MyApp().run()
