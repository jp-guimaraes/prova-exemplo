import random
from textwrap import dedent

def gerar_prova(aluno_nome="FULANO"):
    base = random.randint(5, 15)
    altura = random.randint(4, 12)
    area_correta = (base * altura) / 2

    # Gera 3 alternativas incorretas distintas da correta
    alternativas_erradas = set()
    while len(alternativas_erradas) < 3:
        erro = area_correta + random.choice([-8, -4, -2, 2, 4, 6])
        if erro != area_correta and erro > 0:
            alternativas_erradas.add(erro)
    alternativas = list(alternativas_erradas) + [area_correta]
    random.shuffle(alternativas)

    letras = ['A', 'B', 'C', 'D']
    letra_correta = letras[alternativas.index(area_correta)]

    latex = dedent(f"""
    \\documentclass[12pt]{{article}}
    \\usepackage[margin=2.5cm]{{geometry}}
    \\usepackage{{tikz}}
    \\usepackage{{amsmath}}
    \\usepackage{{multicol}}

    \\title{{Prova de Matemática - Geometria}}
    \\date{{}}
    \\begin{{document}}

    % Cabeçalho
    \\begin{{center}}
      \\Large \\textbf{{IFRN-CM}} \\\\
      \\large Prova de Matemática - Triângulos \\\\
      \\vspace{{0.5cm}}
      \\normalsize Nome: {aluno_nome} \\hfill Nota: \\underline{{\\hspace{{2cm}}}} \\\\
      \\vspace{{0.5cm}}
    \\end{{center}}

    \\vspace{{0.5cm}}

    \\textbf{{Fórmula da área do triângulo:}}
    \\[
    A = \\frac{{b \\cdot h}}{{2}}
    \\]
    onde \\( b \\) é a base e \\( h \\) é a altura do triângulo.

    \\vspace{{0.5cm}}

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

    \\vspace{{0.5cm}}

    \\textbf{{Qual é a área do triângulo?}}

    \\begin{{multicols}}{{2}}
    \\begin{{enumerate}}
    """)

    for i, alt in enumerate(alternativas):
        latex += f"  \\item $ {alt} \\, \\text{{cm}}^2 $\n"

    latex += dedent("""
    \\end{enumerate}
    \\end{multicols}

    \\newpage
    \\section*{Gabarito e Expectativa de Resposta (Uso do Professor)}
    """)

    latex += dedent(f"""
    \\textbf{{Questão 1}}

    Dados:
    \\[
    \\text{{base }} b = {base} \\text{{ cm}}, \\quad \\text{{altura }} h = {altura} \\text{{ cm}}
    \\]

    Cálculo da área:
    \\[
    A = \\frac{{b \\cdot h}}{{2}} = \\frac{{{base} \\cdot {altura}}}{{2}} = \\frac{{{base * altura}}}{{2}} = {area_correta} \\, \\text{{cm}}^2
    \\]

    Alternativa correta: \\textbf{{({letra_correta})}} \\( {area_correta} \\, \\text{{cm}}^2 \\)
    """)

    latex += "\n\\end{document}"

    return latex

# Salva a prova em um arquivo .tex
with open("prova_fulano.tex", "w", encoding="utf-8") as f:
    f.write(gerar_prova("FULANO"))
