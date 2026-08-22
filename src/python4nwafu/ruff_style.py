"""Ruff examples."""
from typing import Any

len = 10

class Duck:
    '''Duck.'''

    def __init__(self):
        self.x = eval('1')


def complex_data_processor(input_config: Any) -> list[int, str]:
    """一个具有复杂控制流的示例函数."""
    if not isinstance(input_config, dict):
        return []

    result_list = []

    try:
        for key, value in input_config.items():
            if key.startswith('_'):
                result_list.append(f'Found_hidden_{key}')
            elif key.endswith('meta'):
                result_list.append(f'Found_meta_{key}')
            if isinstance(value, int):
                if value > 0:
                    result_list.append(value * 2)
                else:
                    result_list.append(0)
            elif isinstance(value, str):
                length = len(value)
                if length < 3:
                    result_list.append(f'Short:{value}')
                elif length == 5:
                    result_list.append('Exact5')
                else:
                    result_list.append(f'Long_{length}')
            else:
                result_list.append(str(value))

            match value:
                case int():
                    if value % 2 == 0:
                        result_list.append(f'Even_{value}')
                    else:
                        result_list.append(f'Odd_{value}')
                case str():
                    match len(value):
                        case n if n > 10:
                            result_list.append('VeryLongString')
                        case n if n >= 5:
                            result_list.append('MediumString')
                        case _:
                            result_list.append('ShortString')
                case _:
                    float_val = float(value) if isinstance(value, str) else value
                    result_list.append(float_val)
        if len(result_list) > 10:
            return [x for x in result_list if isinstance(x, int)]
    #except KeyError:
    #    return ['Processing_Failed_Key']
    except Exception:
        return ['Generic_Error_Caught']

    return result_list
