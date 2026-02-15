def main(N:list[str],R:list[str],D:list[str],ID:list[str]):

        N = ["Michael Burnham" , "Saru" , "Hugh Culber" , "Paul Stamets" ,"Sylvia Tilly"]
        R = ["Captain" , "Lt Commander"  , "Doctor" , "Commander" ,"lieutenant"]
        D = ["Command","Command" ,"Medical" ,"Engineering","Engineering"]
        ID = ["1","2" ,"3" ,"4" ,"5"]
        
        def init_database(N:list[str],R:list[str],D:list[str],ID:list[str]):
                print(N,R,D,ID)
                return 
                        
        init_database()
        def display_menu(N:list[str],R:list[str],D:list[str],ID:list[str]):
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
        
        def add_members(N:list[str],R:list[str],D:list[str],ID:list[str]):
                print("add member")
                N = input("")
                print("add rank")
                R = input("")
                print("add division")
                D= input("")
                print("Add ID")
                ID = input("")
                if ID in ID:
                        print("ID already in use try again")
                        return
                if R not in R:
                        print("rank does not exist")
                        return
                N.append(N)
                R.append(R)
                D.append(D)
                ID.append(ID) 
                
                return
        add_members()
       
        def remove_member(N:list[str],R:list[str],D:list[str],ID:list[str]):
                N = input("Name to remove")
                database = N.index
                N.pop(database)
                R.pop(database)   
                D.pop(database)
                ID.pop(database)
                
                return        
        remove_member()

        def update_rank(N:list[str],R:list[str],D:list[str],ID:list[str]):
                IDF = ID.find(input(""))
                print(IDF)
                R.append(R)
                return
        update_rank()
        
main()