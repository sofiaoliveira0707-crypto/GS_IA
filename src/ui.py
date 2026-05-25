"""Interface CLI estilo Claude Code."""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import pyfiglet
from datetime import datetime

console = Console()

session = PromptSession(
    style=Style.from_dict({
        "prompt": "#06B6D4 bold"
    })
)

def show_banner():
    """Mostra o banner inicial."""

    banner = pyfiglet.figlet_format(
        "Mission Control",
        font="slant"
    )

    console.print(Text(banner, style="bold cyan"))

    console.print(
        Panel.fit(
            "Sistema de monitoramento ambiental via IA.\n"
            "Use /help para comandos.\n"
            "Modelo: gpt-oss:120b",
            title="◆ ENVIROSAT",
            border_style="cyan"
        )
    )

def show_response(text):
    """Mostra resposta da IA."""

    horario = datetime.now().strftime("%H:%M")

    console.print(
        Panel(
            text,
            title="◆ Mission Control",
            subtitle=horario,
            border_style="cyan"
        )
    )

def run_cli(engine):

    show_banner()

    if not engine.is_ready():
        console.print(
            "⚠ Engine status: AGUARDANDO IMPLEMENTAÇÃO\n",
            style="yellow"
        )

    while True:

        try:
            user_input = session.prompt("❯ ").strip()

        except (KeyboardInterrupt, EOFError):
            break

        if not user_input:
            continue

        if user_input == "/exit":
            break

        if user_input == "/help":

            console.print("""
/help
/status
/about
/clear
/exit
            """)

            continue

        if user_input == "/status":

            show_response(
                engine.status_snapshot()
            )

            continue

        if user_input == "/clear":

            console.clear()
            show_banner()

            continue

        resposta = engine.analyze(user_input)

        show_response(resposta)