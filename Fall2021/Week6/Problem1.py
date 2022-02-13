def max (*argv):
    if len(argv) == 0:
        return "no numbers given"
    else:
        tempMax = argv[0]
        for arg in argv:
            if isinstance(arg, str):
                return "given argument is not a number"
            if arg > tempMax:
                tempMax = arg
    return tempMax