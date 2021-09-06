from __future__ import absolute_import, unicode_literals

# from celery import shared_task
from celery.decorators import task
from celery.utils.log import get_task_logger

from .save_data import save_data, gen_data

logger = get_task_logger(__name__)
@task(name="save_and_download_data")
def save_and_download_data(data, df_name, col_types):
    logger.info("Data saved successfully")
    return save_data(data, df_name, col_types)


# @task(name="generate_data")
# def generate_data(data_schemas, user, session_dict, row_nums):
#     logger.info("Data saved successfully")
#     return gen_data(data_schemas, user, session_dict, row_nums)
@task(name="generate_data")
def generate_data(schema_user_dict, session_dict, row_nums):
    logger.info("Data saved successfully")
    return gen_data(schema_user_dict, session_dict, row_nums)