

hai=(87,34,90,11,45,76,34,12,20,87,55,54,87)
hello=["vikas","varun","balaji","hemsworth","vanathi","holland","aarthi"]


def filter():
    try:
        print(hello[int(input("Enter the index to read: "))])
    except ValueError as ve:
        print(ve,"\nValue should be numeric format")
        try:
            print(hello[int(input("Enter the index to read: "))])
        except IndexError as ie:
            print(ie,"\nIndex should within",len(hello))
            print(hello[int(input("Enter the index to read: "))])    
    except IndexError as ie:
        print(ie,"\nIndex should within",len(hello))
        print(hello[int(input("Enter the index to read: "))])
    finally:
        print("Work has done")


filter()