class decor_quiz_result:
    def __init__(self, fn):
        self.origin = fn

    def __call__(self, subject, responses, quiz_data):
        cr, wr, sr = self.origin(self, subject, responses, quiz_data)
        print( "\n{0:.0%} is correct".format(sr[subject]) )
        if type(quiz_data) is type(dict()):
            print( "Found: {0}".format('; '.join(ans for ans in [el[0]+'='+el[1] for el in list(cr.items())]) ) )
            print( "Not Found: {0}".format('; '.join(ans for ans in [el[0]+'='+el[1] for el in list(wr.items())]) ) )
        else:
            print( "Found: {0}".format(' '.join(cr).title()) )
            print( "Not Found: {0}".format(' '.join(wr).title()) )