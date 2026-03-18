
import matplotlib.pyplot as plt
import numpy as np
gene_expression = {
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}
print("1. Initial gene expression dictionary:")
print(gene_expression)

gene_expression["MYC"] = 11.6
print("\n2. Gene expression dictionary after adding MYC:")
print(gene_expression)

plt.figure(figsize=(10, 6))
genes = list(gene_expression.keys())
expressions = list(gene_expression.values())
plt.bar(genes, expressions, color='skyblue')
plt.title("Gene Expression Levels", fontsize=14)
plt.xlabel("Gene Name", fontsize=12)
plt.ylabel("Expression Level", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

target_gene = "EGFR" # Can modify this variable to test different genes
print("\n3. Query expression level of target gene:")
if target_gene in gene_expression:
    print(f"The expression level of gene {target_gene} is: {gene_expression[target_gene]}")
else:
    print(f"Error: Gene {target_gene} is not in the dataset!")

average_expression = sum(expressions) / len(expressions)
print(f"\n4. Average expression level of all genes: {average_expression:.2f}")

plt.show()