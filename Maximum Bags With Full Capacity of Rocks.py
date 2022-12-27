class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        addition=[] #Using empty array to get space available in each bag
        full=0 #Using to count number of bags filled
        for cap,rock in zip(capacity,rocks): #loop through each bag
            addition.append(cap-rock) #append empty space value to array
        addition.sort() #sorting to fill bags with lesser space first
        for add in addition:
            if additionalRocks<1: #if there are no rocks end loop
                break
            if add==0: #if bag is full no need to add rock but count full bag
                full+=1
            elif add<=additionalRocks: #if space available is less than the additonal rocks available
                full+=1 #add count of full bag
                additionalRocks-=add #subtract rocks added to bag
        return full
