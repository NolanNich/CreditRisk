# CreditRisk

This respository contains three of the main stages in a basic data science life cycle: Data cleaning, Feature preparation and the machine learning algorithm prediction. We will be working with data from Lending Club, an online marketplace that matches lenders with borrowers. A borrower species a certain amount, which along with a number of other factors, contributes to an interest rate that Lending Club assigns to them. Lenders must then decide if this interest rate justifies the investment. Obviously, lenders will seek a larger interest rate to offset a loan to a borrower who seems less likely to pay back on time. 

We imagine ourselves as a conservative investor, who wants to use a machine learning algorithm to classify borrowers that will pay back the loan or not. For this purpose, we will use a logistic regression algorithm. 

This scenario lends itself well to machine learning. 

i) We have lots of data that contains information that is pertinent to the reliability of a borrower. 
ii) There are no mathematical equations that can answer this problem. 

We include two different algorithms. The first represents a naive data scientist who applies vanilla logistic regression to the data. We find that the unbalanced data set results in a model that predicts that nearly all borrowers will pay back the loan on time. 

The seocnd algorithm applies different penalities to false positives and false negatives, resulting ia a model that predicts nearly all borrowers who will fail to pay back the loan on time. 
