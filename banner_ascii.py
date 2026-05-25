"""Gerador de banner ASCII da Mission Control AI."""

import pyfiglet
from rich.console import Console
from rich.align import Align
from rich.text import Text

console = Console()

linha1 = pyfiglet.figlet_format("Global Solution", font="slant")
linha2 = pyfiglet.figlet_format("Mission Control AI", font="slant")

console.print(Align.center(Text(linha1, style="bold magenta")))
console.print(Align.center(Text(linha2, style="bold cyan")))
console.print(
    Align.center(
        Text("2026.1 · Prompt Engineering and AI · FIAP", style="italic")
    )
)