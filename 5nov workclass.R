# Load necessary libraries
library(ggplot2)

# Load the Iris dataset
data("iris")

# Display basic structure and summary
print("Dataset Structure:")
str(iris)
print("Summary of Dataset:")
summary(iris)

# 1. Plot histograms to explore distribution of each variable
par(mfrow = c(2, 2))  # Set up plot layout
for (col in colnames(iris)[1:4]) {
  hist(iris[[col]], main = paste("Histogram of", col),
       xlab = col, col = "lightblue", border = "black")
}
par(mfrow = c(1, 1))  # Reset layout

#Boxplot
data(mtcars)
boxplot(mpg~cyl,
data=mtcars,
xlab="Number of Cylinders",
ylab="Miles Per Gallon (mpg)",
main="Boxplot of MPG by cylinder count",
col=c("blue","red","yellow"),
border="blue",
pch=5)

# 4. Scatter plot for Petal.Length vs Petal.Width by species
ggplot(iris, aes(x = Petal.Length, y = Petal.Width, color = Species)) +
  geom_point(size = 3) +
  ggtitle("Petal Length vs Petal Width by Species") +
  xlab("Petal Length") + ylab("Petal Width") +
  theme_minimal()
