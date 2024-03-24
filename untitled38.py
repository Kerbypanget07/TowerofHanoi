def tower_of_hanoi():
    width = int(input("Enter the width of the tower: "))
    height = int(input("Enter the height of the tower: "))
    
    mystring = " "
    top_level = int(width/2)
    
    for i in range (top_level):
        mystring += " "
        
    mystring = " *"
    
    for i in range (1, height):
        mystring += "\n" + ("*" * width)
        
    mystring += "\n" + (("*" * width) + "*")
    
    print(mystring)

def move_disk(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return
    move_disk(n-1, source, auxiliary, target)
    print("Move disk", n, "from", source, "to", target)
    move_disk(n-1, auxiliary, target, source)

def hanoi_with_recursion():
    n = int(input("Enter the number of disks for Tower of Hanoi: "))
    move_disk(n, 'A', 'C', 'B')

tower_of_hanoi()
hanoi_with_recursion()
