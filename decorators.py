def module_help(module_name: str):
    def decorator(func):
        func.__MODULE__ = module_name
        return func
    return decorator

print("Helpo decorators module loaded")
