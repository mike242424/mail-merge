with open('Input/Letters/starting_letter.txt', 'r') as letter:
    letter_contents = letter.read()
    print(letter_contents)

with open('./Input/Companies/companies_list.txt', 'r') as companies:
    companies_list = []
    companies_contents = list(companies.readlines())
    for company in companies_contents:
        stripped_companies = company.replace('\n', '')
        companies_list.append(stripped_companies)

for company in companies_list:
    with open('./Output/ReadyToSend/' + company + '.txt', 'w') as company_letters:
        new_letters = letter_contents.replace('[name]', company)
        company_letters.write(new_letters)