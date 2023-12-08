def summarize_data(data):
    attributes = len(data[0]) - 3  # Calculate the number of attributes

    # Initialize counters for each attribute and classification
    counts = {'Positive_Yes': [0] * attributes, 'Positive_No': [0] * attributes, 'Negative_Yes': [0] * attributes, 'Negative_No': [0] * attributes}

    # Determine unique values for 'Yes' and 'No' dynamically
    possible_yes_values = set()
    possible_no_values = set()

    for entry in data:
        for i in range(attributes):
            value = entry[i + 2]  # Attributes start from the third element
            if value.lower() == 'yes':
                possible_yes_values.add(i)
            elif value.lower() == 'no':
                possible_no_values.add(i)

    for entry in data:
        classification = entry[-1]  # Get the classification (Positive/Negative)
        for i in range(attributes):
            value = entry[i + 2]  # Attributes start from the third element

            # Update the corresponding counter based on classification and attribute value
            key = f'{classification}_Yes' if i in possible_yes_values else f'{classification}_No'
            counts[key][i] += 1

    return counts

# Rest of the code remains the same...


def create_html_table(result, attribute_titles):
    # Create the HTML table content with attribute titles
    table_content = "<table border='1'>\n"
    table_content += "<tr><th>Attribute</th><th>Positive Yes</th><th>Positive No</th><th>Negative Yes</th><th>Negative No</th></tr>\n"

    for i, (key, value) in enumerate(result.items()):
        attribute_name = attribute_titles[i + 2]
        table_content += f"<tr><td>{attribute_name}</td><td>{value[0]}</td><td>{value[1]}</td><td>{value[2]}</td><td>{value[3]}</td></tr>\n"

    table_content += "</table>\n"
    return table_content

# Example data
data = [['55', 'Female', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Negative'],
        ['57', 'Male', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Positive']]

# Example attribute titles
attribute_titles = ['Age', 'Gender', 'Polyuria', 'Polydipsia', 'Sudden Weight Loss', 'Weakness', 'Muscle Stiffness', 'Alopecia', 'Obesity', 'Class']

# Call the function and get the result
result = summarize_data(data)

# Create HTML table content with attribute titles
html_table_content = create_html_table(result, attribute_titles)

# Write HTML content to a file
filepath = 'output.html'
with open(filepath, 'w') as html_file:
    # Multiline F-string for better readability
    html_content = f"""
    <html>
    <head>
    <style>
    </style>
    </head>
    <body>
    {html_table_content}
    </body>
    </html>
    """
    html_file.write(html_content)

print(f"HTML content has been written to {filepath}")
