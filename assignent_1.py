def lower(row, col):

    
    for i in range(0, row):
    
        for j in range(0, col):
        
            if (i < j):
            
                print(" ", end = " ");
            
            else:
                print("*",end = " " );
        
        print(" ");
    
# Function to form upper triangular matrix
def upper(row, col):

    for i in range(0, row):
    
        for j in range(0, col):
        
            if (i > j):
                print(" ", end = " ");
            
            else:
                print("*", end = " " );
        
        print(" ");

def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()
  


row = int(input("Enter the number of rows: "));
col = int(input("Enter the number of columns:"));
n= int(input("Enter the size of pyramid:")); 

print("Lower triangular matrix: ");
lower(row, col);
    
print("Upper triangular matrix: ");
upper(row, col);

print("Pyramidical matrix: ");
full_pyramid(n);