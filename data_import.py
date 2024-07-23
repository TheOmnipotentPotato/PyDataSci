from csv import reader

from pandas import DataFrame as DF


def csv_to_tokens(filename: str) -> list[str]:
    with open(filename, newline="") as csvfile:
        filereader = reader(csvfile, delimiter=",", quotechar="|")
        csv_tokens: list[str] = []
        for token in filereader:
            csv_tokens.append(token)
    return csv_tokens


def tokens_to_dict(csv_tokens: list[str]) -> dict[str, list[str]]:
    csv_tokens = csv_tokens[:]
    column_names = csv_tokens.pop(0)
    transposed_array: list[list[str]] = [[] for _ in range(len(column_names))]
    for row in csv_tokens:
        for idx, item in enumerate(row):
            transposed_array[idx].append(item)
    df_dict = {name: vector for name, vector in zip(column_names, transposed_array)}

    return df_dict


def csv_to_dataframe(filename: str) -> DF:
    return DF(tokens_to_dict(csv_to_tokens(filename)))
