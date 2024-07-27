import pandas as pd

def from_epoch_to_datetime(data_path):
    
    df = pd.read_csv(data_path)
    # Convertir las columnas de epoch a un formato de fecha legible
    df['fecha_mesa'] = pd.to_datetime(df['fecha_mesa_epoch'], unit='s')
    df.drop(columns='fecha_mesa_epoch', inplace=True)
    df['s_graded_at'] = pd.to_datetime(df['s_graded_at'], unit='s')
    df['s_submitted_at'] = pd.to_datetime(df['s_submitted_at'], unit='s')
    df['s_created_at'] = pd.to_datetime(df['s_created_at'], unit='s')
    df['ass_created_at'] = pd.to_datetime(df['ass_created_at'], unit='s')
    df['ass_due_at'] = pd.to_datetime(df['ass_due_at'], unit='s')
    df['ass_unlock_at'] = pd.to_datetime(df['ass_unlock_at'], unit='s')
    df['ass_lock_at'] = pd.to_datetime(df['ass_lock_at'], unit='s')
    return df

def unify_values(data_path):
    
    df = pd.read_csv(data_path)
    # Unificar los valores que significan lo mismo
    df['periodo'] = df['periodo'].replace('01-2022', '1-2022')
    return df