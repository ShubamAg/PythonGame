def Move_rings(n, source, destination, temp):
    
    if n == 1:
        print(f"Move ring 1 from {source} to {destination}")
        return

    Move_rings(n - 1, source,temp, destination)
    
    print(f"Move ring {n} from {source} to {destination}")
    
    Move_rings(n - 1, temp, destination,source )

n = int(input("Enter the number of rings: "))

print("\nSteps to move rings to destination:")
Move_rings(n, 'A', 'B', 'C')
