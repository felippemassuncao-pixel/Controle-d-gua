from rich import print
import random
niveis_reservatorio = [
    "nivel 1 - NIVEL CRITICO!",
    "nivel 2 - NIVEL BAIXO!",
    "nivel 3 - NIVEL MEDIO!",
    "nivel 4 - NIVEL ALTO!",
    "nivel 5 - NIVEL ALTO DEMAIS, ALERTA!"
]
def iniciação():
    print("[bold underline]INICIANDO MONITORAMENTO DO NIVEL DE ÁGUA[/bold underline]")
nivel_atual =  random.randint(1, 5)
iniciação()
if nivel_atual == 1:
    print(f"[red on white]{niveis_reservatorio[0]}[/red on white]")
elif nivel_atual == 2:
    print(f"[yellow on white]{niveis_reservatorio[1]}[/yellow on white]")
elif nivel_atual == 3:
    print(f"[green on white]{niveis_reservatorio[2]}[/green on white]")
elif nivel_atual == 4:
    print(f"[cyan on white]{niveis_reservatorio[3]}[/cyan on white]")
elif nivel_atual == 5:
    print(f"[blue on white]{niveis_reservatorio[4]}[/blue on white]")
