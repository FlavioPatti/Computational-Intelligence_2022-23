"""
PER LA VISUALIZZAZIONE DEL GIOCO 
            *
           ***
          *****
         *******
        *********
 

-Task3.1: An agent using fixed rules based on nim-sum (i.e., an expert system)
ES: if (num_object > 20 then something)

-Task3.2: An agent using evolved rules
ES: if (a < num_object < b) => ottimizzare a e b come se fossero parametri di un genoma

-Task3.3: An agent using minmax

-Task3.4: An agent using reinforcement learning

"""
    
class Nim:
    def __init__(self, num_rows: int, k: int = None):
        self._rows = [i*2 + 1 for i in range(num_rows)]
        self._k = k
        self._num_rows = num_rows
        self._tot_objects = k*k
        #l'avversario gioca in modo standard: toglie sempre 2 oggetti dall'ultima riga tranne quando ci sono meno di due oggetti 
        # in quella riga (in quel caso ne toglie solo 1)
        self._row_opponent = self._num_rows -1
        self._num_objects_opponent = 2
    
        
    def nimming(self, row: int, num_objects: int): #toglie num_object da una determinata row
        if num_objects <= self._k and self._k is not None: #check per correttezza della mossa
            #se il numero di oggetti da togliere è maggiore di quelli attualmente presenti in quella riga tolgo solo quelli
            if self._rows[row] < num_objects:
                num_objects = self._rows[row]
            
            print(f"tolgo {num_objects} oggetti dalla riga {row}")
            self._rows[row] -= num_objects
            self._tot_objects -= num_objects 
            
            if self._rows[row] <= 0:
                self._num_rows -= 1
                self._row_opponent = self._num_rows -1
            
            if sum(self._rows) == 0:
                print("Gioco finito")
        else:
            print("Non hai inserito una mossa valida")
            
    ###TASK 3.1 FIXED RULES####
    def my_turn_fixed_rules(self):
        chosen_row = 0
        object_to_remove = 0
        if (self._tot_objects < 25 and self._tot_objects >= 20):
            chosen_row = self._num_rows - 1
            object_to_remove = 3
        if (self._tot_objects < 20 and self._tot_objects >= 15):
            chosen_row = self._num_rows - 1
            object_to_remove = 2
        if (self._tot_objects < 15 and self._tot_objects >= 10):
            chosen_row = self._num_rows - 1
            object_to_remove = 1
        if (self._tot_objects < 10 and self._tot_objects >= 5):
            chosen_row = self._num_rows - 1
            object_to_remove = 1
        if (self._tot_objects < 5 and self._tot_objects >= 1):
            chosen_row = self._num_rows - 1
            object_to_remove = 1

        return chosen_row, object_to_remove    


if __name__ == '__main__':

    num_rows = 5
    k = 5
    nim = Nim(num_rows, k)
    print(f"comincia il gioco {nim._rows}")

    for i in range(16): #pari => opponent turn, dispari => my turn
        if i % 2 == 0:
            print(f"turno {i} gioca l'avversario e rimangono {nim._tot_objects} oggetti")
            nim.nimming(nim._row_opponent, nim._num_objects_opponent)
        else:
            print(f"turno {i} gioco io e rimangono {nim._tot_objects} oggetti")
            my_row, my_num_objects = nim.my_turn_fixed_rules()
            nim.nimming(my_row, my_num_objects)
        
        print(f"condizione attuale {nim._rows}")
        
    if i % 2 != 0:
        print(f"Hai tolto l'ultimo oggetto! Vince la partita: il mio avversario")
    else:
        print(f"Hai tolto l'ultimo oggetto! Vince la partita: io")