import json
#import Tkinter
import folium
map = folium.Map(location=(53.08, 8.8), zoom_start=12)
#root=Tkinter.Tk()
#width=root.winfo_screenwidth()
#height=root.winfo_screenheight()
#fig = folium.Map(width=width,height=height)
geo_json_map = json.load(open('bigwalk.geojson'))
folium.Choropleth(
    geo_data = geo_json_map,
    fill_color = "steelblue",
    fill_opacity = 1,
    line_color = "steelblue",
    line_opacity = 1
).add_to(map)
folium.Marker((40.414291633123966, -3.70384559016725), popup='Mola Hostel').add_to(map)
map.show_in_browser(