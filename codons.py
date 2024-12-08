def create_codon_dict(file_path):
   dic = {}
   for row in rows:
     cells = row.strip().split('\t')
     codon = cells[0]
     dic[codon] = cells[2]
   return dic


