from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


file_paths = ['sod1.fasta', 'clp1.fasta', 'atg1.fasta']
output_paths = ['sod1.gb', 'clp1.gb', 'atg1.gb']


for i in range(len(file_paths)):
    with open(file_paths[i], 'r') as fasta_file:
        records = SeqIO.parse(fasta_file, 'fasta')
        genbank_records = []
        for record in records:
            genbank_record = SeqRecord(
                record.seq,
                id=record.id,
                description="Protein sequence",
                annotations={"molecule_type": "protein"}  # Molekül tipi!!!
            )
            genbank_records.append(genbank_record)
        with open(output_paths[i], 'w') as genbank_file:
            SeqIO.write(genbank_records, genbank_file, 'genbank')
            print(f"{file_paths[i]} dosyası {output_paths[i]} olarak kaydedildi.")
