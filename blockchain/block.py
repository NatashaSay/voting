import json
import hashlib


class Blockchain:

    def __init__(self):
        self.chain = []
        self.votings = {}
        #self.create_block(prev_hash = '0')
        #self.nodes = set()

    def hashoverride(self, block):

        encoded_block = str(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()


    def get_last_block(self):
        with open('blockchain/txt/text.txt', 'r') as f:
            data_new = str(f.read())
            data_new=data_new.split('}{')
            print(data_new[-1], 'datanew')
            return data_new


    def create_block(self, profile, voting, time, option, prev_hash=0):

        def gethash(block):

            encoded_block = str(block).encode()
            return hashlib.sha256(encoded_block).hexdigest()




        block = {
            'profile': profile,
            'voting': voting,
            'time': str(time),
            'option': option,
            'hash': prev_hash
        }
        # f = open('blockchain/txt/text.txt', 'w')
        # for key,val in block.items():
        #     f.write('{}:{}\n'.format(key,val))
        #
        # f.close()



        #block.hash = gethash("5")

        with open('blockchain/txt/text.txt', 'a') as file:
            json.dump(block, file, indent=4, ensure_ascii=False)

        #self.votings = {}
        self.chain.append(block)
        return block






     # def is_chain_valid(self, chain):
     #    previous_block = chain[0]
     #    block_index = 1
     #    while block_index < len(chain):
     #        block = chain[block_index]
     #        if block['previous_hash'] != self.hash(previous_block):
     #            return False
     #        previous_nonce = previous_block['nonce']
     #        nonce = block['nonce']
     #        hash_operation = hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()
     #        if hash_operation[:4] != '0000':
     #            return False
     #        previous_block = block
     #        block_index += 1
     #    return True
     #
     #
     # def add_transaction(self, sender, receiver, amount, time):
     #    self.transactions.append({'sender': sender,
     #                              'receiver': receiver,
     #                              'amount': amount,
     #                              'time': str(datetime.datetime.now())})
     #    previous_block = self.get_last_block()
     #    return previous_block['index'] + 1





def check():
    return None


def createblock(profile, voting, time, option, prev_hash=''):

    block = {
        'profile': profile,
        'voting': voting,
        'time': time,
        'option': option,
        'hash': prev_hash
    }
    prev_block = {

    }
    prev_hash = gethash(str(prev_block))
