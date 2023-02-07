from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

from flowstat.display import StatsDisplay

class FlowstatApp(App):
    
    CSS_PATH = "app.css"
    BINDINGS = [
        ('d', 'toggle_dark', 'Toggle dark mode'),
        ('q', 'quit', 'Quit')
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield StatsDisplay()
        yield Footer()
    
    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
    
    def action_quit(self) -> None:
        exit(0)