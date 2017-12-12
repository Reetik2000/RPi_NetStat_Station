import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class BottomOpts(AnchorLayout):

    def __init__(self, **kwargs):
        super(BottomOpts, self).__init__(**kwargs)
        bottomLeft = AnchorLayout(
            anchor_x='right', anchor_y='bottom'
        )

        routerBtn = Button(text='Router Details')
        bottomLeft.add_widget(routerBtn)

        self.add_widget(bottomLeft)


class MyApp(App):

    def build(self):
        return BottomOpts()



if __name__ == '__main__':
    MyApp().run()