portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    # Write your recursive code here
    if len(ports) > 0:
        remainPorts = len(ports)
        for i in range(remainPorts):
            permutations(route+[ports[i]], ports[i+1:]+ports[:i])

    # Print the port names in route when the recursion terminates
    else:
        print(' '.join([portnames[i] for i in route]))


# This will start the recursion with 0 "(PAN)" as the first stop
permutations([0], list(range(1, len(portnames))))
