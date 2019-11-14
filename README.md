# WebBot

Projeto Integrador do curso de Banco de Dados da Fatec-SJC 1º Semestre 2019.

O objetivo do projeto é que um grupo de alunos desenvolva uma aplicação em que 
seja utilizado um WebBot desenvolvido pelo grupo, usando o na solução de um 
problema proposto pelo grupo.


********* Objetivo ********* 

Desenvolver um web bot que faça uma raspagem de dados em um site, coletando dados 
referentes as despesas gastas por políticos de cargo eletivo, coletando informações 
que serão arquivadas, onde as mesmas serão desmembradas em quanto cada tipo de despesa 
consumiu do valor pago em impostos pelo contribuinte.


*********  Público Alvo ********* 

As informações podem ser acessadas pela imprensa, com fim de divulgação 
em seus veículos de comunicação, por associações que fazem um trabalho independente 
de fiscalização dos órgãos públicos e pela população em geral, com o intuito de 
cobrar atitudes mais corretas de políticos que tiverem despesas excessivas.


********* Finalidade ********* 

Tornar mais acessível a população informações que podem ajudá-los a 
pressionar os políticos a trabalharem em causas de interesse popular e colaborar 
com órgãos de segurança pública, como a polícia federal e o judiciário por exemplo, 
a identificar possíveis crimes vinculados a corrupção que podem ser identificados 
através de valores anormais ou alguma outra irregularidade, como improbidade administrativa 
e lavagem de dinheiro.


********* Requisitos ********* 

- Desenvolver um programa em linguagem Python que faça a coleta de dados em um site 
que disponibilize as informações necessarias;
- Reunir os valores coletados em um banco de dados ou em forma de tabelas;
- Organizar as informações em categorias a serem definidas.
- Listar os dados de forma estatística com o objetivo de identificar os principais
focos de onde se precisa trabalhar para que os recursos públicos sejam utilizados 
de forma mais eficiente.

********* Desenvolvimento *********

Front End:
- Programa desenvolvido nas linguagens Html, Css e Javascript
- A estrutura do Html será utilizada para criar a interface que será utilizada pelo usuário
- Alguns recursos de Css serão utilizados para melhorar a aparência da página e definir o alinhamento e tamanho de fonte do que será mostrado pela aplicação
- Os recursos do Javascript terão funções de redirecionamento no clique dos botões ou na escolha de alguma opção e de associar essa escolha à parte correspondente do programa

Back End:
- Programa desenvolvido em linguagem Python
- É necessário a instalação das bibliotecas request, pandas e matplotlib
- A biblioteca request fará a raspagem de dados através da api dos sites do Portal da Transparência e dos dados abertos da câmara dos deputados
- As informações obtidas na raspagem serão armazenadas em um documento csv
- Serão inseridas funções para que os valores listados sejam ordenados e apareceram para o usuário de acordo com o critério de pesquisa que ele escolher
- Os recursos da biblioteca Matplotlib serão utilizados para que o usuário possa escolher se os resultados serão mostrados em forma de tabela ou de gráfico.



