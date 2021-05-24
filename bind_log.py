"""Send queries and print stadistical information"""
# Third lib
import pandas

# Local lib 
import api
import bind_parser

def get_top(dataframe:any, column_name: str, limit:int = 5):
    rows_count = len(df)
    df_by_name = df.groupby([column_name]).size().reset_index(name='counts')

    df_by_name = df_by_name.sort_values(by=['counts'], ascending=False).head(limit).reset_index(drop=True)
    df_by_name['R. frecuency'] = df_by_name['counts'].apply(lambda x:  f"{'{:.4f}'.format(100*x / rows_count)} %")

    return df_by_name

bind_data = bind_parser.load("queries")

api.send_dns_queries(bind_data)

df = pandas.DataFrame(data=bind_data)


print(f"Total records {len(df)}")


print("\nClient IPs Rank\n--")
print(get_top(df,column_name = 'name'))

print("\nHost Rank\n--")
print(get_top(df,column_name = 'client_ip'))

