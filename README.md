# scrapyTestCandidate
<h2>Introdução</h2>
Para este desafio consiste em capturar todos os dados (Fakes) de um site de candidatos aprovados em concurso.<br>
Vale a pena mencionar que para este desafio possui duas páginas. Primeira possui uma lista de CPF e<br>
a segunda possui os dados do respectivo CPF.<br>
Para este desafio foi construido com a lib Scrapy em python e funciona da seguinte forma:<br>

* Capturar a lista de CPF's aprovados na primeira página
* Capturar nome e score do candidato
    
<br>
<h2>Como Funciona</h2>
Para executar esse teste precisa instalar a lib Scrapy, sqlite3, pymongo, pandas e flask.
O bot está no arquivo main.py, Ao executar iniciará a captura dos dados. Ao finalizar a captura
possui dois arquivos para visualizar o resultado da captura (teste_1.py e teste_2.py). <br>
O teste_1.py mostra algumas informações, como maior nota e menor nota, média da nota, etc.<br>
Já o teste_2.py disponibiliza algumas informações da captura numa API, status das flags e o que possui
em cada flag.<br>
<br>

Ao iniciar o bot, ele começara a captura na primeira página do teste `https://sample-university-site.herokuapp.com/approvals/1`
que contém uma lista com CPF's, o bot guardará essa lista de CPF's e então fará as requisições para
`https://sample-university-site.herokuapp.com/candidate/CPF`, logo em seguida fará a requisição 
para a próxima página "approvals/2" e assim por diante até a página 4672 que não comtém o botão next
e encerrará a captura do bot.<br>
<br>
