import sys
sys.path.append("./generated")
sys.path.append("../../package/pywinrt/projection/pywinrt")

import _winrt
_winrt.init_apartment(_winrt.MTA)

def import_ns(ns):
    import importlib.machinery
    import importlib.util
    module_name = "_winrt_" + ns.replace('.', '_')
    loader = importlib.machinery.ExtensionFileLoader(module_name, _winrt.__file__)
    spec = importlib.util.spec_from_loader(module_name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module
