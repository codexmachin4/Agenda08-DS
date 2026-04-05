# 📊 Pesquisa de Satisfação - TudoWeb

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Licença](https://img.shields.io/badge/Licença-MIT-yellow)

## 📋 Sobre o Projeto

Este programa em Python foi desenvolvido para a empresa **TudoWeb** com o objetivo de coletar e analisar a opinião de clientes sobre o atendimento prestado. O sistema realiza uma pesquisa com **50 entrevistados** e exibe estatísticas consolidadas ao final.

## 🎯 Funcionalidades

- ✅ Coleta de **nome**, **idade** e **opinião** do cliente
- ✅ Validação de entrada (evita valores inválidos)
- ✅ Opções de avaliação:
  - `1` = EXCELENTE
  - `2` = BOM
  - `3` = RUIM
- ✅ Contabilização automática das respostas
- ✅ Exibição dos resultados:
  - Quantidade de respostas **EXCELENTE**
  - Quantidade de respostas **RUIM**
 
## 🧠 Conceitos aplicados

    Estrutura de repetição (for)

    Estruturas condicionais (if, elif, else)

    Contadores acumuladores

    Tratamento de exceções (try/except)

    Laço de validação (while)

    Entrada e saída de dados

    Programação procedural

## 🔎 Estratégia de validação adotada

O projeto utiliza try/except para garantir que o usuário digite apenas números válidos (1, 2 ou 3) para a opinião.

A validação funciona da seguinte forma:

    O programa tenta converter a entrada para inteiro usando int()

    Se o usuário digitar um valor não numérico (como letras), o except ValueError é acionado

    Se o valor estiver fora do intervalo permitido (1 a 3), o programa solicita novamente

    O loop while True só é interrompido quando uma opção válida é informada

Isso garante a integridade dos dados coletados sem que o programa seja interrompido por erros de entrada.
