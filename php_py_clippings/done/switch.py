
#case _ is default, no break needed in each case

lang="Python"

match lang:
    case "JavaScript":
        print("a web developer.")

    case "Python":
        print("a Data Scientist")

    case "PHP":
        print("a backend developer")
    
    case _:
        print("The language doesn't matter.")
