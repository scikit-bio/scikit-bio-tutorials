The brain Dataset
======

The dataset used in this tutorial was collected from human cerebral cortex cortical tissue, from eight adults and four embryonic samples ranging from 16 to 18 gestational weeks in age. The study was published in:

- Darmanis, S., Sloan, S. A., Zhang, Y., Enge, M., Caneda, C., Shuer, L. M., Hayden Gephart, M. G., Barres, B. A., and Quake, S. R. (2015). A survey of human brain transcriptome diversity at the single cell level. PNAS 112 (23) 7285-7290.
- https://doi.org/10.1073/pnas.1507125112

The data reported in this paper have been deposited in the Gene Expression Omnibus (GEO) database, www.ncbi.nlm.nih.gov/geo (accession no. GSE67835)

Descriptions of files are provided below.

## Expression profile

`tags.csv`: scRNA-seq count matrix
- 466 cells by 22,085 genes
- 420 cells after initial filtering

## Cell type information

`ct.csv`: Labels for each cell
- 8 cell types in total
- neurons, fetal quiescent, astrocytes, oligodendrocytes fetal replicating, endothelial, OPC, microglia included

## Dissimilarity matrix

`cidr.csv`: dissimilarity matrix using CIDR algorithm
- generated using `tags.csv`
- R code for matrix generation provided in `brainCIDR.R`
- resulting a 420 by 420 dissimilarity matrix with dissimilarity score between each of the cell
