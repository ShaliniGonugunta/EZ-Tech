class CarShowroom:
    def __init__(self):
        self.companies = {
            '1': 'Toyota',
            '2': 'Honda',
            '3': 'Ford'
        }
        self.models = {
            'Toyota': ['Camry', 'Corolla', 'Prius'],
            'Honda': ['Civic', 'Accord', 'CR-V'],
            'Ford': ['Mustang', 'F-150', 'Explorer']
        }
        self.variants = {
            'Patrol': 1.2,
            'Diesel': 1.5
        }
        self.cgst = 0.05
        self.sgst = 0.05

    def carcompany(self):
        print("Select a car company:")
        for key, value in self.companies.items():
            print(f"{key}. {value}")
        company_choice = input("Enter the company number: ")
        if company_choice not in self.companies:
            print("Invalid choice. Please try again.")
            self.carcompany()
        else:
            self.selectmodel(self.companies[company_choice])

    def selectmodel(self, company):
        print(f"Select a model for {company}:")
        for model in self.models[company]:
            print(model)
        model_choice = input("Enter the model name: ")
        if model_choice not in self.models[company]:
            print("Invalid choice. Please try again.")
            self.selectmodel(company)
        else:
            self.selectvariant(company, model_choice)

    def selectvariant(self, company, model):
        print(f"Select a variant for {company} {model}:")
        for variant in self.variants:
            print(variant)
        variant_choice = input("Enter the variant name: ")
        if variant_choice not in self.variants:
            print("Invalid choice. Please try again.")
            self.selectvariant(company, model)
        else:
            self.calculateprice(company, model, variant_choice)

    def calculateprice(self, company, model, variant):
        base_price = 1000000  # Assuming a base price of 1,000,000
        variant_price = base_price * self.variants[variant]
        total_price = variant_price + (variant_price * self.cgst) + (variant_price * self.sgst)
        print(f"The total price of {company} {model} {variant} is: {total_price}")


showroom = CarShowroom()
showroom.carcompany()