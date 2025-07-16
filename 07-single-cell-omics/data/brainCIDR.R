
library(cidr)

brainTags <- read.csv("brainTags.csv")
rownames(brainTags) <- brainTags[,1]
brainTags <- brainTags[,-1]

scBrain <- scDataConstructor(as.matrix(brainTags))
scBrain <- determineDropoutCandidates(scBrain)
scBrain <- wThreshold(scBrain)
scBrain <- scDissim(scBrain)

write.csv(scBrain@dissim)