# Data Quality Checker

Data Quality Checker is a Django-based web application that provides robust insights into the quality of data within uploaded Excel files. Through a user-friendly interface, it evaluates datasets and offers feedback on potential issues, allowing for better and more informed data analysis and decision-making.

## Key Features:

- **Excel File Upload**: Seamless uploading of Excel datasets for evaluation.
- **Comprehensive Data Analysis**: Instant checks for:
  - Missing values
  - Duplicate entries
  - Inconsistent data formats
  - Recommended data type corrections
- **Downloadable Reports**: Option to download rows with data inconsistencies for further investigation.

## Getting Started:

### Prerequisites:

Ensure you have Python (3.8 or newer) and `pip` installed. Knowledge of Django's structure and command-line tools is advantageous but not necessary.

### Installation:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/data_quality_project.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd data_quality_project
   ```

3. **Install the Required Python Packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Application**:
   ```bash
   python manage.py runserver
   ```

Now, open a browser and navigate to `http://127.0.0.1:8000/upload/` to start using the Data Quality Checker!

## Contributing:

Your contributions are always welcome! Please have a look at the [contribution guidelines](CONTRIBUTING.md) first.  <!-- Link to a CONTRIBUTING.md if you have one -->

## Feedback:

Feel free to file an issue if you think something could be better. Pull requests are always welcome. Ensure to read the [contribution guidelines](CONTRIBUTING.md) before making changes.

## License:

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.  <!-- Link to a LICENSE file if you have one -->

## Acknowledgments:

- The Django framework for simplifying web development.
- The Python community for the comprehensive libraries and tools.
