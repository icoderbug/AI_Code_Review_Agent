def detect_language(filename):

    extension = filename.split(".")[-1].lower()

    languages = {
        "py": "Python",
        "java": "Java",
        "cpp": "C++",
        "c": "C",
        "js": "JavaScript",
        "rb": "Ruby"
    }

    return languages.get(extension, "Unknown")