#Task 1: The Area & Perimeter Tool (Functions & Return Values)
def calc_rectangle(length, width):
    area=length*width
    perimeter=2*(length+width)
    return(area,perimeter)
area, perimeter= calc_rectangle(8,5)
print("Area of rectangle:",area)
print("Perimeter of rectangle:",perimeter)
    
#Output: Area of rectangle: 40
#        Perimeter of rectangle: 26
   
    
