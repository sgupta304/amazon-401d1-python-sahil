def parse_text(template):
    cleaned_string = ""
    speech_parts = []
    capturing = False
    speech_part_in_progress = ""
    for char in template:
        if char == "{":
            cleaned_string += char
            capturing = True
        elif char == "}":
            cleaned_string += char
            capturing = False
            speech_parts.append(speech_part_in_progress)
            speech_part_in_progress = ""
        elif capturing:
            speech_part_in_progress += char
        else:
            cleaned_string += char
    return cleaned_string, tuple(speech_parts)
