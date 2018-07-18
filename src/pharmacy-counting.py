file_in=open("input/itcont.txt","r") # read file input
file_out=open("test_1/output/top_cost_drug.txt","w") # write file output

drugs={}# drugs store drug_name, num_prescriber, total_cost

next(file_in)# jump the first line
for line in file_in:# loop every line of the file
    line=line.strip().split(',')# split the line with ','
    drug_name=line[3]#get the drug_name
    drug_cost=int(line[4])# get the drug_cost
    if drug_name not in drugs: # if the drug is not in the drugs dict, then set the num_prescriber and total_cost to zeros
        drugs[drug_name]=[0,0]
    drugs[drug_name][0]+=1 # the num_prescriber add 1
    drugs[drug_name][1]+=drug_cost # the total_cost accumulate

drugs_list=[] # drugs_list for store all the information to sort them
for name in drugs:# change the drugs dict to drugs_list
    drugs_list.append([name,drugs[name][0],drugs[name][1]])
drugs_list.sort(key=lambda x:x[2],reverse=True)#sort the drugs_list


file_out.write("drug_name,num_prescriber,total_cost\n")#write the first line
for line in drugs_list:
    line = line[0]+','+str(line[1])+','+str(line[2])+'\n'#change the int to str to write them into the file
    file_out.write(line)
#close these two file
file_in.close()
file_out.close()
