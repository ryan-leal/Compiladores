# Compiladores
Repositório utilizado para desenvolvimento das atividades da disciplina de Construção de Compiladores no período 2023.2 da UFPB

Autores: 
Miguel Amadio de Oliveira
Ryan Matheus da Silva Leal

Para executar, basta abrir o terminal na pasta src, executar o arquivo .py passando como parametro o arquivo de texto a ser analisado

python grammar.py ..\inputs\input_Pascal01.pas

e

python automaton.py ..\inputs\input_AFD.pas

No caso do Automato, tivemos alguns problemas na abordagem inicial, o foco maior foi no da gramática, então o automato foi feito com menos tempo e sua lógica ainda estava em desenvolvimento, ficamos presos na ideia do buffer ser analisado pelo regex, porém, perdemos a informação do caractere atual do loop, fazendo com que um caractere fosse ignorado enquanto o regex analizava o buffer, acredito que com o tempo conseguimos finalizar.