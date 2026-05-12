# 读取FASTA，输出含框内终止密码子的基因（无最后一步单独处理）
input_fa = r'C:\Users\Lenovo\Desktop\IBI1\IBI1_2025-26\IBI1_2025-26\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_fa = r'C:\Users\Lenovo\Desktop\IBI1\IBI1_2025-26\IBI1_2025-26\Practical7\stop_genes.fa'

def get_gene_name(header):
    parts = header.split()
    for p in parts:
        if p.startswith('gene:'):
            return p.split(':')[1]
    return parts[0][1:]

def wrap_sequence(seq, width=60):
    return '\n'.join([seq[i:i+width] for i in range(0, len(seq), width)])

stop_codons = ['TAA', 'TAG', 'TGA']
result = []

# 一行一行读，读到 > 就处理上一条，然后开始新一条
current_header = None
current_seq = ''

with open(input_fa, 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue  # 跳过空行

        if line.startswith('>'):
            # 遇到新标题 → 先把上一条处理完
            if current_header is not None:
                # 检查是否合格
                has_atg = 'ATG' in current_seq
                has_stop = False
                stops_found = set()
                for i in range(0, len(current_seq)-2, 3):
                    c = current_seq[i:i+3]
                    if c in stop_codons:
                        has_stop = True
                        stops_found.add(c)
                if has_atg and has_stop:
                    gene = get_gene_name(current_header)
                    stops = ','.join(sorted(stops_found))
                    new_header = f'>{gene} stop={stops}'
                    result.append(new_header)
                    wrapped_seq = wrap_sequence(current_seq)
                    result.append(wrapped_seq)

            # 开始新序列
            current_header = line
            current_seq = ''
        else:
            # 拼接序列
            current_seq += line

# 写入结果
with open(output_fa, 'w') as f:
    f.write('\n'.join(result))

print('Done! 全程一个循环，无最后一步处理！')