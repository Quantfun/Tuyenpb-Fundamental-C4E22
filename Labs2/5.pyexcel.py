import pyexcel
from collections import OrderedDict
data = [
    OrderedDict({
        "Name": "Kent",
        "Age":29,
    }),
    OrderedDict({
        "Name": "Ivy",
        "Age":3,
    }),
    OrderedDict({
        "Name": "Pea",
        "Age":25,
    })
]

pyexcel.save_as(records=data,dest_file_name="sample.xlsx")
