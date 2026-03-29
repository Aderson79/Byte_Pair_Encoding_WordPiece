# Laboratório 6 - Tokenização: BPE (do zero) & WordPiece (Hugging Face)

import re
from collections import defaultdict
from transformers import AutoTokenizer

# ============================================================
# TAREFA 1: Motor de Frequências (BPE)
# ============================================================

# Vocabulário inicial fornecido pelo enunciado
vocab = {
    'l o w </w>': 5,
    'l o w e r </w>': 2,
    'n e w e s t </w>': 6,
    'w i d e s t </w>': 3
}


def get_stats(vocab):
    """Conta a frequência de cada par adjacente de símbolos no vocabulário."""
    pass


# TODO: Validar que get_stats retorna ('e', 's'): 9

# ============================================================
# TAREFA 2: Loop de Fusão (Merges)
# ============================================================


def merge_vocab(pair, v_in):
    """Substitui todas as ocorrências do par pelo símbolo unido no vocabulário."""
    pass


# TODO: Executar 5 iterações do loop de treinamento BPE
# TODO: Validar que o token 'est</w>' foi criado

# ============================================================
# TAREFA 3: WordPiece com Hugging Face
# ============================================================

# TODO: Carregar bert-base-multilingual-cased
# TODO: Tokenizar a frase de teste e imprimir tokens
