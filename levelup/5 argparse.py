import argparse
import math

def cylinder_V(radius,height):

    vol = (math.pi)*(radius**2)*height
    return vol

parser = argparse.ArgumentParser(description='Cylinder 계산하라')
parser.add_argument('-r','--radius',type=int,help='반지름 값')
parser.add_argument('-H','--height',type=int,help='높이') # h로 쓰면 height와 충돌
args = parser.parse_args()

if __name__ == '__main__':
    print(cylinder_V(args.radius,args.height))

