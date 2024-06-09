import uuid
from notion_client import Client
from pprint import pprint
import json

notion_token = 'secret_frHHTxg46cnG0Hwqaa18G45RcARsUrccAzpKPPs6VU2'
notion_page_id = 'ecde2dd21cfc4ed29ca7a807b0110203'
notion_database_id = 'fa7e2a2f5d5349cf9f47caaba2607d8f'

def write_dict_to_file_as_json(content, file_name):
    content_as_json_str = json.dumps(content)

    with open(file_name, 'w') as f:
        f.write(content_as_json_str)

def read_text(client, page_id):
    response = client.blocks.children.list(block_id=page_id)
    return response['results']

def safe_get(data, dot_chained_keys):
    '''
        {'a': {'b': [{'c': 1}]}}
        safe_get(data, 'a.b.0.c') -> 1
    '''
    keys = dot_chained_keys.split('.')
    for key in keys:
        try:
            if isinstance(data, list):
                data = data[int(key)]
            else:
                data = data[key]
        except (KeyError, TypeError, IndexError):
            return None
    return data

def main():
    client = Client(auth=notion_token)
    
    db_info = client.databases.retrieve(database_id=notion_database_id)

    write_dict_to_file_as_json(db_info, 'db_info.json')

    db_rows = client.databases.query(database_id=notion_database_id)

    write_dict_to_file_as_json(db_rows, 'db_rows.json')

    simple_rows = []

    for row in db_rows['results']:
        name = safe_get(row, 'properties.name.title.0.text.content')
        due_date = safe_get(row, 'properties.due_date.date.start')
        status = safe_get(row, 'properties.status.multi_select.0.name')
        owner = safe_get(row, 'properties.owner.rich_text.0.text.content')

        simple_rows.append({
            'name': name,
            'due_date': due_date,
            'status': status,
            'owner': owner
        })
        print(name, due_date, status, owner)

    write_dict_to_file_as_json(simple_rows, 'simple_rows.json')


if __name__ == '__main__':
    main()
