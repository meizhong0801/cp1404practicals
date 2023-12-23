from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class ConvertMileToKmApp(App):
    """ ConvertMileToKmApp is a Kivy App for convert mile to Kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = int(value) * MILES_TO_KM
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "0.0"

    def handle_change(self, value_change):
        """ Handle calculation (could be button press or other call) to change the input number """
        try:
            current_value = int(self.root.ids.input_number.text)
            new_value = current_value + value_change
            self.root.ids.input_number.text = str(new_value)
        except ValueError:
            self.root.ids.input_number.text = "1"

    def handle_up(self):
        """ Handle increasing the input number by 1 """
        self.handle_change(1)

    def handle_down(self):
        """ Handle decreasing the input number by 1 """
        self.handle_change(-1)


ConvertMileToKmApp().run()


