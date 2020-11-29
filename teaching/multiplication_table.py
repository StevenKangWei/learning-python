def main():
    for i in range(1, 10):
        for j in range(1, i + 1):
            # print("{: 2} * {: 2} = {: 3}".format(j, i, i * j), end=' ')
            print(f"{j: 2} * {i: 2} = {i*j: 3}", end=' ')
        print()


if __name__ == '__main__':
    main()
