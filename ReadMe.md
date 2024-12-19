# README: Data Scraping and Analysis

## Steps for Data Scraping
1. **Objective Identification**:
   - The goal was to extract data from an e-commerce website (noon.com) for the "yoga" catalog. The extracted data included product name, ID (SKU), brand, price, sale price, and image key.

2. **Website Inspection**:
   - Inspected the network responses using browser developer tools to find JSON responses containing product information.
   - Identified a specific API endpoint (a `https://www.noon.com/_next/data/...` URL) that provided paginated JSON data with all the required details.

3. **Scrapy Setup**:
   - Created a Scrapy project and configured a spider to make requests to the API endpoint.
   - Designed the spider to loop through pages (1 to 100) to fetch all available product data.

4. **Data Extraction**:
   - Extracted relevant fields from the JSON response, such as product name, ID, brand, brand ID, price, sale price, and image key.
   - Saved the collected data in a structured format (CSV file: `final_data.csv`).

## Steps for Data Analysis
1. **Loading the Data**:
   - Imported the scraped data from `final_data.csv` into a Jupyter Notebook using Pandas for analysis and visualization.

2. **Data Cleaning**:
   - Ensured all columns had consistent data types and removed any irrelevant fields if present.

3. **Data Visualization**:
   - Created various graphs to extract insights from the data:
     
     a. **Most Expensive and Cheapest Products**:
     - Identified the product with the highest and lowest sale price.
     - Visualized both products on a single line graph with labeled minimum and maximum points and a filled region between the prices.

     b. **Number of Products by Brand**:
     - Grouped the data by `brand_id` and counted the number of products for each brand.
     - Visualized the counts using a horizontal bar chart.

     c. **Candlestick Chart for Brand-wise Pricing**:
     - For each brand, calculated the minimum and maximum prices across products.
     - Created a candlestick graph for each brand, showing the price range.

## Notes
- The graphs generated in the notebook are not displayed in this README file. Please run the notebook to view all visualizations or refer to the exported figures (`Figure 1`, `Figure 2`, and `Figure 3`).
- For reproducibility, ensure you have the necessary dependencies installed, including `scrapy`, `pandas`, `matplotlib`, and `numpy`. Run the scripts in sequence to replicate the process.

