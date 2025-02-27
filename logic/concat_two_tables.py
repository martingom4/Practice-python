import pandas as pd

def combine_two_tables(person: pd.Dataframe, address: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(person,address, on = 'person_id',how= 'left')
    result = result[['firstName', 'lastName', 'city', 'state']]
    return result
