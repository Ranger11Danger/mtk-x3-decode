with open("system.x3", 'rb') as file:
    data = file.read()
    hex_data = data.hex()


n = 2

test = [hex_data[i:i+n] for i in range(0, len(hex_data), n)]

data_len = "".join(test[:4])
test = test[4:]
tag = "".join(test[:4])
test = test[4:]
attr_size = "".join(test[:4])
test = test[4:]
while (len(test)>0):
    try:
        node_size = int("".join(test[:4]), 16)
        test = test[4:]
        node_data = test[:node_size]
        node_tag = int("".join(node_data[:4]), 16)
        node_data = node_data[4:]
        node_attr_size = int("".join(node_data[:4]), 16)
        node_data = node_data[4:]
        node_attrs = node_data[:node_attr_size]
        x = 0
        node = {}
        while True:
            try:
                attr_size = int("".join(node_attrs[:4]), 16)
                node_attrs = node_attrs[4:]
                attr_tag = int("".join(node_attrs[:4]), 16)
                node_attrs = node_attrs[4:]
                attr_type = int("".join(node_attrs[:4]), 16)
                node_attrs = node_attrs[4:]
                attr_count = int("".join(node_attrs[:4]), 16)
                node_attrs = node_attrs[4:]
                value_size = int("".join(node_attrs[:4]), 16)
                node_attrs = node_attrs[4:]
                if (attr_count == 0):
                    attr_value = bytearray.fromhex("".join(node_attrs[:value_size])).decode()
                    node_attrs = node_attrs[value_size:]
                if (attr_type == 3):
                    attr_value = int("".join(node_attrs[:4]), 16)
                    node_attrs = node_attrs[5:]
                if (attr_type == 1):
                    attr_value = bytearray.fromhex("".join(node_attrs[1:5])).decode()
                    node_attrs = node_attrs[5:]

                node[attr_tag] = attr_value
            except:
                break
        print(node)   
        test = test[node_size:]
    except:
        break
