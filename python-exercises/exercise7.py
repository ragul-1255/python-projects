credit_card=input("enter your credit card number: ")
sum_odd_digits=0
sum_even_digits=0
total=0
credit_card=credit_card.replace('-','')
credit_card=credit_card.replace(" ",'')
credit_card=credit_card[::-1]
for i in credit_card[::2]:
    sum_odd_digits+=int(i)        
    '''
    
| Parameter          | When step > 0 | When step < 0  |
| ------------------ | ------------- | -------------- |
| start (if omitted) | 0             | `len(var) - 1` |
| stop (if omitted)  | `len(var)`    | `-1`           |

    '''
    
for j in credit_card[1::2]:
    even=int(j)*2
    if even>=10:
        sum_even_digits+=(1+(even%10))
    else:
        sum_even_digits+=even
total=sum_odd_digits+sum_even_digits
if total%10==0:
    print("valid number")
else:
    print("the number is invalid")    