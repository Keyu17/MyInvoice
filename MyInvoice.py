# Econ HVAC

file = input("File Name: ")
date = input("Date:")
invoice_no = input("Invoice No.: ")
to = input("Company's Name: ")
address = input("Company's Address: ")
fobj = open(file, "w", encoding="utf-8")
fobj.write("\t\t\t\t\t\t\t\tINVOICE\n")
fobj.write('\n')
fobj.write("Econ HVAC\n")
fobj.write("1125 Rue Renoir\t\t\t\t\t\t\t\t\t\t\t\t\tDate: "+date+'\n')
fobj.write("Brossard, QC J4X 2G7\t\t\t\t\t\t\t\t\t\t\t\tInvoice No."+invoice_no+'\n')
fobj.write('\n')
fobj.write("To: "+to+'\n')
fobj.write('    '+address+'\n\n')

fobj.write("Quantity\t\t\tDescription\t\t\t\t\t\tUnit Price\t\tTotal Price\n")

number = 0
subtotal = 0
def products_sold(quantity, description, unit_price, total_price, space):
    if space == '':
        fobj.write(quantity+'\t\t\t\t'+description+'\t\t\t\t\t'+str(unit_price)+'\t\t\t'+str(total_price)+'\n')
    else:
        fobj.write(quantity+'\t\t\t\t'+description+'\t\t\t\t\t'+str(unit_price)+'\t\t\t'+str(total_price)+'\n'+'\t\t\t\t\t  '+space+'\n')
 



while number < 100:
    question = input('Add new product？')
    if question == 'y'or question == 'Y' or question == 'yes' or question == 'yes ':
        des = input('Desciption: ')
        quantity = input('Quantity: ')
        u_price = input('Unit Price: ')
        t_price = round(int(quantity)*int(u_price), 2)
        subtotal += t_price
        if len(des) == 21:
            space = ''
            products_sold(quantity, des, u_price, t_price, space)
            number += 1
        elif len(des) < 21:
            num_des = len(des)
            
            while num_des < 21:
                des += ' '
                num_des += 1
            
            space = ''
            products_sold(quantity, des, u_price, t_price, space)
            number += 1
        else:
            newdes = des[:21]
            space = des[21:]
            products_sold(quantity, newdes, u_price, t_price, space)
            number += 1
        
    else:
        number = 100
    
TPS = round((subtotal*0.05), 2)
TVQ = round((subtotal*0.09975), 2)
total = round((subtotal+TPS+TVQ), 2)

fobj.write('\n\t\t\t\t\t\t\t\t\t\t\tSubtotal\t\t'+ str(subtotal) +'\n')
fobj.write('\t\t\t\t\t\t\t\t\t\t\tTPS\t\t\t'+ str(TPS) + '\n')
fobj.write('\t\t\t\t\t\t\t\t\t\t\tTVQ\t\t\t' + str(TVQ) + '\n')
fobj.write('\t\t\t\t\t\t\t\t\t\t\tTotal\t\t\t'+ str(total))
fobj.write('\nTPS: 802475939 RT0001\n')
fobj.write('TVQ: 1220515717 TQ0001\n')



fobj.close()
