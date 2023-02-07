import tensorflow as tf
# import numpy as np

from textual.app import ComposeResult
from textual.widgets import Static, Label
from textual.reactive import reactive

class StatsDisplay(Static):

    accuracyPercent = reactive(0)
    passed = reactive(0)
    failed = reactive(0)
    total = reactive(0)

    interpreter: tf.lite.Interpreter
    recognition_names: list[str]

    def __init__(self, model_path: str, recognition_names: list[str]) -> None:
        super().__init__()
        self.recognition_names = recognition_names
        self.interpreter = tf.lite.Interpreter(model_path)
        self.interpreter.allocate_tensors()
        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()

    def on_mount(self):
        self.add_class("processing")

    def compose(self) -> ComposeResult:
        yield Label(str(self.accuracyPercent) + "%", classes="percentage")
        yield Label(str(self.passed + self.failed) + "/" + str(self.total), classes="completed") 