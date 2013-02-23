def my_import(name):
	mod = __import__(name)
	components = name.split('.')
	for comp in components[1:]:
		mod = getattr(mod, comp)
	return mod

# def import_all(name):
# 	#usbase.models
# 	mod = __import__(name)
# 	components = name.split('.')
# 	for comp in components[1:]:
		