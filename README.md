# Loggi Data Analysis

<h2>Welcome to my repository.</h2>
<h2>Project carried out using Python to extract data from the company “Loggi”.<img align="center" alto="Ellen-Git" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"></h2>  

<h2>"A business problem focused on Loggi company logistics will be analyzed and explored. The analysis will involve a subset of the original data available, facing several challenges,
  including the optimization of delivery routes and the efficient allocation of deliveries to fleet vehicles, considering their limited capacities, among other aspects."</h2>

  <h3>It was necessary to give the following command to be able to use wget.⬇️</h3>
<br></br>
    
  ````
  pip install wget

  ````
<br></br>
<h3>Python libraries were imported following PEP8 standards:</h3>

````
import wget
import os
import sys
import seaborn as sns
import pandas as pd

````
<br></br>
<hr></hr>
<h3>This is an analysis that has 636148 rows x 3 columns

<br><br>
  
<div align="center"> 
 <img align="center" alto="line-Loggi" height="350" width="700"  
     src="https://github.com/Ellen-TSantos/extract_cdi/assets/122386488/ca0791cc-70cd-4f3d-a384-e39d5a425daf">
<br><br>
 <img align="center" alto="line-Loggi" height="350" width="700"  
     src="https://github.com/Ellen-TSantos/extract_cdi/assets/122386488/ea4ea6a1-8eff-43bd-9a12-fba28a153174">
 </div>
<hr>

<h3>Items to be analyzed</h3>

<br>

<div  align="center">
 <img align="center" alto="line-Loggi" height="350" width="700"  
     src="https://github.com/Ellen-TSantos/movies/assets/122386488/0939f506-2eb1-412f-88b8-86ddd4a82d4b">

<br><br>

  <img align="center" alto="line-Loggi" height="180" width="700"  
     src="https://github.com/Ellen-TSantos/movies/assets/122386488/39d77aaf-39ef-4358-81ec-8d983c2ca66f">
</div>
     


<hr>
<br>

## Visualizations

<h2>This project includes several graphical visualizations to provide insights into delivery data. Below are brief descriptions of each graph:</h2>

<h3>TO VIEW GRAPHICS IT WAS NECESSARY TO INSTALL</h3>

  ````

pip install seaborn

````
<hr>
<br>
<div align="center">
   
<h2>Bar Chart : Delivery Count by Region</h2>
  
<img width="450" src="https://github.com/Ellen-TSantos/fashion_show_website/assets/122386488/b9587229-47b0-437a-877d-9bb13a317ddf">
  <br>
  This bar chart represents the count of deliveries by region. Each bar shows the quantity of deliveries in a specific region. The legend provides information about the distribution of deliveries across different regions.
  
<br>

<hr>
  <br>
  
<h2>Scatter Plot : Location of Hubs and Deliveries</h2>
  
<img width="450" src="https://github.com/Ellen-TSantos/fashion_show_website/assets/122386488/e7b5e7af-0528-4c20-bf96-dbb5abb2e689">
<br>
   The scatter plot displays the location of hubs (red points) and deliveries (green points) on the map. The x and y axes represent longitude and latitude, respectively. This provides a spatial view of deliveries in relation to the hubs.
   
  <br>
<hr>
  <br>
  
<h2>Pie Chart: Distribution of Deliveries by Region</h2> 

<img width="450" src="https://github.com/Ellen-TSantos/fashion_show_website/assets/122386488/e07fd345-2c4e-4e7f-b4fa-930e10566622">
<br>
 The pie chart illustrates the percentage distribution of deliveries across different regions. Each slice of the pie represents the proportion of deliveries in a specific region. This offers a quick glance at the contribution of each region to the total deliveries.
 
<br>
<hr>
</div>
<br>

<h3>Run the Main Script:</h3>
<h4>After installing the dependencies, run the main loggi_data.py script in the terminal:</h4>

````

python loggi_data.py

````
<h3>Check Results:</h3>
<h4>After the script runs, check the output in the terminal for any error or success messages. Furthermore, the analysis results and generated graphs can be found in the output files in the project directory.</h4>
