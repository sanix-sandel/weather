import os 
import re
import inspect

def _get_parser_list(dirname):
    files=[f.replace('.py', '')
        for f in os.listdir(dirname)
        if not f.startswith('__')] #The file name can't start with double underscores
    return files    

def _import_parsers(parserfiles):
    m=re.compile('.+parser$', re.I) #The .+ is the wildcard charcater()
    #matching everything (at least one character), re.I, ignore the cases
    _modules=__import__('weatherterm.parsers',
                        globals(),
                        locals(),
                        parserfiles,
                        0)
    _parsers=[(k, v) for k, v in inspect.getmemebers(_modules)
                if inspect.simodule(v) and m.match(k)]

    _classes=dict()

    for k, v in _parsers:
        _classes.update({k:v for k,v in inspect.getmembers(v)
                        if inspect.sclass(v) and m.match(k)})
        return _classes                    

def load(dirname):
    parserfiles=_get_parser_list(dirname)        
    return _import_parsers(parserfiles)