from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.widget import Widget
from wrcloud.wrcloud import wrCloud
import json

Builder.load_file('menu.kv')


# class MyLayout(Widget):
#     textval = 'heii'
#     def selected(self, filename):
#         try:
#             print(filename[0])
#         except Exception:
#             pass
#
#     def on_click(self):
#         try:
#             api = wrCloud(api_key='5bef4651-dc35-42a3-aec4-179a0b0e8741')
#             print('API connected!')
#         except Exception as ex:
#             print('Something went wrorng', str(ex))
#         job = api.submit_job(filename="media-yoga.mp4", work_type=["annotated_media", "json"],
#                              options={'heads': True, 'est_3d': True, 'resolution_scale': 2}, url=False)
#         print(job)
#         api.wait_for_processed_job(job, interval=10, timeout=900)
#         status = api.get_job_status(job_id=job)
#         print(status)
#         while status != 'Processed':
#             status = api.get_job_status(job_id=job)
#             print(status)
#         results = api.get_json_result_as_dict(job)
#         print(json.dumps(results))
#         self.textval = json.dumps(results)

class MainApp(App):
    layout = BoxLayout(orientation="vertical")
    txt_input = TextInput(height=100)
    button = Button(size=(80, 80), text='Start')
    layout.add_widget(button)
    layout.add_widget(txt_input)

    def build(self):
        self.button.bind(on_press=self.on_click)
        return self.layout

    def on_click(self, instance):
        # self.txt_input.text = 'API connected!'
        try:
            api = wrCloud(api_key='5bef4651-dc35-42a3-aec4-179a0b0e8741')

            print('API connected!')
        except Exception as ex:
            print('Something went wrorng', str(ex))
        job = api.submit_job(filename="media-yoga.mp4", work_type=["annotated_media", "json"],
                             options={'heads': True, 'est_3d': True, 'resolution_scale': 2}, url=False)
        print(job)
        api.wait_for_processed_job(job, interval=10, timeout=900)
        status = api.get_job_status(job_id=job)
        print(status)
        #self.txt_input.text = 'Processing..'
        while status != 'Processed':
            status = api.get_job_status(job_id=job)
            print(status)
            # self.txt_input.text = status
        results = api.get_json_result_as_dict(job)
        print(json.dumps(results))
        # self.txt_input.bind(text=json.dumps(results))
        self.txt_input.text = str(json.dumps(results))


if __name__ == "__main__":
    app = MainApp()
    app.run()
