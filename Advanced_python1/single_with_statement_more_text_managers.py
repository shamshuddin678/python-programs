with(
    open("files/file.txt") as f1,
    open("files/pratice_set/poems.txt") as f2
):
    data1 = f1.read()
    data2 = f2.read()
    print(f"F1 content: {data1}")

    print(data2)
    print(f"F2 content: {data2}")    