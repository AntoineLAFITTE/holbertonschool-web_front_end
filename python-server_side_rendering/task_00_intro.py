import os
""" Task 0: Creating a Simple Templating Program """

def generate_invitations(template, attendees):
    try:
        if not isinstance(template, str):
            raise TypeError("Template is not a string.")

        if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees
        ):
            raise TypeError("Attendees should be a list of dictionaries.")
    except TypeError as e:
        print(f"Error: {e}")
        return

    try:
        if not template.strip():
            raise ValueError("Template is empty, no output files generated.")

        if not attendees:
            raise ValueError("No data provided, no output files generated.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    for i, attendee in enumerate(attendees, start=1):
        output_content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            placeholder = "{" + key + "}"
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            output_content = output_content.replace(placeholder, value)

        output_filename = f"output_{i}.txt"
        if os.path.exists(output_filename):
            print(
                f"Warning: {output_filename} already exists. Skipping file creation."
            )
            continue

        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)
