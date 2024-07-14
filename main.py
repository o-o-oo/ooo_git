from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFloatingActionButton
import math


class MyApp(MDApp):
    def __init__(self):
        super().__init__()
        self.screen = None
        self.tooth_input = None
        self.tooth_output = None
        self.inches_output = None
        self.disto_output = None
        self.distoin_output = None
        self.distomm_output = None

    def calc(self, *args):
        try:
            teeth = int(self.tooth_input.text)
            inches = teeth * .125
            distortion = (inches / math.pi - .124) / (inches / math.pi)
            disto_inches = inches * distortion
            disto_mm = disto_inches * 25.4
        except ValueError:
            self.tooth_input.text = ''
            self.tooth_output.text = ''
            self.inches_output.text = ''
            self.disto_output.text = ''
            self.distoin_output.text = ''
            self.distomm_output.text = ''
        else:
            self.tooth_output.text = f'{teeth}T'
            self.inches_output.text = f'{inches:.3f}"'
            self.disto_output.text = f'{distortion:.2%}'
            self.distoin_output.text = f'{disto_inches:.3f}"'
            self.distomm_output.text = f'{disto_mm:.2f}mm'

    def build(self):
        self.screen = MDScreen(md_bg_color='black')

        md_box_main = MDBoxLayout(orientation='vertical',
                                  md_bg_color='black',
                                  padding='40dp',
                                  )

        md_float_one = MDFloatLayout(md_bg_color='black')
        self.tooth_input = MDTextField(mode='rectangle',
                                       text='',
                                       hint_text='Tooth Size',
                                       icon_left='magnify',
                                       line_color_normal=(0, 122 / 255.0, 1, 1),
                                       line_color_focus=(0, 122 / 255.0, 1, 1),
                                       text_color_normal='white',
                                       text_color_focus='white',
                                       icon_left_color_normal='white',
                                       icon_left_color_focus='white',
                                       hint_text_color_normal=(0, 122 / 255.0, 1, 1),
                                       hint_text_color_focus=(0, 122 / 255.0, 1, 1),
                                       size_hint_x=0.6,
                                       pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       )
        md_float_one.add_widget(self.tooth_input)

        md_float_two = MDFloatLayout(md_bg_color='black')
        md_float_two.add_widget(MDFloatingActionButton(icon='language-python',
                                                       theme_icon_color='Custom',
                                                       icon_color='white',
                                                       md_bg_color=(0, 122/255.0, 1, 1),
                                                       pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                                       on_release=self.calc,
                                                       ))

        md_float_three = MDFloatLayout(md_bg_color='black')
        self.tooth_output = MDTextField(mode='rectangle',
                                        text='',
                                        hint_text='Tooth Size',
                                        icon_left='tooth-outline',
                                        line_color_normal=(0, 122 / 255.0, 1, 1),
                                        line_color_focus=(0, 122 / 255.0, 1, 1),
                                        text_color_normal='white',
                                        text_color_focus='white',
                                        icon_left_color_normal='white',
                                        icon_left_color_focus='white',
                                        hint_text_color_normal=(0, 122 / 255.0, 1, 1),
                                        hint_text_color_focus=(0, 122 / 255.0, 1, 1),
                                        size_hint_x=0.6,
                                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                        )
        md_float_three.add_widget(self.tooth_output)

        md_float_four = MDFloatLayout(md_bg_color='black')
        self.inches_output = MDTextField(mode='rectangle',
                                         text='',
                                         hint_text='Inches',
                                         icon_left='abacus',
                                         line_color_normal=(0, 122 / 255.0, 1, 1),
                                         line_color_focus=(0, 122 / 255.0, 1, 1),
                                         text_color_normal='white',
                                         text_color_focus='white',
                                         icon_left_color_normal='white',
                                         icon_left_color_focus='white',
                                         hint_text_color_normal=(0, 122 / 255.0, 1, 1),
                                         hint_text_color_focus=(0, 122 / 255.0, 1, 1),
                                         size_hint_x=0.6,
                                         pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                         )
        md_float_four.add_widget(self.inches_output)

        md_float_five = MDFloatLayout(md_bg_color='black')
        self.disto_output = MDTextField(mode='rectangle',
                                        text='',
                                        hint_text='Distortion',
                                        icon_left='label-percent-outline',
                                        line_color_normal=(0, 122 / 255.0, 1, 1),
                                        line_color_focus=(0, 122 / 255.0, 1, 1),
                                        text_color_normal='white',
                                        text_color_focus='white',
                                        icon_left_color_normal='white',
                                        icon_left_color_focus='white',
                                        hint_text_color_normal=(0, 122 / 255.0, 1, 1),
                                        hint_text_color_focus=(0, 122 / 255.0, 1, 1),
                                        size_hint_x=0.6,
                                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                        )
        md_float_five.add_widget(self.disto_output)

        md_float_six = MDFloatLayout(md_bg_color='black')
        self.distoin_output = MDTextField(mode='rectangle',
                                          text='',
                                          hint_text='Distorted Inches',
                                          icon_left='abjad-arabic',
                                          line_color_normal=(0, 122 / 255.0, 1, 1),
                                          line_color_focus=(0, 122 / 255.0, 1, 1),
                                          text_color_normal='white',
                                          text_color_focus='white',
                                          icon_left_color_normal='white',
                                          icon_left_color_focus='white',
                                          hint_text_color_normal=(0, 122 / 255.0, 1, 1),
                                          hint_text_color_focus=(0, 122 / 255.0, 1, 1),
                                          size_hint_x=0.6,
                                          pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                          )
        md_float_six.add_widget(self.distoin_output)

        md_float_seven = MDFloatLayout(md_bg_color='black')
        self.distomm_output = MDTextField(mode='rectangle',
                                          text='',
                                          hint_text='Distorted mm',
                                          icon_left='android',
                                          line_color_normal=(0, 122 / 255.0, 1, 1),
                                          line_color_focus=(0, 122 / 255.0, 1, 1),
                                          text_color_normal='white',
                                          text_color_focus='white',
                                          icon_left_color_normal='white',
                                          icon_left_color_focus='white',
                                          hint_text_color_normal=(0, 122 / 255.0, 1, 1),
                                          hint_text_color_focus=(0, 122 / 255.0, 1, 1),
                                          size_hint_x=0.6,
                                          pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                          )
        md_float_seven.add_widget(self.distomm_output)

        md_box_main.add_widget(md_float_one)
        md_box_main.add_widget(md_float_two)
        md_box_main.add_widget(md_float_three)
        md_box_main.add_widget(md_float_four)
        md_box_main.add_widget(md_float_five)
        md_box_main.add_widget(md_float_six)
        md_box_main.add_widget(md_float_seven)

        self.screen.add_widget(md_box_main)

        return self.screen


if __name__ == '__main__':
    MyApp().run()
