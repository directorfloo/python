week = print("""
         
         Days of the week
          
           1 -> Monday
           2 -> Tuesday
           3 -> Wednessday
           4 -> Thursday
           5 -> Friday
           6 -> Saturday
           7 -> Sunday
          
            """)
menu = int(input('choose from the option: '))
match menu :
          case 1 :  
                  print("""
                    Monday""") 
          case 2 :  
                  print("""
                    Tuesday""") 
          case 3 :  
                  print("""
                    	Wednessday""") 
          case 4 :  
                  print("""
                    Thursday""") 
          case 5 :  
                  print("""
                    Friday""")
          case 6 :  
                  print("""
                    Saturday""")
          case 7 :  
                  print("""
                    Sunday""") 
          case  _:
                  print('Enter correct input')
  
             