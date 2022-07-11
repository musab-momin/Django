from django import forms


class CarForm(forms.Form):
    name    = forms.CharField(label='Car')
    brand   = forms.CharField(label='Brand')
    price   = forms.CharField(label='Price')

    #perticular field validation prefix this method with clean_ and suffix it with your field name
    def clean_price(self):
        user_entered_price = self.cleaned_data['price']  #this will give you entered value
        print(f'''
        
            this is user entered price : {user_entered_price}
            {'.' in user_entered_price}
        ''')
        if '.' in user_entered_price:
            raise forms.ValidationError('Only Whole numbers are allowed')
        
        return user_entered_price     