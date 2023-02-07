from textual.app import ComposeResult
from textual.widgets import Static, Label

class StatsDisplay(Static):

    def on_mount(self):
        pass

    def compose(self) -> ComposeResult:
        yield Label("0%", classes="percentage")