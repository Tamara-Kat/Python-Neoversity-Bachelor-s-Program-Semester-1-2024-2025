def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary
    hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    # Move n-1 disks from auxiliary to target
    hanoi(n - 1, auxiliary, source, target)

hanoi(3, 'A', 'B', 'C')

# https://ua5.org/osnprog/255-algoritm-khanojjska-vezha.html
