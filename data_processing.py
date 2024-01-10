import pandas as pd

def create_dataframe(data):
    # Print keys available in the dictionary of each delivery
    print("Keys available in the dictionary of each delivery:", data[0].keys())

    # Create a DataFrame from the input data
    deliveries_df = pd.DataFrame(data)

    # Extract 'region' from the 'origin' column and create a new column 'region'
    deliveries_df['region'] = deliveries_df['origin'].apply(
        lambda x: x.get('region') if x else None)

    # Normalize the 'origin' column using json_normalize
    hub_origin_df = pd.json_normalize(deliveries_df['origin'])
    # Merge the original DataFrame with the normalized DataFrame
    deliveries_df = pd.merge(left=deliveries_df, right=hub_origin_df,
                             how='inner', left_index=True, right_index=True)

    # Drop the 'origin' column
    deliveries_df.drop(["origin"], axis=1, inplace=True)

    # Reorder and select specific columns
    columns = ["name", "region", "lng", "lat",
               "vehicle_capacity", "deliveries"]
    deliveries_df = deliveries_df[columns]

    # Rename columns for clarity
    deliveries_df.rename(
        columns={"lng": "hub_hub", "lat": "hub_lat"}, inplace=True)

    # Explode the 'deliveries' column and create a new DataFrame
    deliveries_exploded_df = deliveries_df[["deliveries"]].explode("deliveries")

    # Create a new DataFrame with normalized 'deliveries' data
    deliveries_normalized_df = pd.concat([
        pd.DataFrame(deliveries_exploded_df["deliveries"].apply(
            lambda record: record["size"])).rename(columns={"deliveries": "deliveries_size"}),
        pd.DataFrame(deliveries_exploded_df["deliveries"].apply(
            lambda record: record["point"])).rename(columns={"deliveries": "deliveries_lng"}),
        pd.DataFrame(deliveries_exploded_df["deliveries"].apply(
            lambda record: record["point"])).rename(columns={"deliveries": "deliveries_lat"}),
    ], axis=1)

    # Print the normalized DataFrame
    print(deliveries_normalized_df)

    # Add the 'region' column from the original DataFrame to the normalized DataFrame
    deliveries_normalized_df['region'] = deliveries_df['region']

    # Return the final DataFrame
    return deliveries_normalized_df
