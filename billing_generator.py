import numpy as np

bill_number = 0
serial_number = 0
item_name = "name"
rate = 0
quantity = 0
price = 0

final_total = 0

# Range from 1 to 10
# TODO: for all ten

quantity_no_mapping_dic = {"एक":1,"दो":2,"तीन":3,"चार":4,"पांच":5,"छह":6,"सात":7,"आठ":8,"नौ":9,"दस":10}
rupee_mapping_dic = {"रुपय":"₹"}
quantity_mapping_dic = {"किलो":"kg","किलोग्राम":"kg","ग्राम":"g","केजी":"kg","बॉटल":"pc","पैकेट":"pc","पीस":"pcs"}
item_rate = {"सूजी":36,"आटा":27,"साबुत लाल मिर्च":400,"सौ एमएल हार्पिक लेवेंडर":66,"दो सौ एमएल हार्पिक लेवेंडर":120,"जानसन्स बेबी पाउडर":175,"ओरल बी":77,"सेरेलैक":290,"हगीज डायपर्स":475,"कोलगेट सेंसिटिव":90,"माहा लैक्टो":1}

#print(quantity_no_mapping_dic["एक"])


'''
['ढाई सौ ग्राम सूजी', 'चार के जी आटा सत्ताईस रुपये केजी वाला', 'छह', 'दस रुपये की साबुत लाल मिर्च', 'सौ एमएल हार्पिक लेवेंडर एक बॉटल', 'दो सौ एमएल हार्पिक लेवेंडर एक बॉटल', 'एक के लॉक्स', 'ओरल बी क्लास एक्शन टू ब्रश एक पैकेट', 'सेरेलैक बीट एप्पल एक पैकेट', 'हगीज डायपर्स एक पैकेट', 'एक पैकेट कोलगेट सेंसिटिव टूथ पर ब्रश']
['छह माहा लैक्टो']
'एक लिपटन चाय पत्ती', 'एक जानसन्स बेबी पाउडर', 'कोलगेट सेंसिटिव टूथब्रश एक पैकेट']
'''

#TODO: 
user_shoping_list = ["दो बॉटल हार्पिक लेवेंडर","दस रुपये की साबुत लाल मिर्च"]


modified_item = []


rate 

quantity = []
price = []

#print(rupee_mapping_dic["रुपय"])


for each_item in user_shoping_list:
    for number_mapping in quantity_no_mapping_dic:
        
        if number_mapping in each_item:
            print("here")
            print(number_mapping)

     
            
            print(str(quantity_no_mapping_dic[number_mapping]))

            # CHECK LOGIC
            if each_item.index(number_mapping) + 1 == "रुपये":
                
            rate.append(quantity_no_mapping_dic[number_mapping])
            
            new_each_item  = each_item.replace(number_mapping, str(quantity_no_mapping_dic[number_mapping]))
            modified_item.append(new_each_item)
            
        else:
            new_each_item = each_item

        
    
    print(modified_item)
    print(price)

    

'''

    if "एक" in each_item:
        new_each_item = each_item.replace("एक",str(quantity_no_mapping_dic["एक"]))
    else:
        new_each_item = each_item


'''



        
        
    
    
