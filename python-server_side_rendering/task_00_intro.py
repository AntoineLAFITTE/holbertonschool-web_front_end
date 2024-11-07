import os

def generate_invitations(template, attendees):
    # Check if the template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if template is empty
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Iterate over each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with values or "N/A" if value is missing
        content = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Generate file name and write content to the file
        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as file:
                file.write(content)
            print(f"Generated {filename}")
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
