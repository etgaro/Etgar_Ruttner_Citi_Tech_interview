import Data_collector_and_repair as dcar

if __name__ == '__main__':
    data_repair = dcar.data_collector()
    data_repair.get_data_from_csv()
    data_repair.repair_rows()
    data_repair.print_enteties()
    print('done')