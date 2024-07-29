import pandas as pd

def replace_with_most_frequent(df, group_col, replace_col):
    # Identificar el valor más frecuente de replace_col para cada group_col
    most_frequent = df.groupby(group_col)[replace_col].agg(lambda x: x.value_counts().index[0]).reset_index()
    most_frequent.columns = [group_col, f'most_frequent_{replace_col}']

    # Unir para tener el valor más frecuente
    df = df.merge(most_frequent, on=group_col, how='left')

    # Reemplazar los valores por el más frecuente
    df[replace_col] = df[f'most_frequent_{replace_col}']

    # Eliminar la columna auxiliar
    df = df.drop(columns=[f'most_frequent_{replace_col}'])
    
    return df

def clean_course_inconsistencies(df):
    return replace_with_most_frequent(df, 'course_name', 'course_uuid')

def clean_user_inconsistencies(df):
    # Verificar si hay user_uuid con más de un legajo asociado
    user_legajo_counts = df.groupby('user_uuid')['legajo'].nunique()
    problematic_user_uuids = user_legajo_counts[user_legajo_counts > 1].index

    # Corregir el problema seleccionando el legajo más frecuente para estos user_uuid problemáticos
    for user_uuid in problematic_user_uuids:
        most_frequent_legajo = df[df['user_uuid'] == user_uuid]['legajo'].value_counts().index[0]
        df.loc[df['user_uuid'] == user_uuid, 'legajo'] = most_frequent_legajo

    return df

def clean_assignment_inconsistencies(df):
    return replace_with_most_frequent(df, 'ass_name', 'assignment_id')

def clean_submit_inconsistencies(df):
    return replace_with_most_frequent(df, 'ass_name_sub', 'sub_uuid')