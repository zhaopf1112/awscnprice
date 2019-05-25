#from select_ri_no5 import *
from select_ri import *
#from select_ri_no5_sap import *
import pandas as pd

input = pd.read_excel("blog3_input.xlsx")
output = pd.DataFrame()
#os.environ['EXCLUDE_EC2_TYPE'] = "3,t"

ri = RI()
for i in range(0, input.shape[0]):
    row = pd.DataFrame(input.loc[[i]])
    row = row.reset_index(drop=True)
    result = ri.select_ec2_by_type(input_row=row)
    output = output.append(result, ignore_index=True, sort=False)
output = pd.concat([input, output], axis=1, join_axes=[input.index])
print (output)
output.to_excel('blog3_output.xlsx', index=False)