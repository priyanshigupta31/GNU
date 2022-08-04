
"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param
        self.set_history(2)  #Example: The comand set_history(4) appends the first 4-1=3 previous items to the input buffer (input_items), while the 4'th item is the current value. Therefore,
            #input_items[0][3] is the beginning of the current input stream.
            #input_items[0][2] is one input older than the current input stream.
            #input_items[0][1] is one input older than input_items[0][2]
            #input_items[0][0] is one input older than input_items[0][1]
            
    def work(self, input_items, output_items):
        for i in range(0, len(output_items[0])):
            output_items[0][i]=input_items[0][i+1]/2+input_items[0][i]/2
        
        # print "length of input_items = ", len(input_items[0])
        # print "length of output_items = ", len(output_items[0])
        # print "len(input_items[0])-len(output_items[0]) = ", len(input_items[0])-len(output_items[0])
        return len(output_items[0])