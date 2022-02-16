# Desafios IDwall

Aqui estão os desafios para a primeira fase de testes de candidatos da IDwall.
Escolha em qual linguagem irá implementar (a não ser que um de nossos colaboradores lhe instrua a utilizar uma linguagem específica).

Não há diferença de testes para diferentes níveis de profissionais, porém o teste será avaliado com diferentes critérios, dependendo do perfil da vaga.

1. [Manipulação de strings](https://github.com/idwall/desafios/tree/master/strings)
2. [Crawlers](https://github.com/idwall/desafios/tree/master/crawlers)

## Rodar o desafios do crawler
Você deve ter instalado em sua maquina *docker, docker-compose, makefile*
`make build
 make up
 make tests
 make reddit_search category=cat score=5000
 make down
`
## Desafio das strings
Você deve ter instalado em sua maquina *python3+*
`python strings/string_formatter.py {input_file_path}
 python strings/string_formatter.py {input_file_path} --justify=True
 python strings/string_formatter.py {input_file_path} --limit=50
`
### Extras

- Descreva o processo de resolução dos desafios;
- Descreva como utilizar a sua solução;
- Tratamento de erros e exceções. Fica a seu critério quais casos deseja tratar e como serão tratados;
- Testes unitários ou de integração;
- Use o Docker.

## Carreira IDwall

Caso queira mais detalhes de como trabalhamos, quais são nossos valores e ideais, confira a página [Carreira IDwall](https://idwall.co/carreira) e mesmo que seu perfil não esteja listado nas vagas em aberto, lhe encorajamos a mandar seu CV! Valorizamos bons profissionais sempre e gostamos de manter contato com gente boa.

Boas implementações! 🎉
