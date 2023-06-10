# import prettytable as pt
from cpuinfo import get_cpu_info


def get_cpu_stat():
    cpu_info = get_cpu_info()

    # table = pt.PrettyTable()
    # table.field_names = ['Attribute', 'Value']
    # table.align['Attribute'] = 'l'
    # table.align['Value'] = 'l'

    # for key, value in cpu_info.items():
    #     table.add_row([key, f'{value:.2f}'])

    # return f"<pre>{table}</pre>"

    return cpu_info
