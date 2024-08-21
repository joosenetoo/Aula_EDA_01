from LivroFiccao import LivroFiccao
from LivroNaoFiccao import LivroNaoFiccao

# Exemplo de uso
livro_ficcao = LivroFiccao("Dom Quixote", "Miguel de Cervantes", 500)
livro_nao_ficcao = LivroNaoFiccao("Sapiens", "Yuval Noah Harari", 100000)

print("--- Preço do livro de ficção ---")
print(f"Preço: R$ {livro_ficcao.calcular_preco()}")

print("\n--- Preço do livro de não ficção ---")
print(f"Preço: R$ {livro_nao_ficcao.calcular_preco()}")