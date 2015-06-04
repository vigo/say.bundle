def results(fields, original_query):
    message = fields['~message']
    html = "<h1>Saying: {0}</h1><p>Press enter!</p>".format(message)
    return {
        "title": "Say '{0}'".format(message),
        "run_args": [message],  # ignore for now,
        "html": html
    }

def run(message):
    import os
    os.system('say "{0}"'.format(message)) # TODO: proper escaping via pipes.quote