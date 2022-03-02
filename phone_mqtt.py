from kivy.app import App 
from kivy.uix.button import Button



class myapp(App):
    def build(self):
        return Button(text = 'Кнопка')
    

if __name__ == "__main__":
    myapp().run()