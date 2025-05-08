from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

class TaskWidget(BoxLayout):
    text = StringProperty()
   
    def remove_self(self):
        self.parent.remove_widget(self)

class TaskManager(BoxLayout):
    task_list = ListProperty([])

    def add_task(self):
        task_input = self.ids.task_input
        task_text = task_input.text.strip()
        if task_text:
            self.ids.task_box.add_widget(TaskWidget(text=task_text))
            task_input.text = ''

class TaskApp(App):
    def build(self):
        return TaskManager()

if __name__ == '__main__':
    TaskApp().run()