import tkinter as tk 
from tkinter import PhotoImage
from tkinter import ttk
import re

class calculadora:
    def __init__(self):
        self.ventana1=tk.Tk()
        icono=PhotoImage(file='C:/Users/Desktop/calculadora.png')
        self.ventana1.iconphoto(False,icono)
        self.ventana1.title("Calculadora")
        self.labelframe1=ttk.LabelFrame(self.ventana1)
        self.labelframe1.grid(column=0,row=0,padx=10,pady=10) 
        self.entrys()
        self.labelframe2=ttk.LabelFrame(self.ventana1)
        self.labelframe2.grid(column=0,row=1,padx=2,pady=3)
        self.digitos()
        self.ventana1.mainloop()

    def entrys(self): 
        self.datoc=tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe1,textvariable=self.datoc,justify='righ',font=("Arial",16))
        self.entry1.grid(column=0,row=0,ipadx=40,ipady=8)  

    def digitos(self):  #Iconos de los botones
        self.iconos = [
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/1.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/2.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/3.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/cruz.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/dividir.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/4.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/5.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/6.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/mas.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/menos.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/7.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/8.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/9.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/raiz.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/elevado.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/0.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/parentesisIzq.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/parentesisDer.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/reinicio.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/bala.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/borra.png'),
            tk.PhotoImage(file='C:/Users/Desktop/Practicas de Phyton/Proyectos_GitHub/Iconos/igual.png')
        ]
        #Botones de la calculadora
        self.boton1=ttk.Button(self.labelframe2,image=self.iconos[0],command=lambda: self.datoc.set(self.datoc.get() + "1"))  
        self.boton1.grid(column=0,row=0,pady=2,padx=2)
        self.boton2=ttk.Button(self.labelframe2,image=self.iconos[1],command=lambda: self.datoc.set(self.datoc.get() + "2"))   
        self.boton2.grid(column=1,row=0,pady=2,padx=2) 
        self.boton3=ttk.Button(self.labelframe2,image=self.iconos[2],command=lambda: self.datoc.set(self.datoc.get() + "3"))  
        self.boton3.grid(column=2,row=0,pady=2,padx=2)
        self.boton4=ttk.Button(self.labelframe2,image=self.iconos[3],command=lambda: self.repetidos("x")) 
        self.boton4.grid(column=3,row=0,pady=4,padx=4)
        self.boton5=ttk.Button(self.labelframe2,image=self.iconos[4],command=lambda: self.repetidos("÷")) 
        self.boton5.grid(column=4,row=0,pady=4,padx=4)
        self.boton6=ttk.Button(self.labelframe2,image=self.iconos[5],command=lambda: self.datoc.set(self.datoc.get() + "4"))  
        self.boton6.grid(column=0,row=1,pady=2,padx=2)
        self.boton7=ttk.Button(self.labelframe2,image=self.iconos[6],command=lambda: self.datoc.set(self.datoc.get() + "5"))   
        self.boton7.grid(column=1,row=1,pady=2,padx=2) 
        self.boton8=ttk.Button(self.labelframe2,image=self.iconos[7],command=lambda: self.datoc.set(self.datoc.get() + "6"))  
        self.boton8.grid(column=2,row=1,pady=2,padx=2)
        self.boton9=ttk.Button(self.labelframe2,image=self.iconos[8],command=lambda: self.repetidos("+")) 
        self.boton9.grid(column=3,row=1,pady=4,padx=4)
        self.boton10=ttk.Button(self.labelframe2,image=self.iconos[9],command=lambda: self.repetidos("-")) 
        self.boton10.grid(column=4,row=1,pady=4,padx=4)
        self.boton11=ttk.Button(self.labelframe2,image=self.iconos[10],command=lambda: self.datoc.set(self.datoc.get() + "7"))  
        self.boton11.grid(column=0,row=2,pady=2,padx=2)
        self.boton12=ttk.Button(self.labelframe2,image=self.iconos[11],command=lambda: self.datoc.set(self.datoc.get() + "8"))   
        self.boton12.grid(column=1,row=2,pady=2,padx=2) 
        self.boton13=ttk.Button(self.labelframe2,image=self.iconos[12],command=lambda: self.datoc.set(self.datoc.get() + "9"))  
        self.boton13.grid(column=2,row=2,pady=2,padx=2)
        self.boton14=ttk.Button(self.labelframe2,image=self.iconos[13],command=lambda: self.repetidos("√")) 
        self.boton14.grid(column=3,row=2,pady=4,padx=4)
        self.boton15=ttk.Button(self.labelframe2,image=self.iconos[14],command=lambda: self.repetidos("^")) 
        self.boton15.grid(column=4,row=2,pady=4,padx=4)
        self.boton16=ttk.Button(self.labelframe2,image=self.iconos[15],command=lambda: self.datoc.set(self.datoc.get() + "0"))  
        self.boton16.grid(column=0,row=3,pady=2,padx=2)
        self.boton17=ttk.Button(self.labelframe2,image=self.iconos[16],command=lambda: self.repetidos("(")) 
        self.boton17.grid(column=1,row=3,pady=2,padx=2)
        self.boton18=ttk.Button(self.labelframe2,image=self.iconos[17],command=lambda: self.repetidos(")")) 
        self.boton18.grid(column=2,row=3,pady=2,padx=2)
        self.boton19=ttk.Button(self.labelframe2,image=self.iconos[18],command=lambda: self.datoc.set("")) 
        self.boton19.grid(column=3,row=3,pady=4,padx=4)
        self.boton20=ttk.Button(self.labelframe2,image=self.iconos[19],command=lambda: self.repetidos(".")) 
        self.boton20.grid(column=4,row=3,pady=4,padx=4)
        self.boton21=ttk.Button(self.labelframe2,image=self.iconos[20],command=self.eliminar) 
        self.boton21.grid(column=0,row=4,columnspan=2,sticky="we")
        self.boton22=ttk.Button(self.labelframe2,image=self.iconos[21],command=self.equal) 
        self.boton22.grid(column=2,row=4,columnspan=3,sticky="we")

    def repetidos(self,dato):
        if re.match("^$",self.datoc.get()):             #si la cadena esta vacia asigna algunas signos al princio          # ^$ coincide con cadenas vacia
            if dato == "+" or dato == "-" or dato == "√" or dato == "(":
                self.datoc.set(self.datoc.get() + dato)
        elif self.datoc.get().endswith(dato):           #si la cadena repite cierto digito, este no volvera a colocar cierto digito, excepto los numeros
            None
        else:                                           #si la cadena no esta vacia ni los digitos se repiten, colocara el nuevo digito asignado
            self.datoc.set(self.datoc.get() + dato)

    def eliminar(self):                     #Elimina el ultimo digito ingresado al string
        nue = self.datoc.get()
        nu = len(nue)
        self.datoc.set(nue[:nu-1]) 

    def equal(self):                        #Enviamos y recibimos el resultado de nuestra operación
        dato = self.datoc.get()

        if re.search(r"\(((\d+(?:\.\d+)?)?[-+x÷√^]+\d+(?:\.\d+)?)+\)",dato):        #Busca parentesis
            dato = self.parentesis(dato)

        while True:
            paren=re.search(r"((\d+(?:\.\d+)?)?(\([-+]?\d+(?:\.\d+)?\))+(\d+(?:\.\d+)?)?)+",dato)       #Busca datos como (4)(54)3,  12(-3)6(2)2,  (2)  si no encuentra rompe el siclo
            if not paren:  
                break
            dato = self.eli_paren(dato)  

        if re.search(r"[-+]?\d+(?:\.\d+)?|^$",dato) != True:        #Busca operaciones sin Parentesis como 3x4+45-4 
            dato = self.operaciones(dato)           
     
        if re.search(r"\d+(\.(0+))$",dato):                     #Busca Decimales que contengan .00000, si todos son 0 se cambia a Entero, si tiene algun valor como .00004 se deja como decimal
            dato = str(int(float(dato)))
        else:
            try:
                d = float(dato)
                dato=str(round(d,7))  #redondeamos y combertimos a string
            except:
                self.datoc.set("Syntax Error")

        if re.search(r"^([-+]?\d+(?:\.\d+)?)$|^$",dato):        #Evalua si el resultado final es algun numero (Entero o Natural)
            self.datoc.set(dato)
        else:                                                    #si el resoltado final no es (Entero o Natural) imprimios, syntax error
            self.datoc.set("Syntax Error")

    def parentesis(self,par):
        while True:
            # Busca el par de paréntesis más interno que no contenga otros paréntesis
            nuevo = re.search(r"\(([^()]+)\)", par)         #esta expresión busca datos sin los parentesis
            if not nuevo:
                break

            n1 = nuevo.start()
            n2 = nuevo.end()
            nue1 = par[:n1]             # parte izquierda antes del paréntesis  <-(datos)
            nue2 = par[n2:]             # parte derecha después del paréntesis  (datos)->
            sep = nuevo.group(1)        # contenido del paréntesis (sin los paréntesis)  (<-   datos   ->)

            ps = self.operaciones(sep)  
            if nue1 != None or nue2 != None:                    #si alrededor del parentesis habian datos, el resultado del parentesis lo guardamos enotro parentesis 
                par = nue1  + "(" + ps + ")" + nue2                             #para que interactue con los demas datos alrededor
            else:
                par = nue1  + ps  + nue2

            return par
    
    def operaciones(self,dato):                     #Donde el programa ara las opereaciones Matematicas
        dato = re.sub(r"\-\-","+",dato)                #Si el dato que ingresa a operaciones tiene dos -- se cambia por +
        dato = re.sub(r"\-\+","-",dato)                #Si el dato que ingresa a operaciones tiene -+ se cambia por -
        dato = re.sub(r"\+\-","-",dato)                #Si el dato que ingresa a operaciones tiene +- se cambia por -

        if re.search(r"(√\d+(?:\.\d+)?|\d+(?:\.\d+)?\^([-+]?\d+(?:\.\d+)?))",dato):   #Busca raizes y elevados  
            dato_regex=r"(√\d+(?:\.\d+)?|\d+(?:\.\d+)?\^([-+]?\d+(?:\.\d+)?))"
            rege=r"[\^√]"     
            while re.search(dato_regex,dato):
                n1,n2,l1,l2,sim = self.separador(dato,dato_regex,rege)

                if sim == "√":
                    rai = str(round(l2**0.5,7))
                    dato = n1 + "(" + rai + ")" +n2
                    dato = self.eli_paren(dato)
                elif sim == "^":
                    ele = str(round(l1**l2,7))
                    dato = n1 + ele + n2
            
            
        if re.search(r"\d+(?:\.\d+)?[x÷][\-+]?\d+(?:\.\d+)?",dato):                 #Busca multiplicaciones y diviviones 
            dato_regex=r"\d+(?:\.\d+)?[x÷][\-+]?\d+(?:\.\d+)?"
            rege=r"[x÷]"
            while re.search(dato_regex,dato):
                n1,n2,l1,l2,sim = self.separador(dato,dato_regex,rege)
                
                if sim == "x":
                    mul = str(round(l1*l2,7))
                    dato = n1 + mul + n2   
                elif sim == "÷":
                    div = str(l1/l2)
                    dato = n1 + div + n2

                dato = re.sub(r"\-\-","+",dato)
                dato = re.sub(r"\-\+","-",dato)
                dato = re.sub(r"\+\-","-",dato)

        if re.search(r"[-+]?\d+(?:\.\d+)?[-+]\d+(?:\.\d+)?",dato):                  #Busca sumas y restas                                                           
            dato_regex=r"[-+]?\d+(?:\.\d+)?[-+]\d+(?:\.\d+)?"            
            while re.search(dato_regex,dato):
                dato = separador_de_digitos(dato,dato_regex)

        return dato  
   
    def separador(self,dato,regex,rege2):
        
        nuevo=re.search(f"{regex}",dato)
        n1=nuevo.start()
        n2=nuevo.end()
        nue1=dato[:n1]      #extrae los valres de la derecha
        nue2=dato[n2:]      #extrae los valores de la izquierda
        sep=dato[n1:n2]     #extrae el valor que buscamos

        nuev=re.search(f"{rege2}",sep)
        l1=nuev.start()
        l2=nuev.end() 
        ll1 = ""
        ll2 = ""
        if sep[:l1] != "":
            ll1 = float(sep[:l1])           #extrae a la izquierda del simbolo
        if sep[l2:] != "":
            ll2 = float(sep[l2:])           #extraemos a la derecha del simbolo
        sim = sep[l1:l2]

        return nue1, nue2, ll1, ll2, sim

    def eli_paren(self,dato:str):           #Extrae los parentesis y nuemeros que tiene a la par como (32)(3), 4(9), (11)1(l12)2(3), -1(2)1 y los multiplica
        mul = 1
      
        paren = re.search(r"([-+]?\d+(?:\.\d+)?)?(\([-+]?\d+(?:\.\d+)?\))((\d+(?:\.\d+)?)?|(\([-+]?\d+(?:\.\d+)?\)))+",dato)
        n1 = paren.start()
        n2 = paren.end()
        par = dato[n1:n2]
        matches = re.findall(r"[-+]?\d+(?:\.\d+)?", par)    #Extrae todas las coicidencias y las guarda en una lista
        for num in matches:
            par2 = float(num)
            mul *= par2        
        res = str(mul)
        dato = dato.replace(dato[n1:n2],res)

        return dato   
    
def separador_de_digitos(dato:str,regex):       #Hace leyes de signos basicas como (-)(-)=- , (-)(+)=depende del numero mayor, etc
        nuevo=re.search(f"{regex}",dato)
        n1=nuevo.start()
        n2=nuevo.end()
        nue1=dato[:n1]      #extrae los valres de la derecha
        nue2=dato[n2:]      #extrae los valores de la izquierda
        sep=dato[n1:n2]     #extrae el valor que buscamos
        res=0
        while re.search(r"[-+]?\d+(?:\.\d+)?",sep):
            nn1 = re.search(r"[-+]?\d+(?:\.\d+)?",sep)
            ll1 = nn1.start()   
            ll2 = nn1.end()
            nn2 = float(sep[ll1:ll2])       #Extrae la primera coicidencia que encuentre 
            res += nn2                      # 0+(3)=3   3+(-4)=-1   -1+(+2)=1   
            sep = sep[:ll1] + sep[ll2:]   
        r=str(res)
        dato = nue1 + r + nue2
        return dato

calcu=calculadora()


              
