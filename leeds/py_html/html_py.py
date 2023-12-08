def count_attributes(data):
    titles = ['Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness', 'muscle stiffness', 'Alopecia', 'Obesity', 'class']
    attributes = titles[2:-1]  
    attribute_counts = {}

    for i in range(len(attributes)):
        attribute_counts[attributes[i]] = {'Positive_Yes': 0, 'Positive_No': 0, 'Negative_Yes': 0, 'Negative_No': 0}

        for record in data:
            if record[-1] == 'Positive':
                if record[i + 2] == 'Yes':
                    attribute_counts[attributes[i]]['Positive_Yes'] += 1
                else:
                    attribute_counts[attributes[i]]['Positive_No'] += 1
            else:
                if record[i + 2] == 'Yes':
                    attribute_counts[attributes[i]]['Negative_Yes'] += 1
                else:
                    attribute_counts[attributes[i]]['Negative_No'] += 1

    return attribute_counts

def generate_html_table(attribute_counts):
    html_table = """
    <html>
    <head>
    <style>
    </style>
    </head>
    <body>
    <table border='1'>
    <tr><th>Attribute</th><th>Positive Yes</th><th>Positive No</th><th>Negative Yes</th><th>Negative No</th></tr>
    """

    for attribute, counts in attribute_counts.items():
        html_table += f"""<tr>
                            <td>{attribute}</td>
                            <td>{counts['Positive_Yes']}</td>
                            <td>{counts['Positive_No']}</td>
                            <td>{counts['Negative_Yes']}</td>
                            <td>{counts['Negative_No']}</td>
                        </tr>"""

    html_table += """
    </table>
    </body>
    </html>
    """

    return html_table

if __name__ == "__main__":
    data = [['55', 'Female', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Negative'],
            ['57', 'Male', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Positive'],
            ['66', 'Male', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Positive'],
            ['60', 'Male', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Positive']]

    attribute_counts = count_attributes(data)
    html_table = generate_html_table(attribute_counts)

    with open("output_table.html", "w") as file:
        file.write(html_table)
