import sys

def main():
    num_cases = int(sys.stdin.readline() [:-1])

    for case in range(num_cases):

        turtle_dict = {}
        aux_dict = {}
        reverse_dict = {}
        turtles = int(sys.stdin.readline() [:-1])

        for turtle in range(turtles):
            name = sys.stdin.readline() [:-1]
            aux_dict [name] = turtle



        for turtle in range(turtles):
            name = sys.stdin.readline() [:-1]
            turtle_dict [name] = (name, aux_dict[name], turtle)
            reverse_dict [turtle] = name

        
        found = False
        aux = [turtle_dict[key] [1] for key in turtle_dict]
        idx = len(aux) - 2
        while idx >= 0:
            if aux[idx] > aux[idx + 1]:
                found = True
                break
            idx -= 1

        if found:
            while (idx >= 0):
                print(reverse_dict[idx])
                idx -= 1
        
        print() 
        
        


        
    return

if __name__ == "__main__":
    main()