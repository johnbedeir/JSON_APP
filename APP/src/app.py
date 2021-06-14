#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:24:24 2021

@author: triple-a
"""
import requests

import xmltojson
import json
import utils

import os


def render(path=""):
    api = requests.get("https://reqres.in/api/users?page=2")

    if path.strip():
        path = os.getcwd()

    filePath = os.path.join(path, 'api.html')

    with open(filePath, "w") as html_file:
        html_file.write(api.text)

    return html_file


render()
