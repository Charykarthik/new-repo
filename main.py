

"""
Python Dependendies

gcsfs
fsspec
pandas
pandas-gbq

"""
def hello_gcs(event):
     

    
     # triggered by a change to a cloud storage bucket.
    #Args:
     #   event (dict):event payload.
      #  context (gc function.context):metadata for event.event
    

    lst = []
    file_name =event['name']
    table_name = file_name.split(',')[0]

    #event, file meta data details writing into big query
    dct={
        'Event_ID':event.event_id,
        'Event_type':event.event_type,
        'Bucket_name':event['bucket'],
        'File_name':event['name'],
        'Created':event['timeCreated'],
        'update':event['update'],
    }
    lst.append(dct)
    df_metadata = pd.DataFrame.from_records(lst)
    df_metadata.to_gbq('sceg_karthik.data_loading_metedata',
                       project_id='bamboo-medium-381213',
                       if_exists='append',
                       location='us')
    

    #Actual file data,writing to bigquery

    df_data = pd.read_csv('gs://' + event['bucket'] + *.txt)
    df_data.to_gbq('sceg_karthik.' + table_name,
                   project_id='bamboo-medium-381213',
                   if_exists='append',
                   location='us')
