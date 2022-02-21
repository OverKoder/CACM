
def main():


    while (True):
        
        numerator, denominator = [int(elem) for elem in input().split()]
        if numerator == 1 and denominator == 1:
            return
        solution = ""
    
        left_num, left_denom = 0,1
        center_num, center_denom  = 1,1
        right_num, right_denom = 1,0

        number = numerator / denominator

        while (center_num != numerator or center_denom != denominator):

            aux = center_num / center_denom

            if ( number > aux):
                left_num = center_num; left_denom = center_denom
                solution += "R"
            
            elif (number < aux):
                right_num = center_num; right_denom = center_denom
                solution += "L"
            

            center_num = left_num + right_num
            center_denom = left_denom + right_denom
        
        print(solution)
    
    return 


if __name__ == "__main__":
    main()