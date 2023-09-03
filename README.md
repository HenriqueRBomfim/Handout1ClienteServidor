# Projeto 1A GetIt
Primeiro projeto da disciplina Tecnologias Web o 4º Semestre de Engenharia da Computação no Insper

Fiz a página de erro com o nome erro.html, ela é chamada pela função code_404 caso a requisição seja para uma página que não existe. Para simular sua existência, basta ir na URL e mudar de "localhost:8080" para "localhost:8080/qualquercoisaquenaosejaeditoudeleteouapagartudo".

Para conseguir o A+, fiz um botão para apagar todas as anotações. Ele fica abaixo das notas em uma posição visualmente agradável e, ao clicar nele, uma requisição do tipo apagartudo é enviada, chamando a função apagartudo() que pega o id de todas as notas existentes e apaga uma por uma. Como é uma funcionalidade extra, suponho que conta para o A+.
