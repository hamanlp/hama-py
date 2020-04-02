import os
import json
from hama.langutils import Singleton


class TagHMM(metaclass=Singleton):
    """Class that represents the Hidden Markov Transition between POS tags.
    
    Attributes:
        hmm (list): 2-D list representing the state transition matrix.
        t2i (dict): Dictionary mapping tag to index within mat axis.

    """

    def __init__(self):
        """Initialize singleton TagSeqHMM class."""
        super().__init__()
        self.hmm = None

    def __getattr__(self, name):
        """Called when an called attribute does not exist."""
        return None

    def load(self):
        """Loads hmm into memory."""
        if self.hmm is None:
            hmm_path = os.path.join(os.path.dirname(__file__),
                                    'resource/hmm.json')
            with open(hmm_path) as f:
                data = json.load(f)
                self.hmm = data['hmm']
                self.t2i = data['t2i']

    def unload(self):
        """Unloads hmm from memory."""
        self.hmm = None
        self.t2i = None

    def query(self, t1, t2):
        """Queries the transition possibility between tags.

        Args:
            t1 (str): Previous tag.
            t2 (str): Next tag.
        
        Returns:
            float: Transition possibility from t1 to t2. 
        
        Raises:
            Exception if t1 and t2 are not valid POS tags,
            or if TagHMM is not initialized by calling load()
        """
        if self.hmm is None:
            raise Exception("Initialize HMM before querying!")

        if t1 not in self.t2i or t2 not in self.t2i:
            raise Exception(
                f"One of the following tags was invalid: [{t1}, {t2}]")

        t1_i = self.t2i[t1]
        t2_i = self.t2i[t2]

        return self.hmm[t1_i][t2_i]
