import sys

print("Argument List:", str(sys.argv))



def test1():
	t="""abc
ghi"""

	print(t)


def test2():
	print ("this is test2")

got_argv = sys.argv[1]

print(got_argv)
exit()

'''
#this need python 10 or above
match got_argv:
	case "test1":
		test1()

	case "test2":
		test2()

	case _:
		print ( "Pls give a param which is the name of the function" )
'''
