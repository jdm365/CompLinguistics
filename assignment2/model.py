import numpy as np
import nltk
from nltk.tokenize import word_tokenize



class NaiveBayes:
    def __init__(
            self, 
            text_file: str, 
            vocab_file: str = None, 
            alpha: float = 1.0
            ) -> None:
        with open(text_file, 'r') as f:
            self.tokens = word_tokenize(f.read())

        if vocab_file is not None:
            with open(vocab_file, 'r') as f:
                self.vocab = f.read().split()
        else:
            ## Vocab tokens
            self.vocab = list(set(self.tokens))

        self.vocab_size = len(self.vocab)
        self.n_tokens   = len(self.tokens)

        self.word_counts = self.get_all_word_counts()

        ## Laplace smoothing factor
        self.alpha = alpha


    def get_all_word_counts(self) -> dict:
        word_counts = {}
        for word in self.vocab:
            word_counts[word] = len(np.where(self.tokens == word))
        return word_counts


    def get_word_context_count(self, words: set) -> int:
        count = 0
        for idx in range(self.n_tokens - 1):
            scanned_words = {self.tokens[idx], self.tokens[idx+1]}
            count += scanned_words == words
        return count


    def calc_likelihood(self, word: str, context: str):
        ## Assuming bigram model for now.
        N_yi = self.get_word_context_count({context, word})
        N_y  = self.word_counts[word]
        return (N_yi + alpha) / (N_y + alpha * self.n_tokens)

    
    def find_max_liklihoods(self, context: str) -> dict:
        liklihoods = {}
        for word in self.vocab:
            liklihoods[word] = self.calc_likelihood(word, context)
        return {word: prob for word, prob in sorted(liklihoods.items(), key=lambda x: x[1], reverse=True)}












if __name__ == '__main__':
    ########################################################
    ####                    TESTING                     ####
    ########################################################
    model = NaiveBayes(
            text_file='data/TheLongPatrol.txt'
            )
    print(model.tokens)
