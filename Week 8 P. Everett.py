# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# P Everett, 3-7-2022,Modified code to complete assignment 8
# #P Everett 3-11-2022 Finish more code
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Peverett, 3-7-2022,Modified code to complete assignment 8
    """
    # --Fields--
    # --Constructor--
    def __init__(self,Product: str,Price:float):
        # --Attributes--
        try:
            self.__Product = str(Product)
            self.__Price = float(Price)
        except Exception as e:
            raise Exception("Error while setting values")


    # --Properties--
    #Getter for Product
    @property
    def Product(self):
        return str(self.__Product).title()
    #Setter for Product
    @Product.setter
    def Product(self,value: str):
        if str(value).inumeric() == False:
            self.__Product = value
        else:
            raise Exception("Products cannot be numbers!")
    #Getter for Price
    @property
    def Price(self):
        return float(self.__Price)
    #Setter for Price
    @Price.setter
    def Price(self,value: float):
        if str(value).isnumeric():
            self.__Price = float(value)
        else:
            raise Exception("Price must be a number!")

    # --Methods--
    def to_string(self):
        """ Converting product data to string """
        return self.__str__()
    def __str__(self):
        """ Changes prodcut data to string"""
        return self.Product + "," +str(self.Price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    #static method for these methods
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects): -> (bool status)

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Patricia  Everett, 3-11-2022,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(fileName: str, listProductObj: list):
        """
        Writes data to a file from the list of products
        :param fileName: string with name of the file
        :param listProductObj: list of product objects to save
        :return: (bool) with status of success or failure to save data
        """
        #Sets status to failure otherwise would always be true and not get an error
        successStatus = False
        #tries opening the file and gives errors if issue occurs
        try:
            file = open(fileName, "w")
            for product in listProductObj:
                file.write(product.__str__() + "\n")
            file.close()
            successStatus = True
        #prints out a bunch of errors to help trouble shoot issue
        except Exception as e:
            print("There was an error!")
            print(e,e.__doc__, type(e),sep= '\n')
            return successStatus

    @staticmethod
    def read_data_from_file(fileName: str):
        """
        Reads data from file into a list object of products and prices
        :param fileName: (string) with name of file
        :return: (list) object that returns data
        """
        listProduct = []
        try:
            File = open(fileName, "r")
            for line in File:
                data = line.split(",")
                row = Product(data[0],data[1])
                listProduct.append(row)
            File.close()
        except Exception as e:
            print("There was an error!")
            print(e,e.__doc__, type(e),sep= '\n')
        return listProduct

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Requests User Inputs to either read data, add data, or save data:

        properties:
            product_name: (string) with the products's  name
            product_price: (float) with the products's standard price
        methods:
            printMenu()
            InputChoice()
            printCurrentList()
            InputProdAndPrice()

        changelog: (When,Who,What)
            RRoot,1.1.2030,Created Class
            P Everett, 3-11-2022,Modified code to complete assignment 8
        """


    @staticmethod
    def printMenu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Current List
        2) Add a new item
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputChoice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def printCurrentList(listProduct: list):
        """
        Print the current items in product list
        :param listProduct: (list) you want to display
        """
        print("------ Current Product List ------")
        for row in listProduct:
            print(row.Product + " (" +str(row.Price) + ")" )
        print("----------------------------------")
        print()

    # TODO: Add code to get product data from user
    @staticmethod
    def inputProdAndPrice():
        """  Gets product and price values to be added to the list

        :return: (Product) object with input data
        """
        try:
            strProduct = str(input("Enter Product: ").strip())
            strPrice = float(input("Enter Price: ").strip())
            print()
            prod = Product(Product = strProduct, Price = strPrice)
        except Exception as e:
            print(e)
        return prod

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while True:
        # Show user a menu of options
        IO.printMenu()
        # Get user's menu option choice
        strChoice = IO.InputChoice()
        if strChoice.strip() == '1':
            # Show user current data in the list of product objects
            IO.printCurrentList(lstOfProductObjects)
            continue
        # Let user add data to the list of product objects
        elif strChoice.strip() == '2':
            lstOfProductObjects.append(IO.inputProdAndPrice())
            continue
        # let user save current data to file and exit program
        elif strChoice.strip() == '3':
            FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
            continue
        elif strChoice.strip() == '4':
            break
except Exception as e:
    print("There was an error, check file permissions.")
    print(e, e.__doc__, type(e), sep='\n')

# Main Body of Script  ---------------------------------------------------- #

