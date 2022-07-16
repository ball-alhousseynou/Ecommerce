# Ecommerce: classification of a product based on a description

## Dataset
This is the classification based E-commerce text dataset for 4 categories - "Electronics", "Household", "Books" and "Clothing & Accessories".

The dataset containt two columns - the first column is the class name and the second one is the datapoint of that class. The data point is the product and description from the e-commerce website.

<table class="dataframe">
  <thead>
    <tr>
        <th>labels</th>
        <th>descriptions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Household</td>
        <td>Paper Plane Design Framed Wall Hanging Motivat...</td>
    </tr>
    <tr>
        <td>Household</td>
        <td>SAF 'Floral' Framed Painting (Wood, 30 inch x ...</td>
    </tr>
    <tr>
        <td>Household</td>
        <td>SAF 'UV Textured Modern Art Print Framed' Pain...</td>
    </tr>
  </tbody>
</table>

For more details >>> [dataset ecommerce ](https://www.kaggle.com/datasets/saurabhshahane/ecommerce-text-classification)

____________________________________________________________________________________________________________________

## Installation
```bash
python -m venv .venv
source ./.venv/bin/activate 
[on windows: .venv\Scripts\activate.bat ]
pip install -r requirements.txt
```
____________________________________________________________________________________________________________________

## ML Models 
- cross validation
<table>
	<thead>
		<tr>
			<th>Models Mean</th>
			<th>F1 score</th>
			<th>Standard deviation</th>
			<th>Time execution(seconds)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>MultinomialNB</td>
			<td>0.942345</td>
			<td>0.001469</td>
			<td>56.890371</td>
		</tr>
		<tr>
			<td>LogisticRegression</td>
			<td>0.967854</td>
			<td>0.001422</td>
			<td>281.605662</td>
		</tr>
		<tr>
			<td>LinearSVC</td>
			<td>0.982501</td>
			<td>0.000840</td>
			<td>68.450801</td>
		</tr>
	</tbody>
</table>

- Lsvc validation dataset
<table>
    <thead>
        <th></th>
        <th>precision</th>
        <th>recall</th>
        <th>f1-score</th>
        <th>support</th>
    </thead>
    <tbody>
        <tr>
            <td>Books</td>    
            <td>0.99</td>         
            <td>0.96</td>          
            <td>0.98</td>          
            <td>2393</td>    
        </tr>
        <tr>
            <td>Clothing & Accessories</td>           
            <td>0.98</td>        
            <td>0.99</td>        
            <td>0.99</td>        
            <td>1697</tr>
        <tr>
            <td>Electronics</td>          
            <td>0.98</td>          
            <td>0.97</td>          
            <td>0.98</td>          
            <td>2137</td>    
        </tr>
        <tr> 
            <td>Household</td>           
            <td>0.97</td>         
            <td>0.99</td>         
            <td>0.98</td>         
            <td>3858</tr>
        <tr></tr>
        <tr>
            <td>accuracy</td>     
            <td></td>    
            <td></td>    
            <td>0.98</td>        
            <td>10085</td>    
        </tr>
        <tr>
            <td>macro avg</td>          
            <td>0.98</td>      
            <td>0.98</td>         
            <td>0.98</td>       
            <td>10085</td>    
        </tr>
        <tr>
            <td>weighted avg</td>           
            <td>0.98</td>       
            <td>0.98</td>         
            <td>0.98</td>        
            <td>10085</td>    
        </tr>
    </tbody>
</table>

- Lsvc test dataset
<table>
    <thead>
        <th></th>
        <th>precision</th>
        <th>recall</th>
        <th>f1-score</th>
        <th>support</th>
    </thead>
    <tbody>
        <tr>
            <td>Books</td>    
            <td>0.98</td>         
            <td>0.97</td>          
            <td>0.98</td>          
            <td>2335</td>    
        </tr>
        <tr>
            <td>Clothing & Accessories</td>           
            <td>0.98</td>        
            <td>0.98</td>        
            <td>0.98</td>        
            <td>1772</tr>
        <tr>
            <td>Electronics</td>          
            <td>0.98</td>          
            <td>0.97</td>          
            <td>0.97</td>          
            <td>2111</td>    
        </tr>
        <tr> 
            <td>Household</td>           
            <td>0.97</td>         
            <td>0.99</td>         
            <td>0.98</td>         
            <td>3867</tr>
        <tr></tr>
        <tr>
            <td>accuracy</td>     
            <td></td>    
            <td></td>    
            <td>0.98</td>        
            <td>10085</td>    
        </tr>
        <tr>
            <td>macro avg</td>          
            <td>0.98</td>      
            <td>0.98</td>         
            <td>0.98</td>       
            <td>10085</td>    
        </tr>
        <tr>
            <td>weighted avg</td>           
            <td>0.98</td>       
            <td>0.98</td>         
            <td>0.98</td>        
            <td>10085</td>    
        </tr>
    </tbody>
</table>
          
## BERT classifier 
- Training
<table class="tg">
  <thead>
    <tr>
      <th>Epoch</th>
      <th>Training Loss</th>
      <th>Validation Loss</th>
      <th>F1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>0.206200</td>
      <td>0.190536</td>
      <td>0.966490</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0.096100</td>
      <td>0.162596</td>
      <td>0.975175</td>
    </tr>
    <tr>
      <td>3</td>
      <td>0.065700</td>
      <td>0.126519</td>
      <td>0.979635</td>
    </tr>
  </tbody>
</table>

- Bert test dataset
<table>
    <thead>
        <th></th>
        <th>precision</th>
        <th>recall</th>
        <th>f1-score</th>
        <th>support</th>
    </thead>
    <tbody>
        <tr>
            <td>Books</td>    
            <td>0.98</td>         
            <td>0.97</td>          
            <td>0.98</td>          
            <td>2335</td>    
        </tr>
        <tr>
            <td>Clothing & Accessories</td>           
            <td>0.99</td>        
            <td>0.99</td>        
            <td>0.99</td>        
            <td>1772</tr>
        <tr>
            <td>Electronics</td>          
            <td>0.97</td>          
            <td>0.97</td>          
            <td>0.97</td>          
            <td>2111</td>    
        </tr>
        <tr> 
            <td>Household</td>           
            <td>0.98</td>         
            <td>0.98</td>         
            <td>0.98</td>         
            <td>3867</tr>
        <tr></tr>
        <tr>
            <td>accuracy</td>     
            <td></td>    
            <td></td>    
            <td>0.98</td>        
            <td>10085</td>    
        </tr>
        <tr>
            <td>macro avg</td>          
            <td>0.98</td>      
            <td>0.98</td>         
            <td>0.98</td>       
            <td>10085</td>    
        </tr>
        <tr>
            <td>weighted avg</td>           
            <td>0.98</td>       
            <td>0.98</td>         
            <td>0.98</td>        
            <td>10085</td>    
        </tr>
    </tbody>
</table>
          
## Dataviz
![Alt text](images/labels.png?raw=true "labels")
![Alt text](images/household.png?raw=true "household")
![Alt text](images/books.png?raw=true "books")
![Alt text](images/clothing_accessories.png?raw=true "clothing")
![Alt text](images/electronics.png?raw=true "electronics")

____________________________________________________________________________________________________________________

## Deployment streamlit
[streamlit ecommerce ](https://aball-ecommerce.herokuapp.com/)

![Alt text](images/dataset-cover.jpg?raw=true "dataset")

____________________________________________________________________________________________________________________

## Contact
ball.alhousseynou@ugb.edu.sn
