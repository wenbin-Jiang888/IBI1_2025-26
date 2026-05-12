def calculate_protein_mass(sequence):
    # Amino acid residue mass table (monoisotopic mass)
    mass_table = {
        'G': 57.02,
        'A': 71.04,
        'S': 87.03,
        'P': 97.05,
        'V': 99.07,
        'T': 101.05,
        'C': 103.01,
        'I': 113.08,
        'L': 113.08,
        'N': 114.04,
        'D': 115.03,
        'Q': 128.06,
        'K': 128.09,
        'E': 129.04,
        'M': 131.04,
        'H': 137.06,
        'F': 147.07,
        'R': 156.10,
        'Y': 163.06,
        'W': 186.08
    }

    total_mass = 0.0

    for aa in sequence:
        if aa not in mass_table:
            return f"Error: Invalid amino acid symbol '{aa}'"
        total_mass += mass_table[aa]

    return total_mass


# Example usage
if __name__ == "__main__":
    seq1 = "GASPV"
    mass1 = calculate_protein_mass(seq1)
    print(f"Sequence {seq1} total mass: {mass1} amu")

    seq2 = "GAX"
    mass2 = calculate_protein_mass(seq2)
    print(f"Sequence {seq2} result: {mass2}")
seq=input("Please enter the protein sequence: ")
mass= calculate_protein_mass(seq)
print(f"Sequence {seq} result: {mass}")