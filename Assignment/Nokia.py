Nokia = print("""
         
         Welcome to your Nokia phone 3310
     
     1-> Phone book
     2-> Message
     3-> Chat
     4-> Call register
     5-> Tones
     6-> Settings
     7-> Call divert
     8-> Games
     9-> Calculator
    10-> Reminders
    11-> Clock
    12-> Profiles
    13-> SIM services
""")          
menu = int(input('choose from the option: '))
match menu :
      case 1 : 
              phonebook = print("""
                        Phone book:
                        1.Search
                        2.Service Nos
                        3.Add name
                        4.Erase
                        5.Edit
                        6.Assign tone
                        7.Send b' card
                        8.Option
                        9.Speed dials
                        10.Voice tags
                                  """)
                         
              phonebook = int(input('choose from the Phonebook option: '))
              match phonebook :
                      case 1 : 
                               print('Search') 
                      case 2 :  
                               print('Service Nos')
                      case 3 :  
                               print('Add name')
                      case 4 :  
                               print('Erase')
                      case 5 :  
                               print('Edit')
                      case 6 :  
                               print('Assign tone')
                      case 7 :  
                               print('Send b card')
                      case 8 :  
                               print("""
                               1.Type of view
                               2.Memory status  
                                     """)
                               option = int(input('choose Option: '))
                               match option :
                                      
                                        case 1 :
                                               print('Type of view')
                                        case 2 : 
                                               print('Memory status')
                                        case _:
                                               print('Enter correct input')
                      case 9 :  
                               print('Speed dials')
                      case 10 :  
                               print('Voice tags')
                      case _:
                               print('Enter correct input')
      case 2 :
              message = print("""
                      1.Write messages
                      2.Inbox
                      3.Outbox
                      4.picture messages 
                      5.Templates
                      6.Smileys
                      7.Message settings
                      8.Info service
                      9.Voice mailbox number
                      10.Service command editor
                                """)
              message = int(input('choose from the Message option: '))
              match message :
                        case 1 : 
                                 print('Write messages') 
                        case 2 :   
                                 print('Inbox')
                        case 3 :  
                                 print('Outbox')
                        case 4 :  
                                 print('picture messages')
                        case 5 :  
                                 print('Templates')
                        case 6 :  
                                 print('Smileys')
                        case 7 :  
                                 print("""
                                 1. Set 
                                 2. Commom  
                                     """)
                                 message_setting = int(input('choose option: '))
                                 match message_setting :
                                    case 1 :
                                             print("""
                                             1. Message Center number
                                             2. Message sent as
                                             3. Message validity
                                             """)
                                             set = int(input('choose an option: '))
                                             match set :
                                                        case 1 :
                                                                print('Message Center number')
                                                        case 2 : 
                                                                print('Message sent as')
                                                        case 3 :
                                                                print('Message validity')
                                                        case _:
                                                               print('Enter correct input')
                                    case 2 :
                                             print("""
                                             1.Delivery reports
                                             2.Reply via same centre
                                             3.Character support
                                              """)
                                             common = int(input('choose an option: '))
                                             match common :
                                                          case 1 :
                                                                  print('Delivery reports')
                                                          case 2 : 
                                                                  print('Reply via same centre')
                                                          case 3 :
                                                                  print('Character support') 
                                                          case _:
                                                                  print('Enter correct input')
                        case 8 :
                                 print('Info service')
                        case 9 :
                                 print('Voice mailbox numer') 
                        case 10 :
                                 print('Service command editor') 
                        case _:
                                 print('Enter correct input')
      case 3 :  
              print("""
                Chat""")    
      case 4 : 
              print("""
              1.Missed calls
              2.Recieved calls
              3.Dialled numbers
              4.Erase recent call lists
              5.Show call duration
              6.Show call costs
              7.Call costs settings
              8.Prepaid credit
                      """)
              call_register = int(input('choose from the call register option: '))
              match call_register:
                        case 1 : 
                                 print('Missed calls') 
                        case 2 :   
                                 print('Recieved calls')
                        case 3 :  
                                 print('Dialled numbers')
                        case 4 :  
                                 print('Erase recent call lists')
                        case 5 : 
                                 print("""
                                 1.Last call duration
                                 2.All calls' duration
                                 3.Received calls' duration
                                 4.Dialled calls' duration
                                 5.Clear timers
				       """) 
                                 duration = int(input('choose an option: '))
                                 match duration :
                                                 case 1 :
                                                           print('Last call duration')
                                                 case 2 : 
                                                           print('All calls duration')
                                                 case 3 :
                                                           print('Received calls duration')
                                                 case 4 :
                                                           print('Dialled calls duration')
                                                 case 5 :
                                                           print('Clear timers')
                                                 case _:
                                                           print('Enter correct input')
                        case 6 :
                                 print("""
                                 1.last call costs
                                 2.All calls' cost
                                 3.Clear counters
                                       """)
                                 show = int(input('choose an option: '))
                                 match show :
                                             case 1 :
                                                     print('last call costs')
                                             case 2 : 
                                                     print('All calls cost')
                                             case 3 :
                                                     print('Clear counters')
                                             case _:
                                                     print('Enter correct input')
                        case 7 :
                                  print("""
                                  1.Call cost Limit
                                  2.Show costs in
                                        """)
                                  show = int(input('choose an option: '))
                                  match show :
                                             case 1 :
                                                     print('Call cost Limit')
                                             case 2 : 
                                                     print('Show costs in')
                                             case _:
                                                     print('Enter correct input')
                        case 8 : 
                                print('Prepaid credit')
                        case _:
                                print('Enter correct input')
      case 5 : 
                print("""
                1.Ringing tone
                2.Ringing volume 
                3.Incoming call Alert
                4.Composer
                5.Message alert tone
                6.keypad tones 
                7.Warning and game tones
                8.Vibrating alert
                9.Screen Saver
                         """)
                tones  = int(input('choose from the Tones option: '))
                match tones :
                        case 1 : 
                                 print('Ringing tone') 
                        case 2 :   
                                 print('Ringing volume')
                        case 3 :  
                                 print('Incoming call Alert')
                        case 4 :  
                                 print('Composer')
                        case 5 :  
                                 print('Warning and game tone')
                        case 6 :  
                                 print('keypad tones')
                        case 7 :  
                                 print('Warning and game tones')
                        case 8 :  
                                 print('Vibrating alert')
                        case 9 :  
                                 print('Screen Saver')
                        case _:  
                                 print('Enter correct input')
      case 6 :
                print("""
                1.Call settings
                2.Phone settings
                3.Security setting
                4.Restore factory settings
                      """)

                settings = int(input('choose from the settings option: '))
                match settings :
                               case 1: 
                                       print("""
                                       1.Automatically redial
                                       2.Speed dialling
                                       3.Call Waiting options
                                       4.Own number sending
                                       5.Phone line in use
                                       6.Automatic answer 
                                               """)
                                       automatically = int(input('choose an option: '))
                                       match automatically :
                                             case 1 :
                                                     print('Automatically redial')
                                             case 2 : 
                                                     print('Speed dialling')
                                             case 3 : 
                                                     print('Call Waiting options')
                                             case 4 : 
                                                     print('Own number sending')
                                             case 5 : 
                                                     print('Phone line in use')
                                             case 6 : 
                                                     print('Automatic answer')
                                             case _:
                                                     print('Enter correct input')
                               case 2:
                                       print("""
                                       1.Language 
                                       2.Cell info display
                                       3.Welcome note
                                       4.Network selection
                                       5.Lights
                                       6.Confirm SIM service actions
                                             """)
                                       language = int(input('choose an option: '))
                                       match language :
                                             case 1 :
                                                     print('Language')
                                             case 2 : 
                                                     print('Cell info display')
                                             case 3 : 
                                                     print('Welcome note')
                                             case 4 : 
                                                     print('Network selection')
                                             case 5 : 
                                                     print('Lights')
                                             case 6 : 
                                                     print('Confirm SIM service actions')
                                             case _:
                                                     print('Enter correct input')  
                               case 3: 
                                       print("""
                                       1.PIN code request
                                       2.Call barring service
                                       3.Fixed dialling
                                       4.Closed user group
                                       5.Phone security
                                       6.Change access codes
                                                 """)
                                       pin = int(input('choose an option: '))
                                       match pin :
                                             case 1 :
                                                     print('PIN code request')
                                             case 2 : 
                                                     print('Call barring service')
                                             case 3 : 
                                                     print('Fixed dialling')
                                             case 4 : 
                                                     print('Closed user group')
                                             case 5 : 
                                                     print('Phone security')
                                             case 6 : 
                                                     print('Change access codes')
                                             case _:
                                                     print('Enter correct input')
                               case 4 : 
                                        print('Restore factory settings')
                               case _:
                                        print('Enter correct input')
      case 7 :
               print("""
               Call divert
                     """)              
      case 8 :
               print("""
               Games
                     """)
      case 9 :
               print("""
               Calculator
                     """)
      case 10 :
               print("""
               Call divert
                     """)
      case 11 :
               print("""
               1.Alarm Clock
               2.Clock settings
               3.Date setting
               4.Stopwatch
               5.Countdown timer
               6.Auto update of date time
                     """)
               alarm = int(input('choose from the  option: '))
               match alarm :
                        case 1 : 
                                 print('Alarm Clock') 
                        case 2 :   
                                 print('Clock settings')
                        case 3 :  
                                 print('Date setting')
                        case 4 :  
                                 print('Stopwatch')
                        case 5 :  
                                 print('Countdown timer')
                        case 6 :  
                                 print('Auto update of date time')
                        case _:  
                                 print('Enter correct input')
      case 12 : 
               print("""
                 Profiles
                    """)
      case 13 :
               print("""
                 SIM services
                    """) 
               
                 
                                      

 







 