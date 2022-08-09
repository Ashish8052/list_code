def isMagicSquare( mat) :
  n = len(mat)
  sumd1=0
  sumd2=0
  for i in range(n):
    sumd1+=mat[i][i]
    sumd2+=mat[i][n-i-1]
  if not(sumd1==sumd2):
    return False
  for i in range(n):
    sumr=0
    sumc=0
    for j in range(n):
      sumr+=mat[i][j]
      sumc+=mat[j][i]
    if not(sumr==sumc==sumd1):
      return False
  return True
mat = [ [ 2, 7, 6 ],
        [ 9, 5, 1 ],
        [ 4, 3, 8 ] ]
     
if (isMagicSquare(mat)) :
    print( "Magic Square")
else :
    print( "Not a magic Square")
    