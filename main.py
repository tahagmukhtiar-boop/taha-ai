from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class TahaAIApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Chat history display
        self.chat_history = Label(text="Taha AI Initialized...\n", size_hint_y=None, halign='left', valign='top')
        self.chat_history.bind(texture_size=self.chat_history.setter('texture_size'))
        
        scroll = ScrollView(size_hint=(1, 0.8))
        scroll.add_widget(self.chat_history)
        root.add_widget(scroll)
        
        # Input layout
        input_layout = BoxLayout(size_hint=(1, 0.1), spacing=10)
        self.user_input = TextInput(hint_text="Yahan message likhein...", multiline=False)
        send_btn = Button(text="Send", size_hint_x=0.3)
        send_btn.bind(on_press=self.process_message)
        
        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_btn)
        root.add_widget(input_layout)
        
        return root

    def process_message(self, instance):
        text = self.user_input.text.strip()
        if not text:
            return
        
        self.chat_history.text += f"\nUser: {text}\n"
        
        # Simple AI response & command logic
        if "hello" in text.lower():
            response = "Taha AI: Hello! Main aapki kya madad kar sakta hoon?"
        elif "open" in text.lower():
            response = f"Taha AI: '{text}' command receive ho gayi hai."
        else:
            response = f"Taha AI: Aapne kaha '{text}'."
            
        self.chat_history.text += f"{response}\n"
        self.user_input.text = ""

if __name__ == '__main__':
    TahaAIApp().run()
        
