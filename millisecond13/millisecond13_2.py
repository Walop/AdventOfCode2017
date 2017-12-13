def main():
    with open("input") as file:
        entry_list = [entry.split(": ") for entry in file.read().splitlines()]
        scanner_list = [[int(entry[0]), (int(entry[1])-1)*2] for entry in entry_list]
        delay = 0
        failure = True
        while failure:
            failure = False
            for scanner in scanner_list:
                timing = delay + scanner[0]
                if timing % scanner[1] == 0:
                    failure = True
                    delay += 1
                    break
        print(delay)


main()
