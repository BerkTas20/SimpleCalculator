#add toplama                                   #BEGİNNER LEVEL - BAŞLANGIŞ SEVİYESİ
#extraction çıkarma                  
#multiple çarpma                   
#divide bölme

def add(x , y):
    return x + y


def extraction(x , y):
    return x - y

def multiple(x , y):
    return x * y


def divide(x , y):
    return x / y

print("Select Operation")
print("1.Add")
print("2.Extraction")
print("3.Multiple")
print("4.Divide")

while True:

    choice = input("Enter choice(1/2/3/4) : ")
   
    if choice in ('1','2','3','4'):
            num1 = float(input("Enter  first number: "))
            num2 = float(input("Enter second number: "))
        
                

            

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", extraction(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiple(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            break
    else:
        print("Invalid Input")    
        
