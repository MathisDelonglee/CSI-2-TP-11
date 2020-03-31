class Rational:
    def __init__(self,Num, Den):
        self.__Num = Num
        self.__Den = Den

    def getNum(self):
        return self.__Num

    def getDen(self):
        return self.__Den

    def simplification(self,N,D):
        Numerateur = N
        Denominateur = D
        if D == 0:
            return False
        reste = N % D
        while reste != 0:
            N = D
            D = reste
            reste = N % D
        return (int(Numerateur/D),int(Denominateur/D))

    def __add__(self, objet):
       return Rational(self.__Num * objet.__Den + objet.__Num * self.__Den, self.__Den * objet.__Den)

    def __sub__(self, objet):
       return Rational(self.__Num * objet.__Den - objet.__Num * self.__Den, self.__Den * objet.__Den)

    def __mul__(self, objet):
       return Rational(self.__Num * objet.__Num , self.__Den * objet.__Den )

    def __truediv__(self, objet):
       return Rational(self.__Num * objet.__Den, self.__Den * objet.__Num)





if __name__=='__main__':
    c1 = Rational(2,6)
    c2 = Rational(1,7)
    c3 = c1 + c2
    c4 = c1 - c2
    c5 = c1 * c2
    c6 = c1 / c2

    c3a, c3b = c3.simplification(c3.getNum(),c3.getDen())
    print(str(c3a)+"/"+str(c3b))
    print("Instance :", isinstance(c3,Rational))

    print("**********")

    c4a, c4b = c4.simplification(c4.getNum(),c4.getDen())
    print(str(c4a)+"/"+str(c4b))
    print("Instance :", isinstance(c4,Rational))

    print("**********")

    c5a, c5b = c5.simplification(c5.getNum(),c5.getDen())
    print(str(c5a)+"/"+str(c5b))
    print("Instance :", isinstance(c5,Rational))

    print("**********")

    c6a, c6b = c6.simplification(c6.getNum(),c6.getDen())
    print(str(c6a)+"/"+str(c6b))
    print("Instance :", isinstance(c6,Rational))
    print("**********")
