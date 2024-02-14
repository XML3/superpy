from rich.console import Console

class RichUtils:
    def __init__(self):
        self.console = Console()
        
    def print_styled_text(self, text, style=""):
        self.console.print(text, style=style)
        
    def print_table(self, header, rows):
        self.console.print(header)
        for row in rows:
            self.console.print(row)
            