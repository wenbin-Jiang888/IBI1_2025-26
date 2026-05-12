# 找最长开放阅读框 ORF
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

start_codon = 'AUG'
stop_codons = ['UAA', 'UAG', 'UGA']

longest_orf = ''
max_len = 0

# 遍历所有可能起始位置
for i in range(len(seq) - 2):
    if seq[i:i+3] == start_codon:
        # 从起始开始找终止密码子
        for j in range(i, len(seq) - 2, 3):
            codon = seq[j:j+3]
            if codon in stop_codons:
                current_orf = seq[i:j+3]
                current_len = len(current_orf)
                if current_len > max_len:
                    max_len = current_len
                    longest_orf = current_orf
                break

print("Longest ORF sequence:", longest_orf)
print("Length (nucleotides):", max_len)