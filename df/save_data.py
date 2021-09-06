import pandas as pd
from .utils import generate_records
from .models import DataframeFilled

def save_data(data, df_name, col_types):
    print(data)
    print(col_types)
    datasha = generate_records(col_types, 100)
    print(datasha)
    # print(generate_records(col_types, 100))
    new_data = pd.DataFrame(columns=data.columns, data=generate_records(col_types, 100))
    return new_data
    # data.to_csv('{}.csv'.format(df_name))


def gen_data(data_schemas, user, session_dict, row_nums):
    # new_data_dict = {}
    for d in data_schemas:
        new_d = DataframeFilled()
        new_data = pd.DataFrame(
            columns=d.data.columns,
            data=generate_records(session_dict.get('{}_col_types'.format(d.df_name)), row_nums)
        )
        new_d.user = user
        new_d.df_name = d.df_name
        new_d.data = new_data
        new_d.save()
        # new_data_dict[d.df_name] = new_data
    return {'status': True}

        # new_data_list.append(new_data)
    # return new_data_dict
