import requests

def get_canadian_wildfire_updates():
    url = "https://services1.arcgis.com/HsjBaDykC1mjhXz9/arcgis/rest/services/Active_Wildfire_Perimeters_in_Canada/FeatureServer/0/query"
    params = {
        "where": "1=1",  # Retrieve all active wildfires
        "outFields": "FIRENAME,STATUS,AREA_HA",  # Fetch only relevant fields
        "f": "json"  # Response format
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        fires = data.get("features", [])
        
        if not fires:
            print("No active wildfires reported in Canada.")
            return
        
        print("Active Wildfires in Canada:")
        for fire in fires:
            attributes = fire.get("attributes", {})
            name = attributes.get("FIRENAME", "Unknown")
            status = attributes.get("STATUS", "Unknown")
            area = attributes.get("AREA_HA", "Unknown")
            
            print(f"\n🔥 Fire Name: {name}")
            print(f"   Status: {status}")
            print(f"   Affected Area: {area} hectares")
    else:
        print("Failed to fetch wildfire data. HTTP Status Code:", response.status_code)

if __name__ == "__main__":
    get_canadian_wildfire_updates()
