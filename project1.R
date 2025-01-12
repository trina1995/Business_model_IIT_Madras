data<-read.csv(file.choose(),header=T)
Total_Volume<-aggregate(data$Qty ~ data$Item.Name,ndf, sum)
DDay<-as.numeric(substr(data$Bill.Date,1,2)) 
DMonth<-as.numeric(substr(data$Bill.Date,4,5)) 
DYear<-as.numeric(substr(data$Bill.Date,9,10)) 
V<-DDay+DMonth*30+(DYear-17)*12*30
V
V<-max(V,na.rm=TRUE)-V
V 
data<-cbind(data,V) 
data
freq<-as.matrix(data[3]*data[4])
freq
glm.fit1 <- glm(data$Qty ~ data$Item.Rate+freq,data=data, family=quasipoisson()) 
coef(glm.fit1) 
plot(density(resid(glm.fit1))) 
qqnorm(resid(glm.fit1)) 
summary(glm.fit1) 
sd(resid(glm.fit1)) 
fpicker<-function(g) 
{ 
dsn=1 for(sn in 1:30) 
{ 
if(sdcomp(g,sn+1)<sdcomp(g,sn)&&sdcomp(g,sn+2)>sdcomp(g,sn+1)&&(nrow(g)>30)) 
{ 
dsn=sn+1 
break 
} 
} 
#print(dsn) 
return(dsn) 
}