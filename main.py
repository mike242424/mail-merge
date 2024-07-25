with open('Input/Letters/starting_letter.txt', 'r') as letter_file:
    letter = letter_file.read()

with open('./Input/Companies/companies_list.txt', 'r') as companies_file:
    companies_list = []
    companies = list(companies_file.readlines())
    for company in companies:
        stripped_companies = company.replace('\n', '')
        companies_list.append(stripped_companies)

for company in companies_list:
    with open('./Output/ReadyToSend/' + company + '.txt', 'w') as company_letters:
        new_letters = letter.replace('[name]', company)
        company_letters.write(new_letters)