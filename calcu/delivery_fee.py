

import math
import dateutil.parser

def delivery_fee_calculator(cart_value, delivery_distance, number_of_items, time_string):
    total_fees = 0 
    surcharge = 0


    #The delivery is free (0€) when the cart value is equal or more than 100€.
    if cart_value < 10000 :

        # If the cart value is less than 10€, a small order surcharge is added to the delivery price.
        if cart_value < 1000 :
            surcharge = 1000 - cart_value

        # A delivery fee for the first 1000 meters (=1km) is 2€. 
        # If the delivery distance is longer than that, 1€ is added for every additional 500 meters. 
        # that the courier needs to travel before reaching the destination

        if delivery_distance <= 1000:
            total_fees = 200
        else:

            total_fees = math.ceil(delivery_distance / 500 ) * 100

        # If the number of items is five or more, an additional 50 cent surcharge is added for each item above four

        if number_of_items >= 5 :
            total_fees += (number_of_items-4)* 50

        
        # Convert time format

        try:
            date_time = dateutil.parser.isoparse(time_string)
        except Exception as e:
            raise ValueError( f"Time:{time_string} Format Wrong") from e

        total_fees += surcharge

        # During the Friday rush (3 - 7 PM UTC), the delivery fee  will be multiplied by 1.1x.
        if date_time.weekday()==4 and 15 < date_time.hour < 19:
            total_fees *= 1.1


        total_fees = min(1500,int(total_fees))


    return total_fees 


if __name__ == '__main__':
    print(delivery_fee_calculator(790, 2235, 4, '2022-01-16T13:00:00Z'))