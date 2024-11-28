#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

print("Hello world")

a <- data.frame(t1 = 1:10,t2 = 11:20)
saveRDS(a,file="test.rds")
