def several_zeros():
    return ([0]*10)
pass

def several_zeros_custom(nb_zeros=10):
    return nb_zeros*[0]
pass

def matrix(rows=3, cols=3):
     return(rows*[cols*[0]])
pass  

class Matrix:
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.__matrice=rows*[cols*[0]]
    
    def voirMatrice(self):
        return(self.__matrice)
    
    def get_value(self, row, col):
        return self.__matrice[row][col]
   
    def __eq__(self, other):
        if self.__matrice == other.__matrice:
            return True
        else:
            return False

def my_sort(my_list: [int]) -> list[int]:
    b=my_list.copy()
    for i in range(len(b)-1):
        for j in range(len(b)-1):
            if b[j]>b[j+1]:
                a=b[j]
                b[j]=b[j+1]
                b[j+1]=a
    return b
pass

if __name__ =='__main__':
   
    print(several_zeros())
    print(several_zeros_custom(3))
    print(matrix(3,2))
    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    print(m1 == m2)  # True
    print(m1.get_value(1, 2))  # 0
    my_list=[15,12,9,8,10,3]
    sorted_list=my_sort(my_list)
    print("Liste originale:", my_list)
    print("Liste triée:", sorted_list)
pass
