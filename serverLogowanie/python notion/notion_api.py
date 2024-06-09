import uuid
from notion_client import Client
from pprint import pprint
import json

notion_token = 'secret_frHHTxg46cnG0Hwqaa18G45RcARsUrccAzpKPPs6VU2'
notion_page_id = 'ecde2dd21cfc4ed29ca7a807b0110203'
notion_database_id = 'fa7e2a2f5d5349cf9f47caaba2607d8f'

def write_dict_to_file_as_json(content, file_name):
    content_as_json_str = json.dumps(content)
    print(content_as_json_str)

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


def write_text(client, page_id, text, type='paragraph'):
    client.blocks.children.append(
      block_id=page_id,
      children=[{
        "object": "block",
        "type": type,
        type: {
          "rich_text": [{ "type": "text", "text": { "content": text } }]
        }
      }]
    )
    
def create_simple_blocks_from_content(client, content):

    page_simple_blocks = []

    for block in content:

        block_id = block['id']
        block_type = block['type']
        has_children = block['has_children']
        rich_text = block[block_type].get('rich_text')

        if not rich_text:
            return


        simple_block = {
            'id': block_id,
            'type': block_type,
            'text': rich_text[0]['plain_text']
        }

        if has_children:
            nested_children = read_text(client, block_id)
            simple_block['children'] = create_simple_blocks_from_content(client, nested_children)

        page_simple_blocks.append(simple_block)


    return page_simple_blocks
    

def write_row(client, database_id, status, date, name, owner):

    client.pages.create(
        **{
            "parent": {
                "database_id": database_id
            },
            'properties': {
                'status': {'multi_select': [{'name': status}]},
                'owner': {'rich_text': [{'text': {'content': owner}}]},
                'due_date': {'date': {'start': date}},
                'name': {'title': [{'text': {'content': name}}]},
            }
        }
    )


def main():
    client = Client(auth=notion_token)

    name = 'zrobić 10 pompek'
    status = 'TO DO'
    date = '2024-12-25'
    owner = '663c725629bd32252ec57d67'
        
    write_row(client, notion_database_id, status, date, name, owner)
    
    
if __name__ == '__main__':
    main()
          