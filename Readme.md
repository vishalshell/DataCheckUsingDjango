# Data Quality Checker

A Django-based web application that allows users to upload Excel files and analyzes the data quality of the uploaded content. It checks for general data quality metrics as well as column-wise metrics including missing values, unique values, and duplicated values.

## Features

- Upload Excel files and instantly get feedback on data quality.
- Check for total missing values and unique values in the dataset.
- Column-wise analysis to identify missing and duplicated values for each column.
- Intuitive web interface for easy use.

## Installation and Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/data_quality_project.git
    cd data_quality_project
    ```

2. **Set up a Virtual Environment**

    ```bash
    python -m venv venv
    # Activate the virtual environment
    # On Windows:
    venv\Scripts\activate
    # On macOS and Linux:
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Start the Development Server**

    ```bash
    python manage.py runserver
    ```

6. **Access the Application**

    Open your web browser and navigate to `http://127.0.0.1:8000/upload/`.

## Usage

1. Use the web interface to upload your Excel file.
2. The system will analyze the data and provide results on data quality.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
