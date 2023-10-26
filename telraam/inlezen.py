#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""Python module voor het inlezen van Telraam data.

"""

import requests
from datetime import datetime


def get_cameras(api_key, id={}, url='https://telraam-api.net/v1/cameras'):
    """"""

    if 'mac' in id.keys():
        url = f'{url}/{id["mac"]}'
    elif 'segment' in id.keys():
        url = f'{url}/segment/{id["segment"]}'

    headers = {'X-Api-Key': api_key}

    response = requests.request('GET', url, headers=headers)

    return response.json()


def get_segments(api_key, id={}, url='https://telraam-api.net/v1/segments'):
    """"""

    if 'segment' in id.keys():
        url = f'{url}/id/{id["segment"]}'
    else:
        url = f'{url}/all'

    headers = {'X-Api-Key': api_key}

    response = requests.request('GET', url, headers=headers)

    return response.json()


def get_data(
        api_key,
        id,
        start_datum,
        stop_datum,
        level='segments',  # 'instances'
        # format='per-hour',  # 'per-quarter'
        # columns=[],
        url='https://telraam-api.net/v1/reports/traffic',
        ):
    """"""

    headers = {'X-Api-Key': api_key}

    body = {
        'level': level,
        'id': id,
        'time_start': f"{start_datum} 00:00:00Z",  # TODO: include time
        'time_end': f"{stop_datum} 00:00:00Z",
        'format': 'per-hour',  # format,
    }
    # if columns:
    #     body['columns'] = columns

    response = requests.request('POST', url, headers=headers, data=str(body))

    return response.json()
