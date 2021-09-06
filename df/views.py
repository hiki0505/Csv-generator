import ast
import collections
import csv

from django.http.response import HttpResponse
from django.shortcuts import render
import pandas as pd

from .models import Dataframe, DataframeFilled
from .tasks import generate_data


def sort_columns_by_order_ints(col_names, col_types, col_indexes):
    coltype_ind_dict = dict(zip(col_indexes, col_types))
    col_name_ind_dict = dict(zip(col_indexes, col_names))
    od_ct = collections.OrderedDict(sorted(coltype_ind_dict.items()))
    od_cn = collections.OrderedDict(sorted(col_name_ind_dict.items()))
    return list(od_cn.values()), list(od_ct.values())


def homepage(request):
    return render(request, 'df/user_home.html')


def create_data(request):
    if request.method == 'POST':
        print(request.POST)
        schema_name = request.POST.get('schema')
        col_sep = request.POST.get('col_sep')
        str_char = request.POST.get('str_char')
        col_names = ast.literal_eval(str(request.POST.getlist('col_name')))
        col_types = ast.literal_eval(str(request.POST.getlist('col_type')))
        orders = ast.literal_eval(str(request.POST.getlist('order')))

        column_names, column_types = sort_columns_by_order_ints(col_names, col_types, orders)

        df = pd.DataFrame(columns=column_names)

        datafile_pd = Dataframe()
        datafile_pd.df_name = schema_name
        datafile_pd.data = df
        datafile_pd.user = request.user
        datafile_pd.save()

        request.session['{}_col_types'.format(schema_name)] = column_types
        request.session['{}_col_sep'.format(schema_name)] = col_sep

        print(request.session.get('{}_col_types'.format(schema_name)))
        print(request.session.get('{}_col_sep'.format(schema_name)))

        return render(request, 'df/add_schema.html')

    try:
        dfka = Dataframe.objects.last()
        print(dfka.data)
    except AttributeError:
        pass

    return render(request, 'df/add_schema.html')


def processing_data(request):
    if request.method == 'POST':
        data_schemas = Dataframe.objects.filter(user=request.user)
        row_nums = request.POST.get('row_nums')

        generate_data.delay(
            data_schemas,
            request.user,
            dict(request.session),
            int(row_nums)
        )

        return render(request, 'df/processing.html', context={'data_schemas': data_schemas,
                                                              'success': 'Data generated successfully!'})
    data_schemas = Dataframe.objects.filter(user=request.user)
    return render(request, 'df/processing.html', context={'data_schemas': data_schemas})


def export(request):
    df_name = [key for key, value in request.POST.items()][1]
    df_to_download = DataframeFilled.objects.filter(df_name=df_name, user=request.user)
    random_data = df_to_download[0].data

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{df_name}.csv"'

    writer = csv.writer(response)
    writer.writerow(list(random_data.columns))
    writer.writerows(list(random_data.itertuples(index=False)))

    return response
