import numpy as np
import datetime
import voice_input as vi


#commands = ["दो बॉटल हार्पिक लेवेंडर","दस रुपये की साबुत लाल मिर्च"]
#commands = ["ढाई सौ ग्राम सूजी", "चार के जी आटा सत्ताईस रुपये केजी वाला"]
commands = ["सूजी दो किलो","आटा आधा किलो","एक्लेयर्स तीन पैकेट"]
#, "छह", "दस रुपये की साबुत लाल मिर्च", "सौ एमएल हार्पिक लेवेंडर एक बॉटल", "दो सौ एमएल हार्पिक लेवेंडर एक बॉटल", "एक के लॉक्स", "ओरल बी क्लास एक्शन टू ब्रश एक पैकेट", "सेरेलैक बीट एप्पल एक पैकेट", "हगीज डायपर्स एक पैकेट", "एक पैकेट कोलगेट सेंसिटिव टूथ पर ब्रश"]
quantity_no_mapping_dic = {"एक":1,"दो":2,"तीन":3,"चार":4,"पांच":5,"छह":6,"सात":7,"आठ":8,"नौ":9,"दस":10, "ढाई सौ": 150, "आधा": 0.5}
entity_name  = []
quantity = []
price = []
cost = []


item_rate = {"सूजी":["Suji", 36],"आटा":["Atta", 27]}
#item_rate = { "सूजी":["Sooji", 36], "आटा":["Atta", 27], "कोलगेट सेंसिटिव टूथब्रश":["Colgate sensitive toothbrush", 90], "कोलगेट टूथपेस्ट सौ ग्राम ":["Colgate toothpaste (100g)", 56], "डेटोल लिक्विड पांच सौ एमएल":["Dettol Liquid (500 ml)", 141], "एक्लेयर्स":["Eclairs", 1], "गार्नियर मेन पॉवरव्हाइट":["Garnier Men Facewash Power White", 180], "हार्पिक लैवेंडर सौ एमएल":["Harpic Lavendar (100 ml)", 66], "हगीस डाइपर्स":["Huggies Diapers", 475], "केलोग्स चौकोस":["Kellogs Chocos", 275], "लिप्टन दार्जीलिंग टी ढाई सौ ग्राम ":["Lipton darjeeling tea (250 g)", 365], "मैगी नूडल्स पैक ऑफ़ फोर ":["Maggi Noodles (pack of 4)", 40], "सफोला गोल्ड दो लीटर ":["Saffola Gold (2 lt)", 235], "लिप्टन दार्जीलिंग टी ढाई सौ ग्राम ":["Lipton darjeeling tea (250 g)", 365], "सर्फ एक्सेल मैटिक दो केजी ":["Surf Excel Matic (2 kg)", 330], "कैडबरी डैरीमिल्क":["Cadbury Dairymilk", 22] }
item_rate = {"सूजी":["Sooji", 36, 0.036, "किलो", "ग्राम"], "आटा":["Atta", 27, 0.027, "किलो", "ग्राम"], "कोलगेट सेंसिटिव टूथब्रश":["Colgate sensitive toothbrush", 90, 90, "पैकेट", "पीस" ], "कोलगेट टूथपेस्ट ":["Colgate toothpaste (100g)", 56, 56, "पैकेट", "पीस"], "डेटोल लिक्विड":["Dettol Liquid (500 ml)", 141, 141, "पैकेट", "पीस"], "एक्लेयर्स":["Eclairs", 1, 1, "पैकेट", "पीस"], "गार्नियर मेन":["Garnier Men Facewash Power White", 180, 180, "पैकेट", "पीस"], "हार्पिक लैवेंडर":["Harpic Lavendar (100 ml)", 66, 66, "पैकेट", "पीस"], "हगीज डायपर्स":["Huggies Diapers", 475, 475, "पैकेट", "पीस"], "के लॉग्स":["Kellogs Chocos", 275, 275, "पैकेट", "पीस"], "लिप्टन दार्जीलिंग टी":["Lipton darjeeling tea (250 g)", 365, 365, "पैकेट", "पीस"], "मैगी नूडल्स":["Maggi Noodles (pack of 4)", 40, 40, "पैकेट", "पीस"], "सफोला गोल्ड ":["Saffola Gold (2 lt)", 235, 235, "पैकेट", "पीस"], "लिप्टन दार्जीलिंग टी":["Lipton darjeeling tea (250 g)", 365, 365, "पैकेट", "पीस"], "सर्फ एक्सेल":["Surf Excel Matic (2 kg)", 330, 330, "पैकेट", "पीस"], "कैडबरी डेयरी मिल्क":["Cadbury Dairymilk", 22, 22, "पैकेट", "पीस"]}


