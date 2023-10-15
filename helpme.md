# Help & Troubleshooting Guide

If you're encountering issues or have questions regarding the Data Quality Checker application, this document is here to assist!

## Common Issues:

### 1. 'NaTType is not JSON serializable' error:
Ensure you're using the latest version of the project. This issue was addressed in recent updates. If the problem persists, consider raising an issue on the GitHub repository.

### 2. Missing modules:
Make sure you've installed all the required dependencies using:
```bash
pip install -r requirements.txt
```

### 3. Database errors:
Try resetting the migrations and the database:
```bash
python manage.py migrate --zero
python manage.py makemigrations
python manage.py migrate
```

## Frequently Asked Questions (FAQ):

### Q: I've uploaded a valid Excel file, but I'm not getting any results?
**A**: Ensure the Excel file format is supported (e.g., `.xls`, `.xlsx`). If the problem persists, it might be due to specific content in the Excel file that the application might not handle yet. Consider raising an issue with a sample dataset.

### Q: Can I check multiple Excel files at once?
**A**: As of the current version, the application supports the analysis of one Excel file at a time. Future updates might incorporate batch processing.

### Q: The application recommends a data type change, but I believe the original type is correct. Why is this?
**A**: Recommendations are based on common patterns detected in the dataset. If the data has variations or unique values, the recommendation might not always be perfect. Always use domain knowledge alongside the tool's feedback.

### Q: How can I contribute to the project or suggest features?
**A**: We appreciate contributions and feedback! Please refer to the `README.md` for guidelines on contributing. You can also raise feature requests as issues on the GitHub repository.

## Further Assistance:

If you encounter any other issues, please:
1. Check Django's official documentation and forums.
2. Consult Python and Pandas documentation for any library-specific issues.
3. Raise an issue on the GitHub repository with a detailed description of the problem.

Thank you for using the Data Quality Checker!
