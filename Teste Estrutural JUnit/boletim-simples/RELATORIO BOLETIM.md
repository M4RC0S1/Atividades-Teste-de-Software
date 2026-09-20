# Relatório: Teste Estrutural com JUnit (boletim-simples)

## 1. Objetivo
Escrever testes unitários em JUnit 5 para as classes `Boletim` e `Participacao` e medir a cobertura com o JaCoCo, buscando 100% de linhas, branches, métodos e classes.

## 2. Resultado da cobertura

| Métrica | Resultado |
|---|---|
| Instruções | 0 perdidas de 57 (100%) |
| Branches | 0 perdidos de 12 (100%) |
| Linhas | 0 perdidas de 20 |
| Métodos | 0 perdidos de 6 |
| Classes | 0 perdidas de 2 |
| Complexidade ciclomática (Cxty) | 12 |

Os 6 métodos são os 4 escritos (`calcularMedia`, `verificarSituacao`, `contarAprovados`, `calcularPontos`) mais os 2 construtores padrão, que o JaCoCo também conta.

## 3. O que cada percentual significa
- **Instruções e linhas:** quanto do código foi executado pelos testes.
- **Branches:** quantas alternativas (verdadeira e falsa) de cada decisão (`if` e condição do `for`) foram exercitadas.
- **Métodos:** quantos métodos foram chamados ao menos uma vez.
- **Classes:** quantas classes tiveram algum método executado.
- **Complexidade ciclomática:** número de caminhos independentes do código (decisões + 1 por método).

## 4. Complexidade e caminhos por método

| Método | Cxty | Caminhos e entradas usadas |
|---|---|---|
| `Boletim()` | 1 | construtor padrão |
| `calcularMedia` | 1 | caminho único: médias exata, decimal e extremos (0 e 10) |
| `verificarSituacao` | 3 | média ≥ 7 (8 → APROVADO); ≥ 4 e < 7 (5 → RECUPERACAO); < 4 (2 → REPROVADO); limites 3.99, 4, 6.99, 7 |
| `contarAprovados` | 3 | zero iterações (array vazio); uma iteração; várias iterações, com aprovados e não aprovados |
| `Participacao()` | 1 | construtor padrão |
| `calcularPontos` | 3 | duas decisões independentes (tabela da seção 5) |
| **Total** | **12** | |

Os 12 branches vêm de 4 em `verificarSituacao` (2 `if` × 2 saídas), 4 em `contarAprovados` (o `for` e o `if`, com 2 saídas cada) e 4 em `calcularPontos` (2 `if` × 2 saídas).

## 5. Caminhos de `calcularPontos`

| entregou | participou | pontos | caminho |
|---|---|---|---|
| true | true | 3 | os dois `if` verdadeiros |
| true | false | 2 | só o primeiro `if` verdadeiro |
| false | true | 1 | só o segundo `if` verdadeiro |
| false | false | 0 | os dois `if` falsos |

Dois testes (true/true e false/false) já dariam 100% de branches, mas deixariam duas combinações sem execução. Por isso foram testadas as quatro, com testes individuais e um `@ParameterizedTest`.

## 6. Estratégia dos testes
- Limites das faixas (4 e 7) testados no valor exato e logo abaixo ou acima, porque erros de `>=` contra `>` aparecem ali.
- `double` comparado com tolerância: `assertEquals(esperado, obtido, 0.0001)`.
- Laço com zero, uma e várias iterações.
- `@ParameterizedTest` com `@CsvSource` para classificações e combinações de booleanos.

## 7. Conclusão
A cobertura chegou a 100% em todas as métricas, mas isso só mostra que o código foi executado. Quem confirma que as respostas estão certas são as asserções; cobertura e asserções se complementam, e um não substitui o outro.
