
def read_binr(self, com):
    start_time = time()
    response = b''
    if not com.warm_request: 
        if com.in_waiting >= 1924:
            while (response[-1] == 3) and (response[-2] == 16) and (response[-3] != 16):
                response += com.read(com.in_waiting)
            com.reset_input_buffer()
            return (com, response)
    elif com.in_waiting == 6:
        com.reset_input_buffer()
        com.write(self.request)
        com.warm_request = False
    else:
        return (com, None)