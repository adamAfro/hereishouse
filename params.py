from pandas import read_csv, DataFrame



def parse(df, id_name = "id", param_name = "params"):

    """
    zbiera parametry w formacie <key><=>value<->value<->value<br>key><=>value<->... z DataFrame,
    >>> parse_params(df)
    id    price[currency]       m rooms_num     market  ... fence_types heating_types access_types vicinity_types is_bungalow
    325017             PLN   72.14         4  secondary  ...        None          None         None           None        None
    """

    columns = [id_name]
    csv_entries = []
    for (i, row) in df.iterrows():
        
        entry = parse_entry(row, columns, id_name, param_name)
        csv_entries.append(entry)
    
    return DataFrame(csv_entries, columns=columns)



def from_file(input, iterrows = 10000, nchunks = None, id_name = "id", param_name = "params"):

    """
    zbiera parametry w formacie <key><=>value<->value<->value<br>key><=>value<->... z pliku CSV
    >>> parse_params_from_file("dane/train.csv")
    id    price[currency]       m rooms_num     market  ... fence_types heating_types access_types vicinity_types is_bungalow
    325017             PLN   72.14         4  secondary  ...        None          None         None           None        None
    """

    iterator = read_csv(input, chunksize=iterrows)

    columns = [id_name]
    csv_entries = []
    for (k, chunk) in enumerate(iterator):

        if (nchunks is not None and k >= nchunks):
            break

        for (i, row) in chunk.iterrows():
            
            entry = parse_entry(row, columns, id_name, param_name)
            csv_entries.append(entry)
    
    return DataFrame(csv_entries, columns=columns)



def parse_entry(row, columns, id_name = "id", param_name = "params"):

    """
    zmienna columns dostaje kolejne nazwy a zwracana jest lista z wartościami
    """

    entry = [str(row[id_name])]
    unordered = {}
    for param in row[param_name].split("<br>"):
        
        key_value = param.split("<=>")

        # pomija parametry bez wartości
        no_value = len(key_value) == 1
        if (no_value):
            continue

        key = key_value[0]

        # niektóre zmienne kończą się na _types i mają wtedy wiele możliwości które się dodatkowo łączą
        # tutaj są zamieniane na zmienne binarne
        if (key.endswith("types")):
            
            if key_value[1].strip() == "" or key_value[1].strip() == "0":
                continue

            for value in key_value[1].split("<->"):

                real_key = key + "_" + value
                if real_key not in columns:
                    columns.append(real_key)
                unordered[real_key] = True
            continue
        
        # dodaje nazwę parametru do nagłówka
        value = key_value[1]
        if key not in columns:
            columns.append(key)

        unordered[key] = value

    for key in columns[1:]:
        entry.append(unordered[key] if key in unordered else None)    

    return entry