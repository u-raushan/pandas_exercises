from datetime import datetime
from datetime import timedelta
import time
import pandas

# Tables of heart rate and blood pressure
df_hr = pandas.DataFrame({'time': [datetime(2022,1,1,7,40), datetime(2022,1,1,9,50), datetime(2022,1,1,10,1)], 'hr': [60, 90,100]})
df_bp = pandas.DataFrame({'time': [datetime(2022,1,1,10), datetime(2022,1,1,8)], 'bp': [140, 120]})

# Expected result
print(pandas.DataFrame({'time_hr': [datetime(2022,1,1,9,50)], 'hr': [90], 'time_bp': [datetime(2022,1,1,10)], 'bp': [140]}))

df_new = df_bp.copy()
df_new[['time_hr', 'hr']] = ["", ""]
df_new.rename(columns = {'time':'time_bp'}, inplace = True)

ind2 = 0
for ind in range(len(df_bp)):
    earliest, latest = df_bp.loc[ind,'time']-timedelta(minutes=15), df_bp.loc[ind,'time']
    if df_hr.loc[ind2,'time'] <= earliest:
        ind2 += 1
    if earliest <= df_hr.loc[ind2,'time'] <= latest:
        df_new.loc[ind,'time_hr'] = df_hr.loc[ind2,'time']
        df_new.loc[ind,'hr'] = df_hr.loc[ind2,'hr']
print(df_new) 
