import pandas as pd


def clean_course_inconsistencies(df):
    # Identificar el course_uuid más frecuente para cada course_name
    most_frequent_course_uuid = df.groupby('course_name')['course_uuid'].agg(lambda x: x.value_counts().index[0]).reset_index()
    most_frequent_course_uuid.columns = ['course_name', 'most_frequent_course_uuid']

    # Unir para tener el course_uuid más frecuente
    df = df.merge(most_frequent_course_uuid, on='course_name', how='left')

    # Reemplazar los course_uuid por el más frecuente
    df['course_uuid'] = df['most_frequent_course_uuid']

    # Eliminar la columna auxiliar
    df = df.drop(columns=['most_frequent_course_uuid'])
    
    return df

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
    # Identificar el assignment_id más frecuente para cada ass_name
    most_frequent_assignment_id = df.groupby('ass_name')['assignment_id'].agg(lambda x: x.value_counts().index[0]).reset_index()
    most_frequent_assignment_id.columns = ['ass_name', 'most_frequent_assignment_id']

    # Unir para tener el assignment_id más frecuente
    df = df.merge(most_frequent_assignment_id, on='ass_name', how='left')

    # Reemplazar los assignment_id por el más frecuente
    df['assignment_id'] = df['most_frequent_assignment_id']

    # Eliminar la columna auxiliar
    df = df.drop(columns=['most_frequent_assignment_id'])

    return df

def clean_submit_inconsistencies(df):
    # Verificar si hay duplicados en sub_uuid para diferentes ass_name_sub
    duplicated_ass_name_sub = df[df.duplicated(subset=['ass_name_sub'], keep=False)][['sub_uuid', 'ass_name_sub']]
    duplicated_ass_name_sub = duplicated_ass_name_sub.sort_values(by='ass_name_sub')

    # Identificar el sub_uuid más frecuente para cada ass_name_sub
    most_frequent_sub_uuid = df.groupby('ass_name_sub')['sub_uuid'].agg(lambda x: x.value_counts().index[0]).reset_index()
    most_frequent_sub_uuid.columns = ['ass_name_sub', 'most_frequent_sub_uuid']

    # Unir para tener el sub_uuid más frecuente
    df = df.merge(most_frequent_sub_uuid, on='ass_name_sub', how='left')

    # Reemplazar los sub_uuid por el más frecuente
    df['sub_uuid'] = df['most_frequent_sub_uuid']

    # Eliminar la columna auxiliar
    df = df.drop(columns=['most_frequent_sub_uuid'])

    # Verificación final
    unique_sub_uuids = df['sub_uuid'].nunique()
    unique_ass_name_sub = df['ass_name_sub'].nunique()

    return df