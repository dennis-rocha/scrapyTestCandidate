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

<h2>Requisitos</h2>

- Criar um serviço usando uma dessas linguagens: GO, Python, Java, C#, Javascript/Typescript (NodeJS), 
    PHP, Dart, Rust que capture a lista de pessoas listadas como aprovadas em um vestibular (dados fictícios) e que são 
    disponibilizadas no seguinte site `https://sample-university-site.herokuapp.com/`.

- Este serviço deve persistir em um banco de dados (pode ser um MySQL, Postgres ou outro banco de dados SQL que 
    você se sinta mais à vontade) todos os dados capturados/coletados do site (CPFs, nomes e scores).

- Deve-se fazer o split dos dados em colunas no banco de dados. Obs: pode ser feito diretamente no serviço ou em sql.

- Realizar higienização dos dados após persistência (sem acento, maiúsculas, etc).

- Validar os CPFs contidos (válidos e não válidos numericamente).

- Utilização de melhores práticas de desenvolvimento (nomenclatura, funções, classes, testes, etc);

- Utilização dos recursos mais recentes das linguagens;

- Boa organização lógica e documental (readme, comentários, etc);

- Cobertura de todos os requisitos;

- Performance na execução da captura;
