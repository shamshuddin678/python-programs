with open("files/pratice_set/poems.txt") as f:
    content = f.read()
    if("tiwnkle" in content):
        print("tiwnkle is present no problem")
    else:
        print("tiwnkle is not present")   