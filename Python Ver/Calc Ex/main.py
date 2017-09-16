import kivy

kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class CalcGridLayout(GridLayout):
    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.see.text = str(eval(calculation))
            except Exception:
                self.see.text = "Error"


class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()


calcApp = CalculatorApp()
calcApp.run()
