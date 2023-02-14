#install pycirclize
import matplotlib.pyplot as plt
from pycirclize import Circos

chr_bed_file, cytoband_file, _ = ("chr.bed","cytoband.tsv","genomic_link.tsv")

# Initialize Circos from BED chromosomes
circos = Circos.initialize_from_bed(chr_bed_file, space=3)
circos.text("Brassica napus", size=15)

# Add cytoband tracks from cytoband file
circos.add_cytoband_tracks((95, 100), cytoband_file)

# Plot chromosome name
for sector in circos.sectors:
    sector.text(sector.name, size=10)

fig = circos.plotfig()

plt.show()

