import time
from bci_framework.extensions.data_analysis import DataAnalysis, loop_consumer, fake_loop_consumer
import logging


# 4/0

########################################################################
class Stream(DataAnalysis):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)

        self.create_buffer(30, samples=1000)
    
        # 5/0
    
        
        # print("@"*10)
        logging.warning("@"*10)
        
        self.stream()
        

    # ----------------------------------------------------------------------
    @fake_loop_consumer('eeg')
    def stream(self, frame):
        """"""
        eeg = self.buffer_eeg_resampled
        
        print("="*10)
        print("Holas\n")
        logging.critical(frame)
        logging.error(frame)
        logging.warning(frame)
        logging.info(frame)
        logging.debug(frame)
        


if __name__ == '__main__':
    Stream()