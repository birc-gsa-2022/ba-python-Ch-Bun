"""Module for computing border arrays."""


def border_array(x: str) -> list[int]:
    #edge case
    if x == "":
        return []
    #built border array
    ba = [0]*len(x)
    
    #otherwise run trough seq
    for i in range(1, len(x)):
        b = ba[i-1]
        #extend border
        while (b > 0) and (x[i] != x[b]):
            b = ba[b-1]
        #if matches
        if(x[i]==x[b]):
            ba[i] = b + 1
        else:
            ba[i] = 0

    return ba


def strict_border_array(x: str) -> list[int]:
    # #edge case
    # if x == "":
    #     return []
        
    # ba = border_array(x)
    # #built border array
    # bax = [0]*len(x)
    
    # #otherwise run trough seq
    # for i in range(len(x)-1):
    #     if (ba[i] != 0 and x[ba[i]] != x[i+1]):
    #         bax[i] = ba[i]
    #     #Search for shorter border
    #     elif(ba[i] != 0 and x[ba[i]] == x[i+1]):
    #         for j in range(1,ba[i]):
    #             if (x[ba[i]-j] != x[i+1] and x[0:ba[i]-j]==x[i-ba[i]+j+1: i+1]):
    #                 bax[i] = ba[i]-j
    #                 break
    #     else:
    #         bax[i] = 0
    # bax[len(x)-1] = ba[len(x)-1]
    # return bax


    ba = border_array(x)
    bax = []
    for i, bai in enumerate(ba):
        if bai == 0:
            bax.append(0)
        elif i == (len(x)-1) or x[i+1] != x[bai]:
            bax.append(bai)
        #longest border not strict -> so we search down the borders 
        # if longest wasn't stikt we checck the shorter where we already know that it is not extendable
        else:
            bax.append(bax[bai-1])
    return bax

def main():
    
    #Test
    print(border_array("aaba"))
    #[0, 1, 0, 1]
    print(border_array("abaabaa"))
    #[0,0,1,1,2,3,4]
    print(border_array("ississippi"))
    #[0, 0, 0, 1, 2, 3, 4, 0, 0, 1]
    print(border_array(""))
    #[]

    print(strict_border_array("aaba"))
    #[0, 1, 0, 1]
    print(strict_border_array("aaaba"))
    #[0, 0, 2, 0, 1]
    print(strict_border_array("abaabaa"))
    #[0,0,1,0,0,1,4]
    print(strict_border_array("ississippi"))
    #[0, 0, 0, 0, 0, 0, 4, 0, 0, 1]
    print(strict_border_array(""))
    #[]

if __name__ == '__main__':
    main()