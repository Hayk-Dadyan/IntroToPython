import Productcheck

def buy(product, num, price):
    if Productcheck.check(product, num) is True:
        print ('You bought %s and spent %s.' % (product, (num*price)))
    else:
        print ('Sorry! We are out of this product.')
    
def main():
    buy('candy', 5, 25)
    buy('ice cream', 10, 30)
    buy('pen', 40, 15)


if __name__ == '__main__':
    main()
