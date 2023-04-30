import json
from genson import SchemaBuilder

builder = SchemaBuilder()

# Создать схему json по образцу
with open("../files/reference.json", 'r') as f:
    datastore = json.load(f)
    builder.add_object(datastore)

users_schema = builder.to_schema()

# И записать её в файл
with open('../hw/users_schema.json', 'w') as f:
    s = json.dump(users_schema, f, indent=4)
    f.write(s)
