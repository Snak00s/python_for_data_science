import os


def ft_tqdm(lst: range) -> None:
    for x in lst:
        percent = int(((x + 1) / len(lst)) * 100)
        less = os.get_terminal_size().columns \
            - len(f"{percent}%|[]| {(x + 1)}/{len(lst)}") - 27
        string = ""
        less_threshold = int(less * percent / 100)
        for y in range(less):
            if y < less_threshold:
                string += "="
            elif y == less_threshold:
                string += ">"
            else:
                string += " "
        if (less_threshold == less):
            lststr = list(string)
            lststr[-1] = ">"
            string = "".join(lststr)
        print(f"{percent}%|[{string}]| {(x + 1)}/{len(lst)}", end='\r')
        yield
