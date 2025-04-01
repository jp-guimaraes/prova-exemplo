from textwrap import dedent
import random
from pathlib import Path

# Lista de nomes extraída da imagem fornecida
nomes_alunos = [
    "Alex Monteiro",
    "Bruno Alencar",
    "Igor Menezes",
    "Lucas Tavares",
    "Wallace Martins",
    "Paula Andrade",
    "Cauê Ramos",
    "Cristina Vilela",
    "Dionísio Freitas",
    "Manuela Soares",
    "Thaís Cardoso",
    "Kaio Santana",
    "Gabriel Farias",
    "Alessa Moura",
    "Henrique Lemos",
    "Victor Almeida",
    "Augusto Ferreira",
    "Iran Costa",
    "Karla Siqueira",
    "Keila Mendes",
    "Lázaro Rocha",
    "Leandro Brito",
    "Cida Vasconcelos",
    "Clara Neves",
    "Vitória Luz",
    "Samuel Fonseca",
    "Carlos Eduardo",
    "William Lopes",
    "Kevyn Câmara",
    "Ramon Azevedo",
    "Thales Fernandes",
    "Beatriz Cunha",
    "Vitória Lima",
    "Yasmin Duarte",
    "Ícaro Henrique"
]


# Função para gerar conteúdo LaTeX da prova e da expectativa de resposta para um aluno
def gerar_conteudo_latex(aluno_nome):
    base = random.randint(5, 15)
    altura = random.randint(4, 12)
    area_correta = (base * altura) / 2

    # Gera alternativas erradas
    alternativas_erradas = set()
    while len(alternativas_erradas) < 3:
        erro = round(area_correta + random.choice([-8, -4, -2, 2, 4, 6]), 1)
        if erro != area_correta and erro > 0:
            alternativas_erradas.add(erro)

    alternativas = list(alternativas_erradas) + [area_correta]
    random.shuffle(alternativas)

    letras = ['A', 'B', 'C', 'D']
    letra_correta = letras[alternativas.index(area_correta)]

    # Corpo da prova
    prova = dedent(f"""
    % PROVA DE {aluno_nome}
    \\begin{{center}}
      \\Large \\textbf{{IFRN-CM}} \\\\
      \\large Prova de Matemática - Triângulos \\\\
      \\vspace{{0.5cm}}
      \\normalsize Nome: \\textbf{{{aluno_nome}}} \\hfill Nota: \\underline{{\\hspace{{2cm}}}} \\\\
      \\vspace{{0.5cm}}
    \\end{{center}}

    \\textbf{{Fórmula da área do triângulo:}}
    \\[
    A = \\frac{{b \\cdot h}}{{2}}
    \\]
    onde \\( b \\) é a base e \\( h \\) é a altura do triângulo.

    \\textbf{{1. (2,0 pts)}} Observe o triângulo abaixo, em que a base mede \\textbf{{{base} cm}} e a altura mede \\textbf{{{altura} cm}}. Calcule a área desse triângulo.

    \\begin{{center}}
    \\begin{{tikzpicture}}[scale=0.8]
      \\draw[thick] (0,0) -- ({base},0) -- (0,{altura}) -- cycle;
      \\draw ({base/2},-0.5) node {{{base} cm}};
      \\draw[dashed] (0,{altura}) -- (0,0);
      \\draw (-0.5,{altura/2}) node[rotate=90] {{{altura} cm}};
      \\filldraw (0,0) circle (2pt) node[below left]{{A}};
      \\filldraw ({base},0) circle (2pt) node[below right]{{B}};
      \\filldraw (0,{altura}) circle (2pt) node[above left]{{C}};
    \\end{{tikzpicture}}
    \\end{{center}}

    \\textbf{{Qual é a área do triângulo?}}

    \\begin{{multicols}}{{2}}
    \\begin{{enumerate}}
    """)

    for alt in alternativas:
        prova += f"  \\item $ {alt} \\, \\text{{cm}}^2 $\n"

    prova += dedent("""
    \\end{enumerate}
    \\end{multicols}
    \\newpage
    """)

    # Corpo da expectativa
    expectativa = dedent(f"""
    % EXPECTATIVA DE RESPOSTA DE {aluno_nome}
    \\section*{{Gabarito e Expectativa de Resposta - {aluno_nome}}}

    Dados:
    \\[
    \\text{{base }} b = {base} \\text{{ cm}}, \\quad \\text{{altura }} h = {altura} \\text{{ cm}}
    \\]

    Cálculo da área:
    \\[
    A = \\frac{{b \\cdot h}}{{2}} = \\frac{{{base} \\cdot {altura}}}{{2}} = {area_correta} \\, \\text{{cm}}^2
    \\]

    Alternativa correta: \\textbf{{({letra_correta})}} \\( {area_correta} \\, \\text{{cm}}^2 \\)

    \\newpage
    """)

    return prova, expectativa

# Inicializa conteúdo principal dos dois arquivos
inicio_documento = dedent(r"""
\documentclass[12pt]{article}
\usepackage[margin=2.5cm]{geometry}
\usepackage{tikz}
\usepackage{amsmath}
\usepackage{multicol}
\usepackage{parskip}
\begin{document}
""")

fim_documento = "\n\\end{document}"

# Acumuladores de LaTeX
conteudo_provas = inicio_documento
conteudo_gabaritos = inicio_documento

# Geração para todos os alunos
for nome in nomes_alunos:
    prova, expectativa = gerar_conteudo_latex(nome)
    conteudo_provas += prova
    conteudo_gabaritos += expectativa

conteudo_provas += fim_documento
conteudo_gabaritos += fim_documento

# Salva os arquivos .tex
Path("provas_alunos.tex").write_text(conteudo_provas, encoding="utf-8")
Path("expectativas_resposta.tex").write_text(conteudo_gabaritos, encoding="utf-8")


