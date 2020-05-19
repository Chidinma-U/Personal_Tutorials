def format_customer(first_name, last_name, location = None):
    full_name = '%s %s' % (first_name, last_name)
    
    if location:
        return '%s (%s)' % (full_name, location)  #%s is the string object
    else:
        return full_name