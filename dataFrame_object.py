import os
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import wget  

def create_and_plot_deliveries_dataframe():
    file_url = "https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/dataset/deliveries.json"
    file_path = "deliveries.json"

    # Download the file if it doesn't exist
    if not os.path.exists(file_path):
        print(f"Downloading {file_url}...")
        wget.download(file_url, out=file_path)
        print("\nDownload complete.")

    # Loading data from JSON file
    with open(file_path, mode='r', encoding='utf8') as file:
        data = json.load(file)

    # Creating the main DataFrame
    deliveries_df = pd.DataFrame(data)

    # Normalizing the structure of the 'origin' column
    hub_origin_df = pd.json_normalize(deliveries_df['origin'])
    deliveries_df = pd.merge(left=deliveries_df, right=hub_origin_df, how='inner', left_index=True, right_index=True)
    deliveries_df.drop(["origin"], axis=1, inplace=True)

    # Selecting the desired columns
    columns = ["name", "region", "lng", "lat", "vehicle_capacity", "deliveries"]
    deliveries_df = deliveries_df[columns]

    # Renaming the columns
    deliveries_df.rename(columns={"lng": "hub_hub", "lat": "hub_lat"}, inplace=True)

    # Exploding the 'deliveries' column
    deliveries_exploded_df = deliveries_df[["deliveries"]].explode("deliveries")

    # Normalizing the data in the 'deliveries' column
    deliveries_normalized_df = pd.concat([
        pd.DataFrame(deliveries_exploded_df["deliveries"].apply(lambda record: record["size"])).rename(columns={"deliveries": "deliveries_size"}),
        pd.DataFrame(deliveries_exploded_df["deliveries"].apply(lambda record: record["point"])).rename(columns={"deliveries": "deliveries_lng"}),
        pd.DataFrame(deliveries_exploded_df["deliveries"].apply(lambda record: record["point"])).rename(columns={"deliveries": "deliveries_lat"}),
    ], axis=1)

    # Bar Chart for Count of Deliveries by Region
    plt.figure(figsize=(8, 8)) 
    region_counts = deliveries_df['region'].value_counts()
    region_counts.plot(kind='bar', rot=45, color='red')
    plt.title('Delivery Count by Region')
    plt.xlabel('Region')
    plt.ylabel('Score')
    plt.savefig('bar_chart.png') 
    plt.show()

    # Scatter Chart to Visualize Deliveries on the Map
    plt.figure(figsize=(8, 8)) 
    plt.scatter(deliveries_df['hub_hub'], deliveries_df['hub_lat'], c='red', label='Hub')
    deliveries_lng_list = deliveries_normalized_df['deliveries_lng'].apply(lambda coord: coord.get('longitude', None)).tolist()
    deliveries_lat_list = deliveries_normalized_df['deliveries_lat'].apply(lambda coord: coord.get('latitude', None)).tolist()
    filtered_lng_list = [lng for lng in deliveries_lng_list if lng is not None]
    filtered_lat_list = [lat for lat in deliveries_lat_list if lat is not None]
    plt.scatter(filtered_lng_list, filtered_lat_list, c='green', label='Entregas')
    plt.title('Location of Hubs and Deliveries')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.savefig('scatter_plot.png')
    plt.show()

    # Pie Chart to Visualize the Distribution of Regions
    plt.figure(figsize=(8, 8)) 
    plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
    plt.title('Distribution of Deliveries by Region')
    plt.savefig('pizza_graph.png')
    plt.show()

    # Return relevant information
    return deliveries_df, deliveries_normalized_df, {
        'bar_chart': 'bar_chart.png',
        'scatter_plot': 'scatter_plot.png',
        'pizza graph': 'pizza graph.png',
    }
