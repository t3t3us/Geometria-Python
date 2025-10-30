Transformações Geométricas em Computação Gráfica com Python

📜 Descrição

Este projeto é uma demonstração prática dos conceitos fundamentais de transformações geométricas 2D (Translação, Escala e Rotação) aplicados em um contexto de Computação Gráfica. Utilizando Python e as bibliotecas NumPy e Matplotlib, o script define uma forma geométrica (um triângulo) e a submete a diversas transformações, visualizando o resultado original e os transformados em um único gráfico.

Este código foi desenvolvido como solução para a Atividade Prática 2 da disciplina de Computação Gráfica.

✨ Conceitos Demonstrados

O script implementa e visualiza as seguintes transformações:

    Translação: Desloca o objeto em uma direção específica no plano (eixos X e Y) através da soma de vetores.

    Escala: Altera as dimensões do objeto, aumentando-o ou diminuindo-o de forma uniforme ou não uniforme em relação à origem.

    Rotação: Gira o objeto em torno da origem por um determinado ângulo.

    Transformação Combinada: Demonstra o conceito de pipeline gráfico, onde múltiplas transformações são aplicadas em sequência (neste caso, uma rotação seguida por uma translação), evidenciando que a ordem das operações é crucial para o resultado final.

🛠️ Tecnologias Utilizadas

    Python 3: Linguagem de programação principal.

    NumPy: Utilizada para cálculos matemáticos eficientes com matrizes e vetores, que são a base das transformações.

    Matplotlib: Utilizada para a visualização 2D dos resultados, plotando as formas geométricas no plano cartesiano.

🚀 Como Executar

    Clone o repositório:
    [Bash](https://github.com/t3t3us/Geometria-Python)

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Instale as dependências: Certifique-se de ter o Python 3 instalado. Em seguida, instale as bibliotecas necessárias:
Bash

pip install numpy matplotlib

Execute o script: No terminal, execute o seguinte comando:
Bash

    python3 main.py

📊 Resultado Esperado

Ao executar o script, uma janela do Matplotlib será exibida, mostrando um gráfico com cinco triângulos:

    Azul: O triângulo original.

    Verde: O triângulo após ser transladado.

    Vermelho: O triângulo após ser escalado.

    Magenta: O triângulo após ser rotacionado.

    Ciano: O triângulo após a aplicação de uma transformação combinada (rotação + translação).

🔧 Como Customizar

Você pode facilmente experimentar com o código para aprofundar seu aprendizado:

    Mudar a forma: Altere as coordenadas da variável triangulo no início do código para criar outras formas, como polígonos irregulares.

    Alterar os valores: Modifique os parâmetros passados para as funções transladar(), escalar() e rotacionar() para ver como os resultados mudam.

    Combinar outras transformações: Crie novas sequências de transformações para observar diferentes resultados no pipeline.
