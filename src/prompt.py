from cmd import Cmd


class AppPrompt(Cmd):
    prompt = '#> '
    intro = '''Welcome! Type ? to list commands\nType 'quit' to exit. \
Press 'Enter' to continue'''

    def do_exit(self, inp):
        '''exit the application'''
        print("Bye")
        return True

    def do_add(self, inp):
        '''add anything'''
        print("Adding '{}'".format(inp))
