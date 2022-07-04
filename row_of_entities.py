class row_of_entities():
    def __init__(self,perliminary_string):
        self.entities = {}
        self.entities['perliminary_string'] = perliminary_string


    def set_year_from_row(self):
        split_row = self.entities['perliminary_string'].split()
        if 'yr' in split_row[-1]:
            val = split_row[-1][0]
        elif 'years' in split_row[-1]:
            val = split_row[-2][0]
        elif 'yr' in split_row[-3]:
            val = split_row[-3][0]
        else:
            print('Not recognize')
            return None
        self.entities['years'] = val+' years'
        return val

    def set_Amount_from_row(self):
        split_row = self.entities['perliminary_string'].split()
        val = None
        for word in split_row:

            if word[-2:] == 'MM':
                val = int(word[0])*1000000
                break

            if word == 'some':
                val = -1
                break

            if word[-1] == 'a': #for the 6'th line
                try:
                    val = int(word[:-1])
                    break
                except:
                    pass
                break

            try:
                val = int(word)
                break
            except:
                pass

        self.entities['amount'] = val
        return val

    def set_stock_from_row(self):
        split_row = self.entities['perliminary_string'].split()
        val = None
        for word in split_row:
            if len(word) == 3 and word.isupper():
                val = word
                break

            if len(word) == 4 and word[0:3].isupper():
                val = word[0:3]
                break

        self.entities['stock'] = val
        return val


    def set_entities_offset(self,type):
        try:
            self.entities[type+'_offset'] = self.entities['perliminary_string'].split().index(self.entities[type])+1 #return the place (1 for the first)
        except:
            self.entities[type+'_offset'] = 'cant_find_need_to_work_harder'




