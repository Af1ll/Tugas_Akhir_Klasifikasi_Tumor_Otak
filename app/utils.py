ALLOW_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    if '.' not in filename:
        return False
    extension = filename.rsplit('.', 1)[1].lower()
    return extension in ALLOW_EXTENSIONS