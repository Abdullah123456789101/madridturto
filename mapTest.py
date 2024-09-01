import pandas as pd
import folium as F
longboi = pd.read_csv("LongBoi.csv")
#53.0765452103364, 8.820692530590472
map = F.Map(location=(53.08, 8.8), zoom_start=12)

F.Marker((53.08, 8.8), popup='Binaur').add_to(map)
F.Marker((56.15636128169986, 10.18786533164987), popup='Aarhus gymnasium c').add_to(map)
F.Marker((2.0729226546484942, 45.333782685774594), popup='Mogadishu').add_to(map)

F.PolyLine(locations=[(56.156373232084015, 10.187715127955723), (2.0729226546484942, 45.333782685774594)], color='blue').add_to(map)
F.PolyLine(locations=[(48.19357393335752, 16.308905638257915), (48.29592777273515, 4.07991017131623)], color='blue').add_to(map)
F.PolyLine(locations=[(56.156373232084015, 10.187715127955723), (6.316190291923891, -10.816162337460593)], color='blue').add_to(map)
map.show_in_browser()
map.save("Map.html")
input("wait for exit")