# Verificação de Idade com Ano de Nascimento

Este projeto foi desenvolvido como parte do curso de Introdução à Programação oferecido pela Proz em parceria com a AWS no programa Talento Cloud. O código solicita o nome e o ano de nascimento do usuário e exibe a idade que ele completou ou completará em 2022. O objetivo é reforçar conceitos como manipulação de variáveis, entrada e validação de dados, estruturas de repetição e exceções em Python.

## Funcionalidade do Programa

O programa realiza as seguintes etapas:
1. Solicita ao usuário que insira seu nome completo.
2. Solicita que insira seu ano de nascimento, com a condição de estar entre 1922 e 2021.
3. Calcula a idade do usuário em 2022.
4. Exibe o nome do usuário e sua idade em 2022.

Se o usuário insere um valor inválido para o ano de nascimento (fora do intervalo de 1922-2021 ou não numérico), o programa exibe uma mensagem de erro e solicita novamente a entrada correta, garantindo que o processo continue até que o valor seja válido.

## Tecnologias e Conceitos Utilizados

- **Python**: linguagem de programação.
- **Entrada de Dados**: `input()`
- **Validação e Tratamento de Erros**: `try-except`
- **Estrutura de Repetição**: `while True`
- **Estruturas de Controle**: `if` para validar intervalos numéricos

## Exemplo de Uso

Ao executar o programa, o usuário verá algo assim:

```plaintext
Digite seu nome completo: João da Silva
Digite seu ano de nascimento (1922 - 2021): 2000
Seu nome é João da Silva e você tem 22 anos.
```

Se o usuário digitar um valor inválido, o sistema informará o erro:

```plaintext
Digite seu nome completo: Maria de Souza
Digite seu ano de nascimento (1922 - 2021): 2025
Por favor, digite um ano de nascimento entre 1922 e 2021.
```

## Autor

Caio Frederico, como parte do curso Talento Cloud da Proz e AWS.
