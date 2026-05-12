# 密码子频率统计 + 饼图输出到文件
import matplotlib.pyplot as plt
from collections import Counter

input_fa = r'C:\Users\Lenovo\Desktop\IBI1\IBI1_2025-26\IBI1_2025-26\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'

# 用户输入
target_stop = input("Enter stop codon (TAA/TAG/TGA): ").strip().upper()
if target_stop not in ['TAA', 'TAG', 'TGA']:
    print("Invalid codon")
    exit()

# 读取序列
sequences = []
current_seq = ''
with open(input_fa, 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            if current_seq:
                sequences.append(current_seq)
                current_seq = ''
        else:
            current_seq += line
if current_seq:
    sequences.append(current_seq)

all_codons = []

for seq in sequences:
    if 'ATG' not in seq:
        continue
    # 找所有ATG起始，到target_stop的最长ORF
    longest_codons = []
    for i in range(len(seq)-2):
        if seq[i:i+3] == 'ATG':
            codons = []
            for j in range(i, len(seq)-2, 3):
                c = seq[j:j+3]
                codons.append(c)
                if c == target_stop:
                    break
            else:
                continue
            # 去掉终止密码子本身
            if codons[-1] == target_stop:
                codons = codons[:-1]
            if len(codons) > len(longest_codons):
                longest_codons = codons
    if longest_codons:
        all_codons.extend(longest_codons)

if not all_codons:
    print("No data")
    exit()

count = Counter(all_codons)
total = sum(count.values())
print("Codon counts:")
for c, n in count.most_common(10):
    print(f"{c}: {n}")

# 画饼图
labels = list(count.keys())
sizes = list(count.values())
plt.figure(figsize=(10,7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize':8})
plt.title(f'Codon distribution upstream of {target_stop}')
plt.savefig('codon_pie.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"Pie chart saved to codon_pie.png")