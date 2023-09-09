def rfact(x):
  f=1
  if(x==0):
    return(1)
    f=x*rfact(x-1)
    return(f)
    printf("Factorial is"+str(rfact(5)))