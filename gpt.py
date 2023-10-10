import csv
import openai

openai.api_key = 'KEY'

with open("bio.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip the header

    with open('tech.csv', 'w', newline='') as tech_file:
        tech_writer = csv.writer(tech_file)
        tech_writer.writerow(['URL', 'Bio'])  # Write the header

        for row in reader:
            url, bio = row

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    temperature=0.5,
                    messages=[
                        {"role": "system", "content": "You are a curt assistant who writes short answers. If the bio suggests the person is using cutting-edge or emerging technology (not science) to do social good, reply a sentence in the format 'Technology: Using <type of technology> to <explain the impact>'. An example is 'Campaigning against government surveillance technology in the US.' or 'Ryan Gersava runs Virtualahan, a Filipino technology school for the chronicly unemployed.' Have a high bar for this. You MUST MUST MUST use the word 'technology'. If not, reply with a short, curt concise explanation for why not in under 5 words."},
                        {"role": "user", "content": bio}
                    ]
                )

                result = response.choices[0].message.content
                if ("echnology" in result) or ("echnology" in bio):
                    tech_writer.writerow([url, bio])
                    print("Tech person:", result, url)
                else:
                    print("Not tech:", result, url)
            except Exception as e:
                print(f"An error occurred: {e}")