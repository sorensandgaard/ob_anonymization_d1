#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

print("Hello world")

a <- data.frame(t1 = 1:10,t2 = 11:20)
a$t3 <- args[1]
a$t4 <- args[2]

saveRDS(a,file="test.rds")
