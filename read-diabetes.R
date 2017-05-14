dataset <- diabetes
dim(dataset)
# dimentions needed
age <- as.matrix(dataset[,8])
typeof(age)
no.pregrancy <- as.matrix(dataset[,1])
lable <- as.matrix(dataset[,9])
glocous <- as.matrix(dataset[,2])
skinThickness <- as.matrix(dataset[,3])
# Lets see data as pairs
# AGE VS PREGRANCY NUMBER
plot (x= age[,1] , y = no.pregrancy[,1] ,type = "p", main="Age vs no of pregrancy ", xlab="Women Age"
      , ylab = "no of women get pregnant", xlim=c(18,85), ylim=c(1,20))
# AGE VS lable
plot (x= age[,1] , y = lable[,1] ,type = "p", main="Age vs lable ", xlab="Women Age"
      , ylab = "Women  have diabites or not", xlim=c(18,85), ylim=c(0,1.5))
# AGE VS GLOCOSE
maxGlo <- which.max(glocous[,1])
plot (x= age[,1] , y = glocous[,1] ,type = "p", main="Age vs glocous level ", xlab="Women Age"
      , ylab = "glocose Level", xlim=c(18,85), ylim=c(0,250))
# AGE VS SkinThickness
plot (x= age[,1] , y = skinThickness[,1] ,type = "p", main="Age vs skinThickness ", xlab="Women Age"
      , ylab = "skinThickness", xlim=c(18,85), ylim=c(0,150))
###############################
# PREGRANCY NUMBER vs lable
plot (x= no.pregrancy[,1] , y = lable[,1],type = "p", main=" no of pregrancy vs Women  have diabites or not", xlab="no of women get pregnant"
      , ylab = "Women  have diabites or not", xlim=c(1,20), ylim=c(0,1.5))
# PREGRANCY NUMBER vs GLOCOSE
plot (x= no.pregrancy[,1] , y = glocous[,1] ,type = "p", main=" no of pregrancy vs glocose level ", xlab="no of women get pregnant"
      , ylab = "glocouse level", xlim=c(1,20), ylim=c(0,250))
# PREGRANCY NUMBER vs SkinThickness
plot (x= no.pregrancy[,1] , y = skinThickness[,1]  ,type = "p", main=" no of pregrancy vs skinThickness ", xlab="no of women get pregnant"
      , ylab = "skinThickness", xlim=c(1,20), ylim=c(0,150))
##############################
# lable vs glocous level
plot (x= glocous[,1] , y = lable[,1] ,type = "p", main=" Women  have diabites or not VS Glocose level",  xlab="Women  have diabites or not"
      , ylab ="Women  have diabites or not", xlim=c(0,250), ylim=c(0,1))
# lable vs skinThickness
plot (x= skinThickness[,1] , y = lable[,1],type = "p", main=" Women  have diabites or not VS skinThickness", xlab="skinthikness"
      , ylab = "Women  have diabites or not", xlim=c(0,150), ylim=c(0,1))
##############################
# glocous vs skinThickness
plot (x= glocous[,1] , y = skinThickness[,1],type = "p", main="  Glocose level vs skinthikness", xlab="Women  have diabites or not"
      , ylab = "skinThickness ", xlim=c(0,250), ylim=c(0,150))
###########################################################################
################## Plot 3D Data ####################

















