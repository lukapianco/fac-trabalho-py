# Trabalho de Algoritmos e Lógica de Programação /<br> Sistema de Automação de Gestão de Peças

## Explicação do Funcionamento
Este é um protótipo em Python desenvolvido para automatizar a inspeção de qualidade em uma linha de montagem industrial. O sistema recebe dados das peças, como **ID, peso, cor, comprimento**, aprova ou reprova automaticamente com base em critérios de qualidade rigorosos, agrupa peças aprovadas em caixas com limite de 10 unidades e gera relatórios operacionais.

## Como Rodar o Programa
1. Abra o terminal na pasta do projeto.
2. Execute o comando: `python index.py`
3. Interaja com o terminal através do menu e opções que aparecerão.

## Exemplos de Entradas e Saídas
**Exemplo de Peça Aprovada:**
- ID: `01`
- Peso: `100` (Dentro do limite de 95g a 105g)
- Cor: `verde` (Cor permitida)
- Comprimento: `15` (Dentro do limite de 10cm a 20cm)
*Saída esperada:* "=> Peça APROVADA e armazenada."

**Exemplo de Peça Reprovada:**
- ID: `02`
- Peso: `90` (Fora do limite)
- Cor: `vermelho` (Cor inválida)
- Comprimento: `15`
*Saída esperada:* "=> Peça REPROVADA e registrada." (Aparecerão os motivos de falha de peso e cor no relatório).
