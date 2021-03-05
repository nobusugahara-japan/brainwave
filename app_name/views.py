from django.shortcuts import render
from django.views import View
import pandas as pd

class SampleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'page01.html')

top_page = SampleView.as_view()

class UploadView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'page01.html')

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')
        file = files[0]
        df_t= pd.read_csv(file)
        idx=df_t[df_t['Alpha_AF7'].isnull() == False].index[0]
        df=df_t.fillna(method='ffill').fillna(0).iloc[idx:,:]
 #       df1=df[~df.iloc[:,1].isnull()]
        list_t=df['TimeStamp'].str[11:19].tolist()[20:]
        list_a7=df['Alpha_AF7'].rolling(20).sum().tolist()[20:]
        list_b7=df['Beta_AF7'].rolling(20).sum().tolist()[20:]
        list_a8=df['Alpha_AF8'].rolling(20).sum().tolist()[20:]
        list_b8=df['Beta_AF8'].rolling(20).sum().tolist()[20:]
        list_gap7=(df['Alpha_AF7']-df['Beta_AF7']).rolling(20).sum().tolist()[20:]
        list_gap8=(df['Alpha_AF8']-df['Beta_AF8']).rolling(20).sum().tolist()[20:]
        list_g7=df['Gamma_AF7'].rolling(20).sum().tolist()[20:]
        list_g8=df['Gamma_AF8'].rolling(20).sum().tolist()[20:]

        context={
            "list_t":list_t,
            "list_a7":list_a7,
            "list_b7":list_b7,
            "list_a8":list_a8,
            "list_b8":list_b8,
            "list_gap7":list_gap7,
            "list_gap8":list_gap8,
            "list_g7":list_g7,
            "list_g8":list_g8,
        }

        return render(request, 'Chart.html', context=context)

uploadview = UploadView.as_view()