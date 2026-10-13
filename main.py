from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.graphics import Color, Ellipse, Rectangle

class GlowingUI(BoxLayout):
    def __init__(self, **kwargs):
        super(GlowingUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20

        # Background color (Dark modern theme)
        with self.canvas.before:
            Color(0.05, 0.05, 0.1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Title Label
        self.title_label = Label(text="Taha AI Active", font_size=28, color=(1, 1, 1, 1))
        self.add_widget(self.title_label)

        # Glowing Circle Layout
        self.glow_layout = BoxLayout(size_hint=(None, None), size=(200, 200), pos_hint={'center_x': 0.5})
        with self.glow_layout.canvas.before:
            self.glow_color = Color(0, 0.8, 1, 0.6)
            self.circle = Ellipse(size=(150, 150), pos=(25, 25))
        self.add_widget(self.glow_layout)

        # Start Glowing Animation
        self.start_glow_animation()

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def start_glow_animation(self):
        anim = Animation(size=(190, 190), duration=1) + Animation(size=(150, 150), duration=1)
        anim += Animation(size=(190, 190), duration=1) + Animation(size=(150, 150), duration=1)
        anim.repeat = True
        anim.start(self.circle)

class TahaAIApp(App):
    def build(self):
        return GlowingUI()

if __name__ == '__main__':
    TahaAIApp().run()
      
