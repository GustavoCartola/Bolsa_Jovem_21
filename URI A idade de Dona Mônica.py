M = int(input())
A = int(input())
B = int(input())

C = M - (A + B)

if M >=40:
 if M <=110:
  if A>=1:
   if A<M:
    if B>=1:
     if B<M:
      if A != B:
       if A > B and A > C:
        print(A)
       elif B > A and B > C:
         print(B)
       elif C > A and C > B:
        print(C)