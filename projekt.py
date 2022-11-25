import tkinter as tk
from tkinter import ttk

class TkinterApp(tk.Tk):
    '''
    This class is a framework that allows the other classes to inherit propties such as the tk.Frame and the grid layout. This can be seen as the base
    on which the application is built upon.
    '''
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Choice_page, Binary_page, Decimal_page, Hexadecimal_page):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Choice_page)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Choice_page(tk.Frame):
    """
    The class of the start menu for selecting an option to convert to. 
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of choice page
        choice_label = ttk.Label(self, text= "Choose an option") 

        choice_label.grid(row = 0, column = 4, padx = 10, pady = 10)

        #Binary button options
        binary_button = ttk.Button(self, text = "Binary coversion", command = lambda : controller.show_frame(Binary_page))
        binary_button.grid(row = 1, column=1, padx=10, pady=10)

        #decimal button options 
        decimal_button = ttk.Button(self, text = "Decimal coversion", command = lambda : controller.show_frame(Decimal_page)) 
        decimal_button.grid(row = 2, column=1, padx=10, pady=10) 
        
        #Hexidecimal button options
        hexi_button = ttk.Button(self, text = "Hexidecimal coversion", command = lambda : controller.show_frame(Hexadecimal_page))
        hexi_button.grid(row = 3, column=1, padx=10, pady=10)

class Conversion_page(tk.Frame):
    """
    Class for the conversion of different types of input. Takes care of the logic for convsersion.
    """
    def __init__(self):
        self.c_list = []
            
    def decimal_convo(self, me, input_text):
        '''
        A function for the decimal conversion to hexadecimal / binary 
        ''' 

        #Algoritmen för decimal till hexadecimal
        if me == "hexa":
            if "0b" in input_text or "0x" in input_text or len(input_text) == 0 or input_text == "Please enter a decimal number":
                return "Please enter a decimal number"
            else:
                return hex(int(input_text))
    
        #Algoritmen för decimal till binär
        if me == "binary":
            if "0b" in input_text or "0x" in input_text or len(input_text) == 0 or input_text == "Please enter a decimal number":
                return "Please enter a decimal number"
            else:
                return bin(int(input_text))


    def hexa_convo(self, me, input_text):
        '''
        A function for the hexadecimal conversion to binary / decimal
        '''
        #Algoritmen för hexadecimal till decimal

        if me == "decimal":
            if "0x" not in input_text or input_text == "0x":
                return "Please enter a hexadecimal number"
            else:
                return str(int(input_text, 16))
        #Algoritmen för hexadecimal till binär
        if me == "binary":
            if "0x" not in input_text or input_text == "0x":
                return "Please enter a hexadecimal number"
            else:
                return bin(int(input_text, 16))

    def binary_convo(self, me, input_text):

        '''
        A function for the binary conversion to hexa / decimal 
        '''
        #Algoritmen för binär till decimal
        if me == "decimal":
            if "0b" not in input_text or input_text == "0b":
                return "Please enter a binary number"
            else:
                return str(int(input_text, 2))
        #Algoritmen för binär till hexadecimal
        if me == "hexa":
            if "0b" not in input_text or input_text == "0b":
                return "Please enter a binary number"
            else:
                return hex(int(input_text, 2))



class Binary_page(tk.Frame):
    """
    Class that handels binary numbers. 
    """
    def __init__(self, parent, controller):

        self.expression = "0b"
        self.input_text = tk.StringVar()

        tk.Frame.__init__(self, parent)

        # label of binary page
        binary_label = ttk.Label(self, text= "Enter a binary number")

        # Sets the label in the postion row= 0, column = 4
        binary_label.grid(row = 0, column = 4, padx = 10, pady = 10)
       
        # Sets the input field with the disabled parameter so the user can't enter with keyboard
        input_field = ttk.Entry(self, textvariable= self.input_text, justify='right', state='disabled')
        input_field.grid(row=1, column= 4)

        #BUTTONS to press
        zero = ttk.Button(self, text = "0",cursor = "hand2", command = lambda: self.btn_click(0)).grid(row = 2, column = 0, padx = 1, pady = 1)
        one = ttk.Button(self, text = "1",cursor = "hand2", command = lambda: self.btn_click(1)).grid(row = 2, column = 1, padx = 1, pady = 1)
        b_decimal = ttk.Button(self, text = "Decimal Conversion",cursor = "hand2", command = lambda: self.BinaryDecimal(self.input_text.get())).grid(row = 0, column = 1, padx = 1, pady = 1)
        b_hexadecimal = ttk.Button(self, text = "Hexadecimal Conversion",cursor = "hand2", command = lambda: self.BinaryHex(self.input_text.get())).grid(row = 0, column = 2, padx = 1, pady = 1)
        clear = ttk.Button(self, text = "Clear",cursor = "hand2", command = lambda: self.clear_input()).grid(row = 3, column = 0, padx = 1, pady = 1)
        
        #Home page
        back_button = ttk.Button(self, text = "Start page", command = lambda : [self.clear_input(), controller.show_frame(Choice_page)])
        back_button.grid(row = 0, column=0, padx=1, pady=1)



    def clear_input(self):
        '''
        The function for clearing the input. 
        '''
        self.expression = "0b"
        self.input_text.set(self.expression)

    def btn_click(self, item):
        """ 
        Allows for the input of button. 
        """
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def BinaryDecimal(self, input_text):
        """ 
        The function that calls from binary conversion to decimal conversion. 
        """
        self.expression = "0b"
        c_page = Conversion_page()
        result = c_page.binary_convo("decimal", input_text)
        self.input_text.set("".join(map(str, result)))

    def BinaryHex(self, input_text):
        """ 
        The function that calls from binary conversion to hexadecimal conversion. 
        """
        self.expression = "0b"
        c_page = Conversion_page()
        result = c_page.binary_convo("hexa", input_text)
        self.input_text.set("".join(map(str, result)))
    
 
class Decimal_page(tk.Frame):
    """
    Class that handles decimal numbers. 
    """
    def __init__(self, parent, controller):

        self.expression = ""
        self.input_text = tk.StringVar()

        tk.Frame.__init__(self, parent)


        # label of decimal page
        decimal_label = ttk.Label(self, text = "Enter a decimal number")

        # Sets the label in the postion row= 0, column = 4
        decimal_label.grid(row = 0, column = 4, padx = 10, pady = 10)
       
        # Sets the input field with the disabled parameter so the user can't enter with keyboard
        input_field = ttk.Entry(self, textvariable= self.input_text, justify='right', state='disabled')
        input_field.grid(row=1, column= 4)


        #BUTTONS to press
        zero = ttk.Button(self, text = "0",cursor = "hand2", command = lambda: self.btn_click(0)).grid(row = 2, column = 0, padx = 1, pady = 1)
        one = ttk.Button(self, text = "1",cursor = "hand2", command = lambda: self.btn_click(1)).grid(row = 2, column = 1, padx = 1, pady = 1)
        two = ttk.Button(self, text = "2",cursor = "hand2", command = lambda: self.btn_click(2)).grid(row = 2, column = 2, padx = 1, pady = 1)

        three = ttk.Button(self, text = "3",cursor = "hand2", command = lambda: self.btn_click(3)).grid(row = 3, column = 0, padx = 1, pady = 1)
        four = ttk.Button(self, text = "4",cursor = "hand2", command = lambda: self.btn_click(4)).grid(row = 3, column = 1, padx = 1, pady = 1)
        five = ttk.Button(self, text = "5",cursor = "hand2", command = lambda: self.btn_click(5)).grid(row = 3, column = 2, padx = 1, pady = 1)

        six = ttk.Button(self, text = "6",cursor = "hand2", command = lambda: self.btn_click(6)).grid(row = 4, column = 0, padx = 1, pady = 1)
        seven = ttk.Button(self, text = "7",cursor = "hand2", command = lambda: self.btn_click(7)).grid(row = 4, column = 1, padx = 1, pady = 1)
        eight = ttk.Button(self, text = "8",cursor = "hand2", command = lambda: self.btn_click(8)).grid(row = 4, column = 2, padx = 1, pady = 1)
        
        nine = ttk.Button(self, text = "9",cursor = "hand2", command = lambda: self.btn_click(9)).grid(row = 5, column = 1, padx = 1, pady = 1)
        clear = ttk.Button(self, text = "Clear",cursor = "hand2", command = lambda: self.clear_input()).grid(row = 5, column = 0, padx = 1, pady = 1)

        d_binary = ttk.Button(self, text = "Binary Conversion",cursor = "hand2", command = lambda: self.DecimalBinary(self.input_text.get())).grid(row = 0, column = 1, padx = 1, pady = 1)
        d_hexadecimal = ttk.Button(self, text = "Hexadecimal Conversion",cursor = "hand2", command = lambda: self.DecimalHexa(self.input_text.get())).grid(row = 0, column = 2, padx = 1, pady = 1)

        #Home page
        back_button = ttk.Button(self, text = "Start page", command = lambda : [self.clear_input(), controller.show_frame(Choice_page)])
        back_button.grid(row = 0, column=0, padx=1, pady=1)


    def clear_input(self):
        """ 
        Clears the input. 
        """
        self.expression = ""
        self.input_text.set(self.expression)

    def btn_click(self, item):
        """ 
        Allows for the input of button. 
        """
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def DecimalBinary(self, input_text):
        """ 
        The function that calls for the decimal to binary conversion. 
        """
        self.expression = ""
        c_page = Conversion_page()
        result = c_page.decimal_convo("binary", input_text)
        if result == "Choose a new number":
            self.input_text.set(result)
            return
        self.input_text.set("".join(map(str, result)))

    def DecimalHexa(self, input_text):
        """ 
        The function that calls for the decimal to hexadecimal conversion. 
        """
        self.expression = ""
        c_page = Conversion_page()
        result = c_page.decimal_convo("hexa", input_text)
        if result == "Choose a new number":
            self.input_text.set(result)
            return
        self.input_text.set("".join(map(str, result)))


class Hexadecimal_page(tk.Frame):
    """ 
    Class that handels hexadecimal numbers. 
    """
    def __init__(self, parent, controller):

        self.expression = "0x"
        self.input_text = tk.StringVar()

        tk.Frame.__init__(self, parent)
        

        # label of hexadecimal page
        hexadecimal_label = ttk.Label(self, text = "Enter a hexadecimal number")

        # Sets the label in the postion row= 0, column = 4
        hexadecimal_label.grid(row = 0, column = 4, padx = 10, pady = 10)
       
        # Sets the input field with the disabled parameter so the user can't enter with keyboard
        input_field = ttk.Entry(self, textvariable= self.input_text, justify='right', state='disabled')
        input_field.grid(row=1, column= 4)

        self.zero = ttk.Button(self, text = "0",cursor = "hand2", command = lambda: self.btn_click(0))
        self.zero.grid(row = 2, column = 0, padx = 1, pady = 1)
        self.one = ttk.Button(self, text = "1",cursor = "hand2", command = lambda: self.btn_click(1))
        self.one.grid(row = 2, column = 1, padx = 1, pady = 1)
        self.two = ttk.Button(self, text = "2",cursor = "hand2", command = lambda: self.btn_click(2))
        self.two.grid(row = 2, column = 2, padx = 1, pady = 1)
        self.three = ttk.Button(self, text = "3",cursor = "hand2", command = lambda: self.btn_click(3))
        self.three.grid(row = 3, column = 0, padx = 1, pady = 1)
        self.four = ttk.Button(self, text = "4",cursor = "hand2", command = lambda: self.btn_click(4))
        self.four.grid(row = 3, column = 1, padx = 1, pady = 1)
        self.five = ttk.Button(self, text = "5",cursor = "hand2", command = lambda: self.btn_click(5))
        self.five.grid(row = 3, column = 2, padx = 1, pady = 1)
        self.six = ttk.Button(self, text = "6",cursor = "hand2", command = lambda: self.btn_click(6))
        self.six.grid(row = 4, column = 0, padx = 1, pady = 1)
        self.seven = ttk.Button(self, text = "7",cursor = "hand2", command = lambda: self.btn_click(7))
        self.seven.grid(row = 4, column = 1, padx = 1, pady = 1)
        self.eight = ttk.Button(self, text = "8",cursor = "hand2", command = lambda: self.btn_click(8))
        self.eight.grid(row = 4, column = 2, padx = 1, pady = 1)
        self.nine = ttk.Button(self, text = "9",cursor = "hand2", command = lambda: self.btn_click(9))
        self.nine.grid(row = 5, column = 1, padx = 1, pady = 1)
        self.h_decimal = ttk.Button(self, text = "Decimal Conversion",cursor = "hand2", command = lambda: self.HexDecimal(self.input_text.get()))
        self.h_decimal.grid(row = 0, column = 1, padx = 1, pady = 1)
        self.h_binary = ttk.Button(self, text = "Binary Conversion",cursor = "hand2", command = lambda: self.HexBinary(self.input_text.get()))
        self.h_binary.grid(row = 0, column = 2, padx = 1, pady = 1)
        clear = ttk.Button(self, text = "Clear",cursor = "hand2", command = lambda: self.clear_input()).grid(row = 5, column = 0, padx = 1, pady = 1)


        self.change_state = ttk.Button(self, text = "Letters",cursor = "hand2", command = lambda: self.change_buttons_lett(controller))
        self.change_state.grid(row = 5, column = 2, padx = 1, pady = 1)
        
        #Home page
        back_button = ttk.Button(self, text = "Start page", command = lambda : [self.clear_input(), controller.show_frame(Choice_page)])
        back_button.grid(row = 0, column=0, padx=1, pady=1)

    def change_buttons_num(self,controller):
        """    
        function for the buttons with numbers. 
        """
        self.zero.configure(text = "0",cursor = "hand2", command = lambda: self.btn_click(0))
        self.zero.grid(row = 2, column = 0, padx = 1, pady = 1)
        self.one.configure(text = "1",cursor = "hand2", command = lambda: self.btn_click(1))
        self.one.grid(row = 2, column = 1, padx = 1, pady = 1)
        self.two.configure(text = "2",cursor = "hand2", command = lambda: self.btn_click(2))
        self.two.grid(row = 2, column = 2, padx = 1, pady = 1)
        self.three.configure(text = "3",cursor = "hand2", command = lambda: self.btn_click(3))
        self.three.grid(row = 3, column = 0, padx = 1, pady = 1)
        self.four.configure( text = "4",cursor = "hand2", command = lambda: self.btn_click(4))
        self.four.grid(row = 3, column = 1, padx = 1, pady = 1)
        self.five.configure(text = "5",cursor = "hand2", command = lambda: self.btn_click(5))
        self.five.grid(row = 3, column = 2, padx = 1, pady = 1)
        self.six.configure(text = "6",cursor = "hand2", command = lambda: self.btn_click(6))
        self.six.grid(row = 4, column = 0, padx = 1, pady = 1)
        self.seven.configure(text = "7",cursor = "hand2", command = lambda: self.btn_click(7))
        self.seven.grid(row = 4, column = 1, padx = 1, pady = 1)
        self.eight.configure(text = "8",cursor = "hand2", command = lambda: self.btn_click(8))
        self.eight.grid(row = 4, column = 2, padx = 1, pady = 1)
        self.nine.configure(text = "9",cursor = "hand2", command = lambda: self.btn_click(9))
        self.nine.grid(row = 5, column = 1, padx = 1, pady = 1)
        self.change_state.configure(text = "Letters",cursor = "hand2", command = lambda: self.change_buttons_lett(controller))
        self.change_state.grid(row = 5, column = 2, padx = 1, pady = 1)
    
    def change_buttons_lett(self,controller):
        """ 
        Function for the buttons with letters. 
        """
        self.zero.configure(text = "A",cursor = "hand2", command = lambda: self.btn_click("A"))
        self.zero.grid(row = 2, column = 0, padx = 1, pady = 1)
        self.one.configure(text = "B",cursor = "hand2", command = lambda: self.btn_click("B"))
        self.one.grid(row = 2, column = 1, padx = 1, pady = 1)
        self.two.configure(text = "C",cursor = "hand2", command = lambda: self.btn_click("C"))
        self.two.grid(row = 2, column = 2, padx = 1, pady = 1)
        self.three.configure(text = "D",cursor = "hand2", command = lambda: self.btn_click("D"))
        self.three.grid(row = 3, column = 0, padx = 1, pady = 1)
        self.four.configure(text = "E",cursor = "hand2", command = lambda: self.btn_click("E"))
        self.four.grid(row = 3, column = 1, padx = 1, pady = 1)
        self.five.configure(text = "F",cursor = "hand2", command = lambda: self.btn_click("F"))
        self.five.grid(row = 3, column = 2, padx = 1, pady = 1)
        self.six.grid_forget()
        self.seven.grid_forget()
        self.eight.grid_forget()
        self.nine.grid_forget()
        self.change_state = ttk.Button(self, text = "Numbers",cursor = "hand2", command = lambda: self.change_buttons_num(controller))
        self.change_state.grid(row = 5, column = 2, padx = 1, pady = 1)


    def clear_input(self):
        """ 
        Clears the input. 
        """
        self.expression = "0x"
        self.input_text.set(self.expression)

    def HexDecimal(self, input_text):
        """ 
        The function that calls for the hexadecimal to decimal conversion.
        """
        self.expression = "0x"
        c_page = Conversion_page()
        result = c_page.hexa_convo("decimal", input_text)
        self.input_text.set("".join(map(str, result)))

    def HexBinary(self, input_text):
        """ 
        The function that calls for the hexadecimal to binary conversion. 
        """
        self.expression = "0x"
        c_page = Conversion_page()
        result = c_page.hexa_convo("binary", input_text)
        self.input_text.set("".join(map(str, result)))

    def btn_click(self, item):
        """ 
        Function for buttons. 
        """
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

app = TkinterApp()
app.mainloop() 