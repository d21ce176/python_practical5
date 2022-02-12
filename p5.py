from operator import truediv


def swap (b):
    output='';
    for paragraph in b:
        if paragraph.isupper()==True:
            output+=(paragraph.lower())
        else:
            output+=(paragraph.upper())
    return output
if __name__=='__main__':
    b=input()
    print(swap(b))
print("this program is prepared by om and id :d21ce176")  