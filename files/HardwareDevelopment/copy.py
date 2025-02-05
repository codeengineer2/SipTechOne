import sys

def process_beverages(beverages):
    print(f"Verarbeite die folgenden Getränke: {beverages}")

if len(sys.argv) > 1:
    received_data = sys.argv[1]
    beverages_tuple = tuple(received_data.split(','))
    
    print(f"Empfangene Daten: {beverages_tuple}")
    
    process_beverages(beverages_tuple)
    
else:
    print("Keine Getränke übergeben.")