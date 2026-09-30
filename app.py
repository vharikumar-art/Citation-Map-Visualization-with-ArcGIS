# import streamlit as st
# import pandas as pd
# import requests
# import folium
# from io import BytesIO
# from streamlit_folium import st_folium
# import time

# st.title("Citation Mapping with ArcGIS")

# # ArcGIS Geocoding API Key
# api_key = "AAPKdc7b2ff2df0643c9862ec9d816a967c68kookelLZzekcspoX5TtjXoVKK9lvFU3vJ6sILgSwqXg8efMFEBCc9NlnqYtlAid"

# def get_lat_long_arcgis(university, country):
#     geocode_url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"
#     params = {
#         "f": "json",
#         "SingleLine": f"{university}, {country}",
#         "outFields": "Match_addr,Addr_type",
#         "token": api_key
#     }
#     try:
#         response = requests.get(geocode_url, params=params)
#         response_json = response.json()
#         if response_json["candidates"]:
#             location = response_json["candidates"][0]["location"]
#             return location["y"], location["x"]
#     except Exception as e:
#         st.error(f"Error for {university}, {country}: {e}")
#     return None, None

# uploaded_file = st.file_uploader("Upload Excel File with 'UNIVERSITY' and 'COUNTRY' columns", type=["xlsx"])

# if uploaded_file:
#     data = pd.read_excel(uploaded_file)
    
#     if 'UNIVERSITY' not in data.columns or 'COUNTRY' not in data.columns:
#         st.error("The Excel file must have 'UNIVERSITY' and 'COUNTRY' columns.")
#     else:
#         with st.spinner("Geocoding locations..."):
#             latitudes, longitudes = [], []
#             for _, row in data.iterrows():
#                 lat, lon = get_lat_long_arcgis(row["UNIVERSITY"], row["COUNTRY"])
#                 latitudes.append(lat)
#                 longitudes.append(lon)
#                 time.sleep(0.1)  # Rate limit

#             data['Latitude'] = latitudes
#             data['Longitude'] = longitudes

#         st.success("Geocoding completed.")

#         # Create map
#         m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB positron")
#         for _, row in data.iterrows():
#             if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']):
#                 folium.Marker(
#                     location=[row['Latitude'], row['Longitude']],
#                     popup=f"{row['UNIVERSITY']} ({row['COUNTRY']})",
#                     tooltip=row['UNIVERSITY'],
#                     icon=folium.Icon(color='red', icon='circle', prefix='fa')
#                 ).add_to(m)

#         # Save HTML to memory
#         map_html = m._repr_html_()
#         buffer = BytesIO()
#         m.save(buffer, close_file=False)

#         st.markdown("### 📍 Map Preview")
#         st_folium(m, width=700)

#         st.markdown("### ⬇️ Download Map as HTML")
#         st.download_button(
#             label="Download HTML Map",
#             data=buffer.getvalue(),
#             file_name="Citation_Map.html",
#             mime="text/html"
#         )










# import streamlit as st
# import pandas as pd
# import requests
# import folium
# from io import BytesIO
# from streamlit_folium import folium_static
# import time

# st.set_page_config(layout="wide")
# st.title("🌍 Citation Map Visualization with ArcGIS")

# # ArcGIS API key
# api_key = "AAPKdc7b2ff2df0643c9862ec9d816a967c68kookelLZzekcspoX5TtjXoVKK9lvFU3vJ6sILgSwqXg8efMFEBCc9NlnqYtlAid"

# def get_lat_long_arcgis(university, country):
#     geocode_url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"
#     params = {
#         "f": "json",
#         "SingleLine": f"{university}, {country}",
#         "outFields": "Match_addr,Addr_type",
#         "token": api_key
#     }
#     try:
#         response = requests.get(geocode_url, params=params)
#         response_json = response.json()
#         if response_json["candidates"]:
#             location = response_json["candidates"][0]["location"]
#             return location["y"], location["x"]
#     except Exception as e:
#         return None, None
#     return None, None

# # File uploader
# uploaded_file = st.file_uploader("📄 Upload Excel File with 'UNIVERSITY' and 'COUNTRY' columns", type=["xlsx"])

# if uploaded_file:
#     data = pd.read_excel(uploaded_file)

#     if 'UNIVERSITY' not in data.columns or 'COUNTRY' not in data.columns:
#         st.error("❌ The file must contain 'UNIVERSITY' and 'COUNTRY' columns.")
#     else:
#         st.info("⏳ Fetching coordinates for universities...")
#         latitudes, longitudes = [], []

#         progress_bar = st.progress(0)
#         status_text = st.empty()

#         for idx, row in data.iterrows():
#             university = row['UNIVERSITY']
#             country = row['COUNTRY']
#             lat, lon = get_lat_long_arcgis(university, country)
#             latitudes.append(lat)
#             longitudes.append(lon)

#             # Update progress
#             percent_complete = (idx + 1) / len(data)
#             progress_bar.progress(percent_complete)
#             status_text.text(f"Processing: {university}, {country}")

