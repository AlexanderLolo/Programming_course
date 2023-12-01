def GenerateBBSTArray(array_of_nodes):

    total_number_of_nodes = len(array_of_nodes)

    if total_number_of_nodes == 1:
        return array_of_nodes


    sorted_array_of_nodes = sorted(array_of_nodes)
    binary_tree_array = []
    added_nodes = set()
    central_elem_index_step = total_number_of_nodes // 2

    while len(binary_tree_array) < total_number_of_nodes:

        # на каждом шаге делим массив на 2, 4, 8 и тд частей, выбирая центральные элементы
        for index in range(central_elem_index_step, total_number_of_nodes, central_elem_index_step + 1):
            if index in added_nodes:
                continue

            binary_tree_array.append(sorted_array_of_nodes[index])
            added_nodes.add(index)

        central_elem_index_step //= 2

    return binary_tree_array
