def lengthAfterTransformations(s: str, t: int):
    if t == 0:
        return len(s)

    last_s = s 
    for _ in range(t):
        new_s = "" 
        for j in last_s:
            new_char_ascii = ord(j) + 1
            if new_char_ascii > 122:
                new_char_ascii = 97 + (new_char_ascii % 122)
                new_s += "a" + chr(new_char_ascii)
            else:
                new_s += chr(new_char_ascii)

        last_s = new_s
                
    return len(last_s)


def lengthAfterTransformations2(s: str, t: int):
    scale = 0
    for j in s:
        char = ord(j) - 97 + t
        if char > 25:
            curr_scale = char // 26
            scale += curr_scale
            for _ in range(curr_scale): 


    return len(s)


def main():
    length = lengthAfterTransformations("abcyy", 2)
    print(length)

    length = lengthAfterTransformations2("azbk", 1)
    print(length)

    length = lengthAfterTransformations("abcyy", 2)
    print(length)

    length = lengthAfterTransformations2("azbk", 1)
    print(length)

    length = lengthAfterTransformations2("jqktcurgdvlibczdsvnsg", 7517)
    print(length)


    
if __name__ == "__main__":
    main()
