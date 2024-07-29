import pandas as pd

def convert_epoch_to_datetime(df, columns):
    # Convierte columnas de epoch a formato de fecha legible.
    for column in columns:
        df[column] = pd.to_datetime(df[column], unit='s')
    return df

def from_epoch_to_datetime(df):
    # Convierte las columnas de epoch a un formato de fecha legible.
    epoch_columns = ['fecha_mesa_epoch', 's_graded_at', 's_submitted_at', 's_created_at', 
                     'ass_created_at', 'ass_due_at', 'ass_unlock_at', 'ass_lock_at']
    
    df = convert_epoch_to_datetime(df, epoch_columns)
    df.rename(columns={'fecha_mesa_epoch':'fecha_mesa'}, inplace=True)
        
    return df

def unify_values(df):
    # Unifica los valores que significan lo mismo.
    df['periodo'] = df['periodo'].replace('01-2022', '1-2022')
    return df
