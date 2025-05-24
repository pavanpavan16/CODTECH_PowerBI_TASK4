# CODTECH_TASK4
# 🧠 Task 4: Advanced Analytics in Power BI using Python


*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : PAVAN MANUMARRI

*INTERN ID* : CT04DK572

*DOMAIN* : POWER BI

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH



## 📄 Description
This project demonstrates the use of Python scripting within Power BI to perform advanced data analysis and custom visualizations. The dataset used is the popular "Superstore" sample data, which includes details about orders, customers, sales, and regional performance.

Python is integrated directly in Power BI to:
- Perform data preprocessing and cleaning
- Create advanced visualizations such as pairplots and heatmaps
- Detect sales outliers and sales trends
- Summarize category-wise performance

## 📈 Summary
The report highlights how Python can extend Power BI’s native capabilities to include advanced statistical analysis and custom visuals. This is especially useful for data scientists and analysts who want to apply machine learning or deeper analysis within a BI environment.

## 🔗 Report File
In Power BI Service, if your report is connected to streaming data (such as via a Streaming Dataset or Push Dataset), downloading a PBIX file is typically not supported. This limitation exists because:
Streaming datasets do not store historical data.
Power BI does not retain the report definition in a format that can be exported as a PBIX when using certain types of streaming data sources.
Therefore, I uploaded a mp4 file. 
Here is the reference for this task to the complete

## STEPS
📌 STEP-BY-STEP PROCESS:
🔹 Step 1: Set Up Your Environment
Make sure you have the following:

✅ A Microsoft Power BI account (Pro or higher recommended)

✅ Access to Power BI Service: https://app.powerbi.com

✅ Azure account (if you're using Azure Event Hub / IoT Hub)

✅ Python or Node.js environment (for simulating real-time data)

✅ Postman (for manual API testing if needed)

🔹 Step 2: Create a Streaming Dataset in Power BI
Go to Power BI Service (not Power BI Desktop).

Click on Workspace > Choose your workspace.

Click “+ New” > Streaming dataset.

Select API as the source and click Next.

Define dataset schema, e.g.:

json
Copy
Edit
{
  "timestamp": "DateTime",
  "temperature": "Number",
  "humidity": "Number",
  "location": "Text"
}
Turn “Historic data analysis” to ON (if you want to use report visuals).

Click Create and note the Push URL provided.

🔹 Step 3: Send Streaming Data to Power BI
You have 2 options:

Option A: Use Azure Stream Analytics
Set up an Azure Stream Analytics job.

Input: Azure Event Hub / IoT Hub / Blob

Output: Power BI

Authenticate Power BI when configuring output.

Map fields from Stream Analytics to Power BI dataset.

Option B: Simulate Data using Python (Example)
python
Copy
Edit
import requests
import json
import time
import random
from datetime import datetime

url = 'https://api.powerbi.com/beta/YOUR_WORKSPACE_ID/datasets/YOUR_DATASET_ID/rows?key=YOUR_API_KEY'

while True:
    data = [{
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(40.0, 60.0), 2),
        "location": "Lab1"
    }]
    
    response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
    print(response.status_code, response.text)
    time.sleep(2)
Make sure to replace the url with the one Power BI gave you.

🔹 Step 4: Build a Live Dashboard in Power BI
Go back to your workspace in Power BI Service.

Click + New Dashboard.

Use the “Add a tile” option.

Choose Custom streaming data as source.

Select the dataset you created earlier.

Pick visual types (line chart, card, gauge, etc.).

Configure fields (e.g., temperature as Y-axis, timestamp as X-axis).

Your dashboard will start updating live as data comes in from your API or stream.

🔹 Step 5: Customize and Format Your Dashboard
Add filters or slicers if you enabled historic analysis.

Use time-based visuals like:

Line charts for trends

Cards for current value

Gauges for threshold alerts

Title and format your visuals to make the dashboard user-friendly.

🔹 Step 6: Share or Export the Dashboard
Share with others using Power BI workspace access.

Pin the dashboard to a Power BI App for external visibility.

Take screenshots or screen recordings for your internship submission.

✅ COMPLETION CHECKLIST FOR YOUR INTERNSHIP:
 Power BI Streaming Dataset Created

 Real-Time Data Feed Working (via API or Azure)

 Dashboard Live and Updating in Real-Time

 Dashboard Contains Multiple Visuals (Card, Line Chart, etc.)

 Documented or Demonstrated Dashboard for Certificate

## 🛠️ Tools & Technologies Used
- **Power BI** – for report development and data visualization
- **Python** – for scripting and custom analytics
  - Pandas
  - Seaborn
  - Matplotlib
- **Superstore Dataset** – for sales and performance analysis


## 📷 Sample Features in Report
- Region-wise and category-wise breakdown
- Dynamic slicers for filtering by segment, category, and region
- Python visuals:
  - Heatmaps showing correlation
  - Scatterplots for quantity vs. profit
  - Boxplots for profit outliers
  - Forecasting trends

