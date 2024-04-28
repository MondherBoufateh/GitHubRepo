
def main():

    import pandas as pd
    import Function_1 as f
    df1=pd.read_csv(r'c:\Users\ext-mboufath\Desktop\TRANSPORT BI\Shipment_20230725.csv')
    text= df1.tail(2)

    msg=f.print_path()
    print(msg)
    print(text)
    
    
if __name__=="__main__":
    main()