# Customer_Segmentation
## Background
Data comes from a commercial Sales database of an Export company, starting from April 2019, With Product Category, Customer Code
Destination Country, Quantity of Item in Invoice, and total Price of each Item. the marketing team wants to
create segments of customers based on transaction patterns so that marketing strategies can be developed for 
each segment.
## [Data Management](https://github.com/Ahmd-karrar/Customer_Segmentation/blob/main/Data_management.py)
- create Month and Year variables.
### Derived variables used for customer segmentation 
- Total_Sales 
- Number of unique Purchase 
- Number of unique Brand
- Number of unique Destination
#### Merging all the above dfs
#### Replace Nan value with 0 since NA 
## Model Build
- Drop unnecessary columns
- Standardize the data using scale()
- Create a plot for the elbow method to decide the optimum number of clusters
- Running KMeans model
- Add cluster membership to the data
- Visualising cluster solution using two principal components of variables used in the clustering algorithm
- Calculate the mean for each variable clusterwise
![cluster_ddddddd](https://github.com/Ahmd-karrar/Customer_Segmentation/assets/155227956/b38f9eba-803b-4a28-9355-770ccd90a1ab)

Comment: cluster 3 appears to be a cluster of "Platinum" customers whereas customers in Cluster 3 are a group of underperformers. Customers in cluster 1 are next to the "Platinum" group.
