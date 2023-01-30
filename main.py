import json
from task import data_push
import pandas as pd


data = pd.read_excel(r'D:\KAJOL\STUDY\JOB\Vinculum\VINCU\VinStore\student.xlsx').set_index('id')
parsed = json.loads(data.to_json(orient = 'records'))
data = json.dumps(parsed, indent =4)
#print(json_data)
result = data_push.delay(data)
#print(result)