def map_to_number(hindi_quant):
    english_mapping = int("0")

    print("Hindi:" + hindi_quant)
    for number_mapping in list(quantity_no_mapping_dic.keys()):

        if number_mapping ==  hindi_quant:
            english_mapping = float(quantity_no_mapping_dic[hindi_quant])

    return english_mapping


def get_entity(command):
    entities = list(item_rate.keys())
    set_entity = "No entity detected"
    
    for each_entity in entities:
        
        if each_entity in command:
            set_entity = each_entity

    return set_entity


def get_quantity(command):

    set_quantity = "No quantity detected"

    entity = get_entity(command)
    split_command = command.split(" ")

    print(split_command)

    if "सूजी" or "आटा" in split_command:

        if "किलो" in split_command:
            print("KG detected")
            quant_index = split_command.index("किलो") - 1
            quant_hindi = split_command[quant_index]
        elif "ग्राम" in split_command:
            print("G detected")
            quant_index = split_command.index("ग्राम") - 1
            quant_hindi = split_command[quant_index]
        elif "पैकेट" in split_command:
            quant_index = split_command.index("पैकेट") - 1
            quant_hindi = split_command[quant_index]
        elif "पीस" in split_command:
            quant_index = split_command.index("पीस") - 1
            quant_hindi = split_command[quant_index]
        else:
            print("Else")

    quant_index  = split_command.index(entity) - 1
    #print("Quant index:" + str(quant_index))
    #quant_hindi = split_command[quant_index]

    print("PASSED for conversion:" + str(quant_hindi))
    quant = map_to_number(quant_hindi)
    print("Quant:" + str(quant))

    set_quantity = quant

    '''
    if "किलो" in split_command:
        set_quantity = item_rate[entity][1] * quant

    elif "ग्राम" in split_command:
        set_quantity = item_rate[entity][2] * quant

    elif  "पैकेट" in split_command or "पीस" in split_command:
        set_quantity = item_rate[entity][1] * quant

    else:
        set_quantity = "No quantity detected."
    '''
    return set_quantity


def get_price(command):

    set_price  = 0

    entity = get_entity(command)
    quant  = get_quantity(command)

    split_command = command.split(" ")

    if "किलो" in split_command:
        set_price = item_rate[entity][1]

    elif "ग्राम" in split_command:
        set_price = item_rate[entity][2]

    elif  "पैकेट" in split_command or "पीस" in split_command:
        set_price = item_rate[entity][1]

    else:
        set_price = "No quantity detected."


    return set_price


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
            
            price.append(quantity_no_mapping_dic[split_command[next_target_position-1]])
            
            price.append(get_price(input_command))
            quantity.append(get_quantity(input_command))

                
            entity_name.append(item_rate[get_entity(input_command)][0])
            
        else:
            
            price.append(get_price(input_command))
            quantity.append(get_quantity(input_command))

            # function to detect entity in a text!
            entity_name.append(item_rate[get_entity(input_command)][0])



    return quantity, price, entity_name


def compute_final_price(entity_name, quantity, price):

    np_quantity = np.array(quantity)
    np_price = np.array(price)
    np_entity_name = np.array(entity_name)
    np_cost = np_quantity * np_price
    final_total = np_cost.sum()

    return final_total, np_cost


def print_invoice(entity_name, quantity, price, np_cost, final_total):
    print("Price")
    print(price)

    print("Quantity")
    print(quantity)

    print("Entity")
    print(entity_name)

    print("Cost:")
    print(np_cost)

    print("Total Amount:")
    print(final_total)

    print("\n")

    print("================================================================")
    print("MULTI LINGUAL VOICE ASSISTANT" + "    " + "DATE:" + str(datetime.datetime.now()))
    print("================================================================")

    counter = 0


    for serial_number in range(len(entity_name)):
        print(str(counter + 1) + ". " +str(entity_name[counter]) + "    " + str(quantity[counter]) + str(price[counter]) )
        counter = counter + 1


    print("TOTAL: " + str(final_total))
    print("================================================================")

def main():

    commands = vi.get_voice_input()
    quantity, price, entity_name = assign_quantaties(commands,quantity_no_mapping_dic)
    final_total, np_cost  = compute_final_price(entity_name, quantity, price)
    print_invoice(entity_name, quantity, price, np_cost, final_total)



main()



