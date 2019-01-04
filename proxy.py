from mitmproxy import ctx
import base64
import datetime
import eggobject

# TODO
# find the backup timestamp or the version control
# Fix the soul eggs fbug (in eggobject)
# Find the egg value 


class Proxy:
    def __init__(self):
        pass

    def request(self, flow):
        req = flow.request
        # http://www.auxbrain.com/ei/save_backup
        if req.host == 'www.auxbrain.com' and req.path == '/ei/save_backup':
            self.save(req.content, "save_backup")
            # flow.request.content = self.set_epic_research(flow.request.content)



    def response(self, flow):
        req = flow.request
        # http://www.auxbrain.com/ei/first_contact
        if req.host == 'www.auxbrain.com':
            if req.path == '/ei/first_contact':
                flow.response.content = self.set_epic_research(flow.response.content)

            if req.path == '/ei/get_contracts':
                content = base64.b64decode(flow.response.content)
                content = content.replace(b'Quantum Trash BagsRbWith all the wrapping paper and boxes to throw out, Quantum Trash bags are flying off the shelves!',
                                b'Maximal did it !! :)')
                flow.response.content = base64.b64encode(content)



    def set_epic_research(self, content, data=False):
        if data:
            binary_save = binary_save.replace('data=', '')
        binary_save = base64.b64decode(content)
        epic_research = eggobject.EpicResearch()
        binary_save = epic_research.mod(binary_save)
        if data:
            binary_save = 'data=' + binary_save
        return base64.b64encode(binary_save)

    def save(self, content, name, binary=True):
        name = name + ' {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        content = content.replace(b'data=', b'')
        if binary:
            with open(name, 'wb') as file:
                file.write(base64.b64decode(content))
        else:
            with open(name, 'w') as file:
                file.write(content)


addons = [
    Proxy()
]
