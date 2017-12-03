


class nf_sefaz(object):

    def __init__(self, name, key):
        self.name = name
        self.key = key
        self.logs = []

    def add_log(self, log):
        self.logs.append(log)
