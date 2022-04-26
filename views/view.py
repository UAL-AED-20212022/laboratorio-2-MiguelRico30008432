from models import LinkedList as l


def main():
    lista_ligada = l.LinkedList()

    while True:
        comandos = input().split()

        lista_ligada = verify_input(comandos, lista_ligada)

def verify_input(comandos:list, obj:object) -> object:
    if comandos[0] == "RPI":
        obj.insert_at_start(comandos[1])
        obj.traverse_list()

    elif comandos[0] == "RPF":
        obj.insert_at_end(comandos[1])
        obj.traverse_list()

    elif comandos[0] == "RPDE":
        obj.insert_after_item(comandos[2], comandos[1])
        obj.traverse_list()

    elif comandos[0] == "RPAE":
        obj.insert_before_item(comandos[2], comandos[1])
        obj.traverse_list()

    elif comandos[0] == "RPII":
        obj.insert_at_index(int(comandos[2]), comandos[1])
        obj.traverse_list()

    elif comandos[0] == "VNE":
        get_count:int = obj.get_count()
        print(f"O número de elementos são {get_count}.")

    elif comandos[0] == "VP":
        verify_country:bool = 0
        verify_country = obj.search_item(comandos[1])

        if verify_country == 1:
            print(f"O país {comandos[1]} encontra-se na lista.")
        else:
            print(f"O país {comandos[1]} não se encontra na lista.")

    elif comandos[0] == "EPE":
        country:str = obj.start_node.get_item()
        obj.delete_at_start()
        print(f"O país {country} foi eliminado da lista.")

    elif comandos[0] == "EUE":
        get_country:str = obj.get_last_node()

        obj.delete_at_end()
        print(f"O país {get_country} foi eliminado da lista.")

    elif comandos[0] == "EP":
        verify_country_exists: bool = 0

        verify_country_exists = obj.search_item(comandos[1])

        if verify_country_exists == 1:
            obj.delete_element_by_value(comandos[1])
            print(f"O país {comandos[1]} foi eliminado da lista.")
        else:
            print(f"O país {comandos[1]} não se encontra na lista.")

    return obj
