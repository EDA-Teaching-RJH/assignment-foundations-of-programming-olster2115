def main():

        N = ["Michael Burnham" , "Saru" , "Hugh Culber" , "Paul Stamets" ,"Sylvia Tilly"]
        R = ["Captain" , "Lt Commander"  , "Doctor" , "Commander" ,"lieutenant"]
        D = ["Command","Command" ,"Medical" ,"Engineering","Engineering"]
        ID = ["1","2" ,"3" ,"4" ,"5"]
        
        def init_database ():
                print(N,R, D ,ID)
                return 1
                        
        init_database()
        def display_menu():
                print("Add Members:")
                print("Remove Members:")
                print("Update Members:")
                print("display Roster:")
                print("Search Crew:")
                print("Filter by Division:")
                print("Calculate Payroll:")
                print("Count Officers:")
                input("select a option:")
                return 
        display_menu()                            
        
       
main()