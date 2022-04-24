from models import LinkedList as l


def main():
    lista_ligada = l.LinkedList()

    while True:
        comandos = input().lower().split()

        lista_ligada = verify_input(comandos, lista_ligada)

def verify_input(comandos:list, obj:object) -> object:
    if comandos[0] == "rpi":
        obj.insert_at_start(comandos[1])
        obj.traverse_list()

    elif comandos[0] == "rpf":
        obj.insert_at_end(comandos[1])
        obj.traverse_list()

    elif comandos[0] == "rpde":
        obj.insert_after_item(comandos[2], comandos[1])
        obj.traverse_list()

    elif comandos[0] == "rpae":
        obj.insert_before_item(comandos[2], comandos[1])
        obj.traverse_list()

    elif comandos[0] == "rpii":
        obj.insert_at_index(comandos[2], comandos[1])
        obj.traverse_list()

    elif comandos[0] == "vne":
        get_count:int = -1 
        get_count = obj.insert_at_index(comandos[2], comandos[1])
        print(f"O número de elementos são {get_count}.")

    elif comandos[0] == "vp":
        verify_country:bool = 0
        verify_country = obj.search_item(comandos[1])

        if verify_country == 1:
            print(f"O país {comandos[1]} encontra-se na lista.")
        else:
            print(f"O país {comandos[1]} não se encontra na lista.")

    elif comandos[0] == "epe":
        country:str = obj.start_node.get_item()
        obj.delete_at_start()
        print(f"O país {country} foi eliminado da lista.")

    elif comandos[0] == "eue":
        obj.delete_at_start()
        print(f"O país {comandos[1]} foi eliminado da lista.")

    elif comandos[0] == "ep":
        verify_country_exists: bool = 0

        verify_country_exists = obj.search_item(comandos[1])

        if verify_country_exists == 1:
            obj.delete_element_by_value(comandos[1])
            print(f"O país {comandos[1]} foi eliminado da lista.")
        else:
            print(f"O país {comandos[1]} não se encontra na lista.")

    return obj
