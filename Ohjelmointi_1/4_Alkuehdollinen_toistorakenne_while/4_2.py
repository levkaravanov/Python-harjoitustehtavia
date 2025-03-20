while True:
    tuuma = float(input("Anna tuumaa:"))
    if tuuma < 0:
        break
    print(f"{tuuma * 2.54} cm")