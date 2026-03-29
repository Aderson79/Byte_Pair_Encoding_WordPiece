# Contexto do Projeto: Laboratório 6 - Tokenização (BPE & WordPiece)

Este documento serve como guia de referência e instruções para o desenvolvimento do Laboratório 6. O objetivo é implementar o algoritmo Byte Pair Encoding (BPE) do zero e explorar o WordPiece via Hugging Face.

---

## 🎯 Objetivos Principais

- **Implementar o motor de frequências (BPE):** Contagem de pares adjacentes em um corpus simulado.
- **Implementar o Loop de Fusão (Merges):** Atualizar o vocabulário unindo os pares mais frequentes.
- **Exploração Industrial:** Utilizar o `AutoTokenizer` do BERT para analisar a decomposição morfológica em Português.

---

## 🛠️ Tarefas e Requisitos Técnicos

### Tarefa 1: O Motor de Frequências

**Dado Inicial:** Utilizar estritamente o dicionário `vocab` fornecido:

```python
vocab = {
    'l o w </w>': 5,
    'l o w e r </w>': 2,
    'n e w e s t </w>': 6,
    'w i d e s t </w>': 3
}
```

- **Função `get_stats(vocab)`:** Deve retornar um dicionário com a contagem de pares (ex: `('e', 's'): 9`).
- **Validação Obrigatória:** O par `('e', 's')` deve resultar em exatamente **9** (6 de *newest* + 3 de *widest*).

### Tarefa 2: O Loop de Fusão

- **Função `merge_vocab(pair, v_in)`:** Deve substituir todas as ocorrências do par pelo novo símbolo unido.
- **Iterações:** Executar o loop de treinamento por **5 iterações**.
- **Resultado Esperado:** Ao final das 5 iterações, o token `est</w>` deve ter sido criado.
- **Cuidado com Regex:** Ao fazer o join dos tokens, use `re.escape` para evitar problemas com caracteres especiais.

### Tarefa 3: WordPiece com Hugging Face

- **Modelo:** `bert-base-multilingual-cased`.
- **Frase de Teste:** `"Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."`
- **Ação:** Imprimir os tokens resultantes e observar o uso de `##`.

---

## 📋 Obrigações de Entrega e Sucesso

- **Repositório GitHub:** Código-fonte em `.py` ou `.ipynb`.
- **Versionamento:** Criar obrigatoriamente a tag `v1.0` no commit final.
- **Documentação (`README.md`):**
  - Explicar o significado de `##` nos tokens (ex: `##mente`).
  - Justificar por que sub-palavras evitam o travamento do modelo (problema de OOV).
- **Citação de IA:** Se usar IA para as funções de substituição/regex, detalhar quais trechos foram gerados e o que foi revisado por você.

---

## ⚠️ Cuidados e Atenção

- **Símbolo `</w>`:** Fundamental para identificar o fim da palavra. Não remova.
- **Espaços:** O dicionário inicial tem espaços entre cada letra. A fusão deve remover o espaço apenas entre o par selecionado (ex: `e s` vira `es`).
- **Persistência:** Garanta que a cada iteração o `get_stats` seja recalculado sobre o vocabulário atualizado.

---

## 🤖 Instruções para a IA (Claude/ChatGPT)

Ao me ajudar neste código:

1. Priorize clareza nas funções `get_stats` e `merge_vocab`.
2. Certifique-se de que a lógica de substituição de strings não quebre tokens que já foram unidos anteriormente.
3. Use a biblioteca `re` para manipulação de strings no BPE.
4. Para a Tarefa 3, foque na correta instalação e uso da biblioteca `transformers`.