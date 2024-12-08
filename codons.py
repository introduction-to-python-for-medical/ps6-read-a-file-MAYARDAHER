def create_codon_dict(file_path):
   path = "data/codons.txt"
   with open(path, "r") as file:
      rows = file.readlines()
   dic = {}
   for row in rows:
     cells = row.strip().split('\t')
     codon = cells[0]
     dic[codon] = cells[2]
   return dic


