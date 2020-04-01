import pickle

class ScoreBoard():

    def  __init__(self, code_dict, score_dict):
        # code_dict = code6.pkl, code8.pkl
        # score_dict = 6.pkl,8.pkl
        self.code_dict = self.load_code_dict(code_dict)
        self.score_board = self.load_score_dict(score_dict)

    def load_code_dict(self, code_dict):
        with open (code_dict, 'rb') as f:
            code_dict = pickle.load(f)
            return code_dict

    def load_score_dict(self, score_dict):
        with open (score_dict, 'rb') as f:
            score_board = pickle.load(f)
            return score_board

    def decode(self, input_array):
        '''
        decode strings in the input_array

        :param input_array: 8 elements in one list,
        :return: a list

        '''
        n = len(input_array)
        decode_array = []
        for i in range(n):
            encoded_string = input_array[i]
            decoded_string = self.code_dict[encoded_string]
            decode_array.append(decoded_string)

        return decode_array

    def get_score(self, input_array):
        '''
        according to the current state, this function will calculate a score

        :param input_array: input_array: 8 elements in one list,
        :return: score for current state

        '''
        # change to new array
        decode_array = self.decode(input_array)

        # get the score
        score = 0
        for i in range(8):
            s1 = str(i) + decode_array[i]
            for j in range(i+1,8):
                s2 = str(j) + decode_array[j]
                s = s1 + s2
                score += self.score_board[s]

        return score










        