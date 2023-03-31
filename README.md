# WJ-Gerador-de-Senhas

## O projeto foi dividido em 3 arquivos:
- main.py onde está a interface;
- funcoes.py com as funcoes;
- style.css com estilo do projeto;

## Módulos e bibliotecas usadas:
- PyQt6 para criar a interface
- Módulo String e Random para fazer um script personalizado que gera sequencias de caracteres aleatórios.

## Principais problemas e soluções
No decorrer do projeto surgiram alguns problemas, tais como:
### WordWrap do label nao funcionava como o desejado (quebrando a linha antes de chegar no final);
- Usei "\n".join para quebrar a string a cada x caracteres. Para funcionar melhor, mudei a fonte para uma Monospace.

### Deixar o campo 'tamanho da senha' em branco ou inserir um valor não inteiro ou não marcar nenhuma opção de caracteres gerava erro;
- Resolvi usando if's.
