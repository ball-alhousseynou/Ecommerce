## Ecommerce: classification of a product based on a description

### Dataset
This is the classification based E-commerce text dataset for 4 categories - "Electronics", "Household", "Books" and "Clothing & Accessories".

The dataset containt two columns - the first column is the class name and the second one is the datapoint of that class. The data point is the product and description from the e-commerce website.

<table border="1" class="dataframe">
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


### Installation
```bash
python -m venv .venv
source ./.venv/bin/activate 
[on windows: .venv\Scripts\activate.bat ]
pip install -r requirements.txt
```
### Models 
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mean F1 score</th>
      <th>Standard deviation</th>
      <th>Time execution(seconds)</th>
    </tr>
    <tr>
      <th>Model name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MultinomialNB</th>
      <td>0.953949</td>
      <td>0.001148</td>
      <td>36.536089</td>
    </tr>
    <tr>
      <th>LogisticRegression</th>
      <td>0.970093</td>
      <td>0.001619</td>
      <td>196.039848</td>
    </tr>
    <tr>
      <th>LinearSVC</th>
      <td>0.983119</td>
      <td>0.000746</td>
      <td>48.967262</td>
    </tr>
  </tbody>
</table>

- Linearsvc classifier
<table classe="tg">
<thead>
<tr>
  <th></th>
  <th>precision</th>
  <th>recall</th>
  <th>f1-score</th>
  <th>support</th>
</tr>
</thead>
<tbody>
<tr>
  <th>Books</th>
  <td>0.99</td>
  <td>0.97</td>
  <td>0.98</td>
  <td>3546</td>
</tr>
<tr>
  <th>Clothing & Accessories</th>
  <td>0.98</td>
  <td>0.99</td>
  <td>0.98</td>
  <td>2601</td>
</tr>
<tr>
  <th>Electronics</th>
  <td>0.98</td>
  <td>0.97</td>
  <td>0.98</td>
  <td>3187</td>
</tr>
<tr>
  <th>Household</th>
  <td>0.97</td>
  <td>0.99</td>
  <td>0.98</td>
  <td>5794</td>
</tr>
<tr>
  <th>accuracy</th>
  <td></td>
  <td></td>
  <td>0.98</td>
  <td>15128</td>
</tr>
<tr>
  <th>macro avg</th>
  <td>0.98</td>
  <td>0.98</td>
  <td>0.98</td>
  <td>15128</td>
</tr>
<tr>
  <th>weighted avg</th>
  <td>0.98</td>
  <td>0.98</td>
  <td>0.98</td>
  <td>15128</td>
</tr>
</tbody>
</table>

### Dataviz
![Alt text](images/labels.png?raw=true "labels")
![Alt text](images/household.png?raw=true "household")
![Alt text](images/books.png?raw=true "books")
![Alt text](images/clothing_accessories.png?raw=true "clothing")
![Alt text](images/electronics.png?raw=true "electronics")


### Deployment streamlit
[streamlit ecommerce ](https://aball-ecommerce.herokuapp.com/)
![Alt text](images/dataset-cover.jpg?raw=true "dataset")

### Contact
ball.alhousseynou@ugb.edu.sn
