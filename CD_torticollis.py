import pandas as pd
CD_data=pd.read_csv('E:\python\CD_DLC.csv')
#pd.set_option("display.max.columns", None)
CD_data.head()
frames_CD=CD_data["coords"]
nosebrx=CD_data["nb_x"]
nosebry=CD_data["nb_y"]
midlinex=CD_data["ad_x"]
midliney=CD_data["ad_y"]
distx=midlinex.subtract(nosebrx)
disty=midliney.subtract(nosebry)
import numpy as np
nosebrxr=np.where(nosebrx<0,0,nosebrx)
area_nbx=print('areanosebridgeright=', np.trapz(nosebrxr))
nosebrxl=np.where(nosebrx>0,0,nosebrx)
area_nbx=print('areanosebridgeleft=', np.trapz(nosebrxl))
move_nbx=print('movement_nosebridge_horizontal=', np.std(nosebrx))
import matplotlib.pyplot as plt
plt.plot((frames_CD/30), distx)
plt.plot((frames_CD/30), disty)
plt.plot((frames_CD/30), nosebry)
plt.plot((frames_CD/30), nosebrx)
plt.ylim(-50,250)
plt.axhline(0,linestyle='dotted')
plt.show()


