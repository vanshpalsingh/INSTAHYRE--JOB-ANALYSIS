from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__, template_folder='templates')

# Load your job listings data
data = pd.read_csv(r"D:\MASAI\PROJECT\Shivanni\job Analysis\JOB_FINAL.csv")

# Initialize a variable to store filtered data
filtered_data = None

@app.route('/')
def index():
    # Add the skill_query parameter to clear the input field
    return render_template('index.html', skill_query='')

@app.route('/result', methods=['POST'])
def search_jobs():
    global filtered_data  # Access the global variable

    if request.method == 'POST':
        # Get the user's input for skills
        skill_query = request.form['skill_query']

        # Split the user's input on commas
        skills = [skill.strip() for skill in skill_query.split(',')]

        # Filter the data based on user input
        filtered_data = data[data['Skills'].str.contains('|'.join(skills), case=False, na=False)]

        # Check if there are any results
        if filtered_data.empty:
            return render_template('result.html', error_message='No matching skills found.')

        # Analyze the filtered data
        most_common_companies = filtered_data['Company'].value_counts().head(10).index.tolist()
        most_common_experience = filtered_data['Experience'].value_counts().idxmax()
        most_common_cluster = filtered_data['Cluster'].value_counts().idxmax()
        total_companies = len(filtered_data)

        return render_template('result.html', most_common_companies=most_common_companies, most_common_experience=most_common_experience, most_common_cluster=most_common_cluster, total_companies=total_companies, skill_query=skill_query)

    return render_template('index.html', skill_query='')

@app.route('/all_job_details')
def all_job_details():
    global filtered_data  # Access the global variable

    if filtered_data is not None:
        # Load filtered job details data
        all_job_details_data = filtered_data.to_dict('records')
        return render_template('all_job_details.html', all_job_details_data=all_job_details_data)

    return render_template('all_job_details.html', all_job_details_data=[])

if __name__ == '__main__':
    app.run(debug=True)
