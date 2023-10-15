from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
import io
from .models import UploadedFile
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data = pd.read_excel(request.FILES['file'])
            results, failed_rows = analyze_data(data)

            # Convert DataFrame to CSV string and store in session
            csv_buffer = io.StringIO()
            failed_rows.to_csv(csv_buffer, index=False)
            request.session['failed_rows'] = csv_buffer.getvalue()

            return render(request, 'results.html', {'results': results})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def download_failed_rows(request):
    # Retrieve the CSV string and convert back to DataFrame
    csv_buffer = io.StringIO(request.session.get('failed_rows', ''))
    failed_rows = pd.read_csv(csv_buffer)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="failed_rows.csv"'
    failed_rows.to_csv(path_or_buf=response, index=False)
    return response


def analyze_data(data):
    total_values = data.size
    missing_values_total = data.isnull().sum().sum()
    total_rows = len(data)

    columns_data = {}
    failed_rows = pd.DataFrame()  # To collect rows with incorrect values
    
    for col in data.columns:
        unique_values = data[col].nunique()
        missing_values = data[col].isnull().sum()
        duplicated_values = data[col].duplicated().sum()

        invalid_values_count = 0
        actual_dtype = str(data[col].dtype)
        recommended_dtype = actual_dtype
        
        try:
            pd.to_numeric(data[col], errors='raise')
        except ValueError:
            invalid_values_count += 1
            if actual_dtype not in ['object', 'str']:
                recommended_dtype = "String or Categorical"

        mixed_data_formats = data[col].apply(lambda x: type(x)).nunique() > 1

        if mixed_data_formats:
            failed_rows = pd.concat([failed_rows, data[data[col].apply(lambda x: type(x)) != type(data[col].iloc[0])]])

        columns_data[col] = {
            'unique_values': unique_values,
            'missing_values': missing_values,
            'duplicated_values': duplicated_values,
            'invalid_values': invalid_values_count,
            'mixed_data_formats': mixed_data_formats,
            'actual_dtype': actual_dtype,
            'recommended_dtype': recommended_dtype
        }

    results_data = {
        'missing_values_total': missing_values_total,
        'total_values': total_values,
        'total_rows': total_rows,
        'columns_data': columns_data
    }

    return results_data, failed_rows.drop_duplicates()
