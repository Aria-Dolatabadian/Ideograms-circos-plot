#install pycirclize
import matplotlib.pyplot as plt
from pycirclize import Circos
from pycirclize.utils import ColorCycler

chr_bed_file, cytoband_file, chr_links = ("chr.bed","cytoband.tsv","genomic_link.tsv")

# Initialize Circos from BED chromosomes
circos = Circos.initialize_from_bed(chr_bed_file, space=3)
# circos.text("B. napus\n(Westar)", deg=315, r=150, size=12)
circos.text("B. napus\n(Westar)", size=12)

# Add cytoband tracks from cytoband file
circos.add_cytoband_tracks((95, 100), cytoband_file)

# Create chromosome color mapping
ColorCycler.set_cmap("hsv")
chr_names = [s.name for s in circos.sectors]
colors = ColorCycler.get_color_list(len(chr_names))
chr_name2color = {name: color for name, color in zip(chr_names, colors)}

# Plot chromosome name & xticks
for sector in circos.sectors:
    sector.text(sector.name, r=120, size=10, color=chr_name2color[sector.name])
    sector.get_track("cytoband").xticks_by_interval(
        50000000,
        label_size=8,
        label_orientation="vertical",
        label_formatter=lambda v: f"{v / 1000000:.0f} Mb",
    )


fig = circos.plotfig()
plt.show()

