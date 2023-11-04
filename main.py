# Import permutations
from itertools import permutations

#Write a FUNCTION to list all the permutations

def allpermutations(str):

  permlist = permutations(str)
  #Iterate through the LIST

  for perm in list(permlist):
    print(''.join(permlist))


#Call the Main Function
if __name__ == "__main__":
  str = "RADAR"

  #Call the Function
  allpermutations(str)


