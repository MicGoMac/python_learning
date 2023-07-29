#https://stackoverflow.com/questions/52155591/how-to-insert-string-into-a-string-as-a-variable

EnemyHealth = 0  

EnemyIs = 'dead'

#using format
op = "The Enemy's health is {} The Enemy is {}".format(EnemyHealth, EnemyIs)

#using placeholder
op2 = "The Enemy's health is %d. The Enemy is %s." % (EnemyHealth, EnemyIs)

'''
print(op)
print(op2)
'''
