#defining computepay
import argparse

#def computepay(hrs,rate):
def main():
    hrs = int(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))
    if hrs <= 40:
        return hrs * rate
    elif hrs > 40:
     #defining extra hours
        extra = (40 * rate) + (hrs - 40) * (1.5 * rate)
        print(extra)
        


if __name__ == '__main__':
    
    helptitle = "This is my script"
    parser = argparse.ArgumentParser(description=helptitle)
    args = parser.parse_args()
    main()


