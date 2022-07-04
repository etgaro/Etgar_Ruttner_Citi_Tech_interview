import pandas as pd
from row_of_entities import row_of_entities


class data_collector():
    def __init__(self):
        self.datatable = None
        self.rows = []  # list of entities

    def pre_process(self):
        # do something to the self.datatable
        pass

    def get_data_from_csv(self):
        self.datatable = pd.read_csv('input.csv')

    def repair_rows(self): #set the list of group of emtities
        for row in self.datatable.iterrows():

            row_entitie = row_of_entities(row[1][0])

            #period section
            row_entitie.set_year_from_row()

            #stock section
            row_entitie.set_stock_from_row()

            #amount section
            row_entitie.set_Amount_from_row()


            row_entitie.set_entities_offset(type='years')
            row_entitie.set_entities_offset(type='stock')
            row_entitie.set_entities_offset(type='amount')


            #add the repaired row
            self.rows.append(row_entitie)


    def print_enteties(self):
        # amount print
        print("\n--------AMOUNTS----------")
        for row in self.rows:
            print(row.entities['amount'], "\t offset = ",row.entities['stock_offset'])

        # Stock print
        print("\n--------STOCKS----------")
        for row in self.rows:
            print(row.entities['stock'], "\t offset = ",row.entities['stock_offset'])


        #years print
        print("--------YEARS----------")
        for row in self.rows:
            print(row.entities['years'], "\t offset = ",row.entities['years_offset'])


    # def output_to_csv(self):
    #     output = pd.DataFrame()
    #     for row in self.rows:
    #         row_to_df = [row.entities['amount'],row.entities['stock'],row.entities['years']]
    #         output.append(pd.DataFrame(row_to_df))
    #     print(output)
    #



