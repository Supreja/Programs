library(compare)
library(fields)
irisdata<-read.csv("iris.csv",header = TRUE)

centroids <-irisdata[sample(nrow(irisdata),3),]

newcentroids <- data.frame(X=numeric(),
                           Sepal.Length=numeric(),
                           Sepal.Width=numeric(),
                           Petal.Length=numeric(),
                           Petal.Width=numeric())
comp <- compare(centroids$X,newcentroids$X)
iterations <- 0
repeat
{
  
  if((comp$result==TRUE) | (iterations>=3))
  {
    break
  }
  print(centroids)
  eu<-rdist(irisdata[-6],centroids[-6])
  eu
  colnames(eu) <- c(1,2,3)
  minrow<-colnames(eu)[apply(eu,1,which.min)]
  print(minrow)
  cbind(irisdata,minrow)
  for(i in c(1,3))
    newcentroids<-aggregate.data.frame(irisdata[,!names(irisdata) %in% drops],by=list(minrow),FUN=mean)
    newcentroids
    comp <- compare(centroids$X,newcentroids$X)
  iterations=iterations+1
  centroids$X <- newcentroids$X
  centroids$Sepal.Length<-newcentroids$Sepal.Length
  centroids$Sepal.Width<-newcentroids$Sepal.Width
  centroids$Petal.Length<-newcentroids$Petal.Length
  centroids$Petal.Width<-newcentroids$Petal.Width
  
}  

