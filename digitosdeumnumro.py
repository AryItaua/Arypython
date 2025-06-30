num  =  int ( input ( "Digite um número: " )) 
count  =  0 
for  digit  in  str ( abs ( num )):   
    count  +=  1
print ( "Número total de dígitos:" ,  count )