import json


def read_json(path):
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def generate_diff(first_path, second_path):
    first_data = read_json(first_path)
    second_data = read_json(second_path)

    keys = sorted(first_data.keys() | second_data.keys())
    lines = ['{']

    for key in keys:
        if key not in second_data:
            val = format_value(first_data[key])
            lines.append(f'  - {key}: {val}')
        elif key in first_data and key in second_data:
            if first_data[key] == second_data[key]:
                val = format_value(first_data[key])
                lines.append(f'    {key}: {val}')
            else:
                val_1 = format_value(first_data[key])
                val_2 = format_value(second_data[key])
                lines.append(f'  - {key}: {val_1}')
                lines.append(f'  + {key}: {val_2}')
        else:
            val = format_value(second_data[key])
            lines.append(f'  + {key}: {val}')

    lines.append('}')

    return '\n'.join(lines)