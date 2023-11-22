# Instahyre-Job-Analysis

<img src="https://github.com/ShivanniShinde/Instahyre-Job-Analysis/assets/143825606/e502f58f-c6b1-474b-bf40-aeb8afe63796" alt="Image Description" >

# Table of Contents

- [Introduction 🚀](#introduction-)
- [Objectives 🎯](#objectives-)
- [K-Means Clustering ✨](#k-means-clustering-)
  - [Model creation 💡](#model-creation-)
  - [Evaluating Model 📜](#evaluating-model-)
  - [Elbow Clustering for K-Means ✨](#elbow-clustering-for-k-means-)
- [Webpage Creation 🌐](#webpage-creation-)
- [Challenges 🧩](#challenges-)
- [Conclusion](#conclusion)

---
# Introduction 🚀

The Instahyre Job Analytics project is a data-driven endeavor that involves web scraping job posting data from Instahyre, followed by thorough data preprocessing and clustering analysis. The project's primary goal is to empower users with insights into the job market.

This project culminated in the development of an interactive web application, offering users the opportunity to explore job market insights, trends, and valuable information. Whether you are a job seeker or a recruiter, this project is designed to provide you with a comprehensive and user-friendly tool for making informed decisions in the job market.

---

# Objectives 🎯
<img src="https://github.com/ShivanniShinde/Instahyre-Job-Analysis/assets/143825606/8a7a475b-62a5-4410-b6f6-418fa68f6a79" alt="Image Description" width="100" height="100" align ='right'>

- **Data Extraction:** Our project employs Selenium, a powerful web automation tool, to extract data from the InstaHyre website. This data includes job listings, company information, and various other relevant details.

 
- **Data Analysis:** To make sense of the extracted data, we implement a K-means clustering model. This model groups job listings and companies into clusters based on common characteristics, allowing users to identify trends and patterns.
  <img src="https://github.com/ShivanniShinde/Instahyre-Job-Analysis/assets/143825606/81a13dec-0cec-4355-beb8-a59d0e3e8bb7" alt="Image Description" width="250" align ='right'>
- **Webpage Creation:** We've created an interactive webpage using HTML and CSS that displays the analyzed data in a user-friendly and visually appealing manner.
<br>
<br>

---

# K-Means Clustering ✨

K-Means is a machine learning technique used for data clustering. It groups similar data points into clusters based on their characteristics. In our project, we used K-Means clustering to discover patterns and relationships within job listings and companies, making it easier to identify trends and insights in the data.




## Model creation 💡
<div style="display: flex; justify-content: space-between;">
    <div style="flex: 1; margin-right: 20px;">
        <img src="https://github.com/ShivanniShinde/Instahyre-Job-Analysis/assets/143825606/8d89a528-2d06-441f-b773-5594d1a4690d" alt="Image Description" width="400" align ='left'>
    </div>
    <div style="flex: 2;">
       <li> We employed the Scikit-learn library for K-Means clustering. Scikit-learn is a powerful machine learning library in Python, and we harnessed its capabilities to implement a K-Means clustering model. </li><li>This model groups job listings and companies into clusters based on common characteristics, enabling the identification of valuable trends and patterns in the data.</li>
        <li>Our use of Scikit-learn ensures that the clustering process is efficient and robust, allowing for meaningful insights to be extracted from the data.</li>
        <br>
    
  </div>
</div>
<br>
<br>


## Evaluating Model 📜
A Silhouette Score is a metric used to evaluate the quality of clusters in K-Means clustering or other clustering algorithms
Silhouette Score of 0.97998 indicates strong and well-separated clusters in your K-Means model.
<p align="center">
  <img src="https://github.com/ShivanniShinde/Instahyre-Job-Analysis/assets/143825606/74ade680-fbb4-4058-8cc3-3a649641a1e4" alt="Image Description" width="450">
</p>


## Elbow Clustering for K-Means ✨

Elbow clustering, often used in K-Means, is a technique to determine the optimal number of clusters (k) for a dataset. It involves running K-Means for a range of k values and then looking for the "elbow point" on a plot of the cost or variance against k. The elbow point indicates the point where increasing the number of clusters no longer significantly reduces the within-cluster variance.

By applying elbow clustering, we aim to find the most appropriate number of clusters for our data, ensuring that our K-Means analysis is well-structured and provides meaningful insights.

<p align="center">
  <img src="https://github.com/ShivanniShinde/Instahyre-Job-Analysis/assets/143825606/43425f33-2f39-460f-9277-e23ddf57cb80" alt="Image Description" width="450">
</p>

---

# Webpage Creation 🌐
Designed a user-friendly and visually appealing webpage to showcase the results of  analysis. This webpage was created using HTML and CSS, combining elegant design with informative content.

## Video Presentation of webpage

[Click to download video](https://github.com/ShivanniShinde/Instahyre-Job-Analysis/raw/main/assets/143825606/034082d1-236a-4b5d-bf2c-10e4cc02e537)

---

## Challenges 🧩
<img src="https://github.com/ShivanniShinde/Instahyre-Job-Analysis/assets/143825606/9e3fdd2d-c7cc-4f3e-bb2c-1d849048dfe2" width="400" align="right">

During the development of this project, we encountered several challenges, which included:

1. **Webpage Design:** Designing a webpage with HTML and CSS presented challenges in making it both visually appealing and functional.

2. **User Input Handling:** Managing user input for text processing and learning was complex, requiring effective validation and processing mechanisms.

3. **Backend Development:** Developing the backend with Flask was a bit challenging, particularly when setting up data communication between the frontend and backend components.

4. **Web Scraping:** Web scraping using the Selenium library presented its own set of challenges, from handling dynamic web pages to efficient data extraction.

These challenges were crucial in our learning process and in making the project robust and user-friendly.

In summary, the project successfully provided insights into the job market through data analysis and web development, despite various data-related challenges.

---

## Conclusion
In conclusion, the Instahyre Job Analytics project successfully extracts, analyzes, and presents job market data. Utilizing Selenium for web scraping and Scikit-learn for K-Means clustering, the project delivers an interactive webpage for users to explore insights. Despite challenges in design, user input handling, backend development, and web scraping, the team's commitment shines through. The project stands as a robust, user-friendly tool, providing valuable job market information for both seekers and recruiters.




  

