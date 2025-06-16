"""
 This program provide to the user a list of proteins.
 Request for choice from the list. 
 Then redirects the user to RSCB to show the 3D structure 
 of the protein choosen.  
 """
import webbrowser

#On this dicctionary: key== name of the enzyme, value == a tuple with the PCB ID
# (unique 4-character code that identifies a 3D structure of a biological molecule ), 
# the corresponding URL on both NCBI and RSCB, numeber on the list

PROTEINS_VIEW_3D= {  
            'Hexokinasa': ('4F9O', 1, 'https://www.ncbi.nlm.nih.gov/Structure/pdb/4F9O', 'https://www.rcsb.org/structure/4F9O'),
            'Phosphoglucose isomerase': ('6XUH', 2, 'https://www.ncbi.nlm.nih.gov/Structure/pdb/6XUH' , 'https://www.rcsb.org/structure/6XUH'),
            'Phosphofructokinase':('7LW1', 3, 'https://www.ncbi.nlm.nih.gov/Structure/pdb/7LW1' , 'https://www.rcsb.org/structure/7LW1'),
            'Aldolase':('6XMH', 4 , 'https://www.ncbi.nlm.nih.gov/Structure/pdb/6XMH', 'https://www.rcsb.org/structure/6XMH'),
            'Triose phosphate isomerase': ('4ZVJ', 5, 'https://www.ncbi.nlm.nih.gov/Structure/pdb/4ZVJ' , 'https://www.rcsb.org/structure/4ZVJ'),
            'Glyceraldehyde-3-phosphate dehydrogenase': ('5C7L', 6, 'https://www.ncbi.nlm.nih.gov/Structure/pdb/5C7L' , 'https://www.rcsb.org/structure/5C7L'),
            'Phosphoglycerate kinase': ('2WZB',7, 'https://www.ncbi.nlm.nih.gov/Structure/pdb/2WZB' ,'https://www.rcsb.org/structure/2WZB'),
            'Phosphoglycerate mutase': ('7XB7', 8, 'https://www.rcsb.org/structure/7XB7', 'https://www.ncbi.nlm.nih.gov/Structure/pdb/7XB7'),
            'Enolase': ('5TD9', 9, 'https://www.ncbi.nlm.nih.gov/Structure/pdb/5TD9' , 'https://www.rcsb.org/structure/5TD9'),
            'Pyruvate kinase': ('6JFB', 10, 'https://www.ncbi.nlm.nih.gov/Structure/pdb/6JFB' , 'https://www.rcsb.org/structure/6JFB')
} 

#Intro to the user
print ('Hello, this program will show you a 3D structure of human enzymes ') 

print ('\nSelect the number corresponding to an enzyme from the list below: ')

# Displaying a menu of ezymes used on the glycolisis pathway
#.items recorre el diccionario completo (key,value pair) 
for key, data_v in PROTEINS_VIEW_3D.items():
    number_picked = data_v [1]
    print(f"{number_picked}. {key}")

#Ask for input 
while True:
        selected_number = input('\nEnter the number of the enzyme: ').strip().lower()
        selected_number = int(selected_number)

        #Creating a dictionary that only has number : name of the enzime. Using the PROTEIN_VIEW_3D dic
        number_to_protein = {data_v[1]: key for key, data_v in PROTEINS_VIEW_3D.items()}

        if selected_number in number_to_protein:
                protein_name = number_to_protein[selected_number]#accesing to the value through the key
                
                #Unpacking the values of the dictionary PROTEINS_VIEW_3D
                tuple_values = PROTEINS_VIEW_3D[protein_name] #accesing to the value through the key

                pdb_id = tuple_values[0]
                number = tuple_values[1]
                ncbi_url = tuple_values[2]
                rcsb_url = tuple_values[3]

                print(f"\nOpening RCSB structure for {protein_name} ({pdb_id})...")
                webbrowser.open(rcsb_url)
        else:print('Invalid number')
        #Ask the users if they want to see a different protein        
        continue_choice = input('\n Do you want to see another protein? (yes/ no):').strip().lower()
        if continue_choice not in ['yes', 'y']:
                print('Goodbye')
                break 
       
   
    

