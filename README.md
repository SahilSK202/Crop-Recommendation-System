

# Crop Recommendation System Using Machine Learning

Crop recommendation is one of the most important aspects of precision agriculture. Crop recommendations are based on a number of factors. Precision agriculture seeks to define these criteria on a site-by-site basis in order to address crop selection issues. While the "site-specific" methodology has improved performance, there is still a need to monitor the systems' outcomes.Precision agriculture systems aren't all created equal. However, in agriculture, it is critical that the recommendations made are correct and precise, as errors can result in significant material and capital loss.


<br><br>
This application will assist farmers in increasing agricultural productivity, preventing soil degradation in cultivated land, reducing chemical use in crop production, and maximizing water resource efficiency. <br>In this application, the user can provide the soil data from their side and the application will predict which crop should the user grow.

# [ Dataset ](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset)
This dataset was build by augmenting datasets of rainfall, climate and fertilizer data available for India.

### [Attributes information:]()

* **N** - Ratio of Nitrogen content in soil
* **P** - Ratio of Phosphorous content in soil
* **K** - Ratio of Potassium content in soil
* **Temperature** -  temperature in degree Celsius
* **Humidity** - relative humidity in %
* **ph** - ph value of the soil
* **Rainfall** - rainfall in mm 

### [Experiment Results:]()

 * **Performance Evaluation**
    * Splitting the dataset by 67 % for training set and 33 % validation set.
 * **Training and Validation**
    * GausianNB with MinMaxScalar gets a higher accuracy score than other classification models.
    * GaussianNB ( 99 % accuracy score )
 * **Performance Results**
    * Training Score: 99.6%
    * Validation Score: 99.2%

 
# Demo
Live Demo: https://grow-precise.herokuapp.com/

![](https://github.com/SahilSK202/Crop-Recommendation-System/tree/main/static/app1.png)
![](https://github.com/SahilSK202/Crop-Recommendation-System/tree/main/static/app2.png)

## Further Improvements
There are lot of things to improve upon

- Frontend can be made more nicer 
- Need to improve responsiveness for mobile
- More data = More Accuracy = More Reliable
