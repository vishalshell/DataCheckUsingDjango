# Create your views here.
import pandas as pd
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            file_path = form.instance.file.path
            data = pd.read_excel(file_path)
            
            # Analyze the data quality
            results = analyze_data(data)
            return render(request, 'results.html', {'results': results})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def analyze_data(data):
    # General Analysis
    total_values = data.size
    missing_values_total = data.isnull().sum().sum()
    
    # Column-wise analysis
    columns_data = {}
    for col in data.columns:
        unique_values = data[col].nunique()
        missing_values = data[col].isnull().sum()
        duplicated_values = data[col].duplicated().sum()

        columns_data[col] = {
            'unique_values': unique_values,
            'missing_values': missing_values,
            'duplicated_values': duplicated_values,
        }

    return {
        'missing_values_total': missing_values_total,
        'total_values': total_values,
        'columns_data': columns_data
    }


