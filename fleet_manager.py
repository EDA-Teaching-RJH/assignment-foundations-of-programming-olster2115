#to do list
#2.  `display_menu()`:  users full name, Prints the options and current student logged in and returns the user's choice.
    
#3.  `add_member(names, ranks, divs, ids)`:
    
    -   Validates ID is unique.
        
    -   Validates Rank is a valid TNG rank.
        
    -   Appends data to all 4 lists.
        
#4.  `remove_member(names, ranks, divs, ids)`:
    
    -   Asks for an ID.
        
    -   Finds the index.
        
    -   Removes the entry from _all 4 lists_ to keep them in sync.
        
#5.  `update_rank(names, ranks, ids)`:
    
    -   Finds a member by ID.
        
    -   Updates their rank string.
        
#6.  `display_roster(names, ranks, divs, ids)`:
    
    -   Iterates through the lists using `range(len(names))`.
        
    -   Prints a formatted table of all crew.
        
#7.  `search_crew(names, ranks, divs, ids)`:
    
    -   Asks for a search term.
        
    -   Prints any crew member whose name contains that term.
        
#8.  `filter_by_division(names, divs)`:
    
    -   Asks user for "Command", "Operations", or "Sciences".
        
    -   Prints only members in that division using `match` or `if` .
        
#9.  `calculate_payroll(ranks)`:
    
    -   Iterates through the ranks list.
        
    -   Assigns a credit value to ranks (e.g., Captain = 1000, Ensign = 200).
        
    -   Returns the total cost of the crew.
        
#10.  `count_officers(ranks)`:
    
	   -   Counts how many "Captain" and "Commander" ranks exist and returns the integer.


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
                True == N
                N == input(" idetify yourself")
                if N == True 
                        print("access granted welcome" + str(input) )
                        
                display_menu()
       
main()