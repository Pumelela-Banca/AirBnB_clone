#!/usr/bin/python3
from models import base_model
from models import storage
import json
import sys


storage.reload()
obj = storage.all()
j = 0
ky = 'BaseModel' + '.' + '00a7840c-7c0e-42d5-af09-18371fbc7ecc'
if obj.get(ky) is None:
    print('** no instance found **')
    exit(1)

var = obj[ky]
var = eval(var)
model1 = base_model.BaseModel(**var)
model1.las
