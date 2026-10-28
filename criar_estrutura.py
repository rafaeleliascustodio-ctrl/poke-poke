#!/usr/bin/env python3
"""
Gera a estrutura de pastas do projeto Unity (clone de Pokémon FireRed).
Compatível com Windows, macOS e Linux.
"""

from pathlib import Path

# Diretório atual (onde o script é executado)
RAIZ_PROJETO = Path.cwd()
PASTA_ASSETS = RAIZ_PROJETO / "Assets"

# Caminhos relativos à raiz do projeto
PASTAS = [
    "Assets/_Projeto/Animations",
    "Assets/_Projeto/Audio/BGM",
    "Assets/_Projeto/Audio/SFX",
    "Assets/_Projeto/Prefabs",
    "Assets/_Projeto/Scenes",
    "Assets/_Projeto/Scripts/Battle",
    "Assets/_Projeto/Scripts/Gameplay",
    "Assets/_Projeto/Scripts/Pokemon",
    "Assets/_Projeto/Sprites/UI",
    "Assets/_Projeto/Sprites/Overworld",
]

CONTEUDO_LEIA_ME = """\
ORGANIZAÇÃO DOS SCRIPTS
=======================

Para manter o projeto modular e fácil de manter, separe a lógica
nas seguintes subpastas:

Battle/
    Toda a lógica de batalha: sistema de turnos, cálculo de dano,
    efetividade de tipos, menus de luta, IA do oponente e fluxo
    de início/fim de combate.

Gameplay/
    Movimentação em grid do jogador e dos NPCs, detecção de colisão,
    interações com o cenário, encontros em grama alta, diálogos e
    transições entre cenas.

Pokemon/
    Dados dos Pokémon: espécies, status base, golpes, tipos,
    evolução, ScriptableObjects e classes de dados em geral.

Regra de ouro: evite dependências diretas entre as pastas. Se
Battle precisar de dados de um Pokémon, leia-os através das
classes de Pokemon/, nunca duplicando a informação.
"""


def main() -> None:
    print("=" * 50)
    print(" Gerador de estrutura Unity - Pokémon FireRed Clone")
    print("=" * 50)
    print(f"Diretório base: {RAIZ_PROJETO}\n")

    # Verifica se a pasta Assets já existe
    if PASTA_ASSETS.exists():
        print("[INFO] Pasta 'Assets' já existe (projeto Unity detectado).")
        print("       As novas pastas serão criadas dentro dela.\n")
    else:
        print("[INFO] Pasta 'Assets' não encontrada. Ela será criada agora.\n")

    criadas = []
    ja_existiam = []
    erros = []

    for caminho_relativo in PASTAS:
        pasta = RAIZ_PROJETO / caminho_relativo
        try:
            if pasta.exists():
                ja_existiam.append(caminho_relativo)
            else:
                pasta.mkdir(parents=True, exist_ok=True)
                criadas.append(caminho_relativo)
        except OSError as e:
            erros.append((caminho_relativo, e))

    # Cria o arquivo LEIA-ME.txt
    leia_me = RAIZ_PROJETO / "Assets" / "_Projeto" / "Scripts" / "LEIA-ME.txt"
    leia_me_status = None
    try:
        if leia_me.exists():
            leia_me_status = "já existia (mantido sem alterações)"
        else:
            leia_me.write_text(CONTEUDO_LEIA_ME, encoding="utf-8")
            leia_me_status = "criado"
    except OSError as e:
        erros.append(("Assets/_Projeto/Scripts/LEIA-ME.txt", e))

    # Relatório final
    if criadas:
        print("Pastas criadas com sucesso:")
        for c in criadas:
            print(f"  [OK] {c}")

    if ja_existiam:
        print("\nPastas que já existiam:")
        for c in ja_existiam:
            print(f"  [--] {c}")

    if leia_me_status:
        print(f"\nArquivo LEIA-ME.txt: {leia_me_status}")

    if erros:
        print("\nErros encontrados:")
        for caminho, erro in erros:
            print(f"  [ERRO] {caminho}: {erro}")
    else:
        print("\nEstrutura gerada com sucesso!")


if __name__ == "__main__":
    main()