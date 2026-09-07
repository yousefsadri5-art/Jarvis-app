from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import os

class JarvisApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # عنوان برنامه
        self.label = Label(text="J.A.R.V.I.S. Core Online, Sir.", font_size=20, color=(0, 1, 1, 1))
        root.add_widget(self.label)
        
        # دکمه باز کردن یوتیوب
        btn_yt = Button(text="Open YouTube", background_color=(1, 0, 0, 1))
        btn_yt.bind(on_press=self.open_youtube)
        root.add_widget(btn_yt)
        
        # دکمه چراغ قوه
        btn_torch = Button(text="Toggle Flashlight", background_color=(0, 1, 0, 1))
        btn_torch.bind(on_press=self.toggle_torch)
        root.add_widget(btn_torch)
        
        # دکمه خروج
        btn_exit = Button(text="Shutdown", background_color=(0.5, 0.5, 0.5, 1))
        btn_exit.bind(on_press=self.stop)
        root.add_widget(btn_exit)
        
        return root

    def open_youtube(self, instance):
        self.label.text = "Opening YouTube, Sir."
        os.system("am start --user 0 -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -n com.google.android.youtube/com.google.android.apps.youtube.app.WatchWhileActivity")

    def toggle_torch(self, instance):
        self.label.text = "Toggling Flashlight, Sir."
        os.system("termux-torch on")

if __name__ == '__main__':
    JarvisApp().run()
  
