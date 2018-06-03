#commands = ["दो बॉटल हार्पिक लेवेंडर","दस रुपये की साबुत लाल मिर्च"]
commands = ["ढाई सौ ग्राम सूजी", "चार के जी आटा सत्ताईस रुपये केजी वाला"]
#, "छह", "दस रुपये की साबुत लाल मिर्च", "सौ एमएल हार्पिक लेवेंडर एक बॉटल", "दो सौ एमएल हार्पिक लेवेंडर एक बॉटल", "एक के लॉक्स", "ओरल बी क्लास एक्शन टू ब्रश एक पैकेट", "सेरेलैक बीट एप्पल एक पैकेट", "हगीज डायपर्स एक पैकेट", "एक पैकेट कोलगेट सेंसिटिव टूथ पर ब्रश"]
quantity_no_mapping_dic = {"एक":1,"दो":2,"तीन":3,"चार":4,"पांच":5,"छह":6,"सात":7,"आठ":8,"नौ":9,"दस":10}
entity_name  = []
quantity = []
cost = []

item_rate = {"सूजी":["Suji", 36],"आटा":["Atta", 27]}


def get_entity(command):

    entities = list(item_rate.keys())
    set_entity = "No Entity detected"
    
    for each_entity in entities:
        
        if each_entity in command:
            set_entity = each_entity

    return set_entity


# Will take a list of multilinqual voice commands and return corresponding list of quantity, cost, entity 
def assign_quantaties(commands,quantity_no_mapping_dic):

    tracker = 0

    for input_command in commands:
        print(input_command)
 
        
        split_command = input_command.split(" ")

        for number_mapping in list(quantity_no_mapping_dic.keys()):
            
            if number_mapping in split_command:
                next_target_position = (split_command.index(number_mapping)) + 1
            else:
                next_target_position = 0

        if split_command[next_target_position] == "रुपय" or split_command[next_target_position] == "रुपये" :
            print("detected rupees")
            
            cost.append(quantity_no_mapping_dic[split_command[next_target_position-1]])
            quantity.append(0)

                
            entity_name.append(item_rate[get_entity(input_command)][0])
            
        else:
            
            cost.append(0)
            quantity.append(0)

            # function to detect entity in a text!
            entity_name.append(item_rate[get_entity(input_command)][0])



    return quantity, cost, entity_name


quantity, cost, entity_name = assign_quantaties(commands,quantity_no_mapping_dic)
print("Cost")
print(cost)

print("Quantity")
print(quantity)

print("Entity")
print(entity_name)