#             time.sleep(0.1)  # respect API rate limit

#         data['Latitude'] = latitudes
#         data['Longitude'] = longitudes

#         st.success("✅ Geocoding complete!")

#         # Full screen Folium map
#         st.markdown("## 🌐 Fullscreen Map View")
#         m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB positron")

#         for _, row in data.iterrows():
#             if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']):
#                 folium.Marker(
#                     location=[row['Latitude'], row['Longitude']],
#                     popup=f"{row['UNIVERSITY']} ({row['COUNTRY']})",
#                     tooltip=row['UNIVERSITY'],
#                     icon=folium.Icon(color='red', icon='circle', prefix='fa')
#                 ).add_to(m)

#         # Save map to HTML (in memory)
#         buffer = BytesIO()
#         m.save(buffer, close_file=False)

#         folium_static(m, width=1400, height=700)

#         st.download_button(
#             label="📥 Download Map as HTML",
#             data=buffer.getvalue(),
#             file_name="Citation_Map.html",
#             mime="text/html"
#         )



import streamlit as st
import pandas as pd
import requests
import folium
from io import BytesIO
from streamlit_folium import st_folium
import time

st.set_page_config(layout="wide")
st.title("🌍 Citation Map Visualization with ArcGIS")

api_key = "AAPTaiWjXPzgowMZT7jNiiV4sZg..fZWlHwm5HgC5t_EuUWV82KUOeSf4sR37HXhAwufktIO5LUQwxcC3GKrXrJYcfDPvWz2XpiuYJDk-RJEhU7d--v_5XAKzv2U6uR0oDrOMKlA6pcEMXgb9MuO1EdDUkneNCcnVTcWzS3uLA-Jst8jpC6FQ2FrfCKFnmwDehoxpQUtQOtX3ZYLHHog9S3_-JyVO4w4pSL0VGny4ne7beOTskc_VXt3OLtaxLlonMDlwJQ3D3_9U8F-T9kEhJCQC5Byw4wMjduMYho4.AT1_thvavnaT"

def get_lat_long_arcgis(university, country):
    geocode_url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"
    params = {
        "f": "json",
        "SingleLine": f"{university}, {country}",
        "outFields": "Match_addr,Addr_type",
        "token": api_key
    }
    try:
        response = requests.get(geocode_url, params=params)
        response_json = response.json()
        if response_json["candidates"]:
            location = response_json["candidates"][0]["location"]
            return location["y"], location["x"]
    except Exception as e:
        return None, None
    return None, None

# Session state to avoid recomputation
if 'html_map_bytes' not in st.session_state:
    st.session_state['html_map_bytes'] = None

uploaded_file = st.file_uploader("📄 Upload Excel File with 'UNIVERSITY' and 'COUNTRY' columns", type=["xlsx"])

if uploaded_file and st.session_state['html_map_bytes'] is None:
    data = pd.read_excel(uploaded_file)

    if 'UNIVERSITY' not in data.columns or 'COUNTRY' not in data.columns:
        st.error("❌ The file must contain 'UNIVERSITY' and 'COUNTRY' columns.")
    else:
        st.info("⏳ Fetching coordinates for universities...")
        latitudes, longitudes = [], []

        progress_bar = st.progress(0)
        status_text = st.empty()

        for idx, row in data.iterrows():
            university = row['UNIVERSITY']
            country = row['COUNTRY']
            lat, lon = get_lat_long_arcgis(university, country)
            latitudes.append(lat)
            longitudes.append(lon)

            percent_complete = (idx + 1) / len(data)
            progress_bar.progress(percent_complete)
            status_text.text(f"Processing: {university}, {country}")

            time.sleep(0.1)

        data['Latitude'] = latitudes
        data['Longitude'] = longitudes

        st.success("✅ Geocoding complete!")

        m = folium.Map(location=[20, 0], zoom_start=2, tiles=None)
        folium.TileLayer(
            tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
            attr="Tiles &copy; Esri and its data providers",
            name="Esri World Street Map",
        ).add_to(m)
        for _, row in data.iterrows():
            if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']):
                folium.Marker(
                    location=[row['Latitude'], row['Longitude']],
                    popup=f"{row['UNIVERSITY']} ({row['COUNTRY']})",
                    tooltip=row['UNIVERSITY'],
                    icon=folium.Icon(color='red', icon='circle', prefix='fa')
                ).add_to(m)

        buffer = BytesIO()
        m.save(buffer, close_file=False)
        st.session_state['html_map_bytes'] = buffer.getvalue()

        st.markdown("## 🌐 Fullscreen Map View")
        st_folium(m, width=1400, height=700)

if st.session_state['html_map_bytes']:
    st.markdown("### ⬇️ Download Your HTML Map")
    st.download_button(
        label="📥 Download HTML",
        data=st.session_state['html_map_bytes'],
        file_name="Citation_Map.html",
        mime="text/html"
    )
