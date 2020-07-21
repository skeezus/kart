


class URLBuilder(object):
    
    def __init__(self, base):
        self.base = base
        self.resources = []
        self.params = {}

    def add_resource(self, resource):
        self.resources.append(resource)

    def add_param(self, key, value):
        self.params[key] = value

    def build_url(self):
        for r in self.resources:
            self.base = '{0}/{1}'.format(self.base, r)

        if self.params:
            self.base = '{0}{1}'.format(self.base, '?')
            for k, v in self.params.items():
                self.base = '{0}{1}={2}{3}'.format(self.base, k, v, '&')

        return self.base