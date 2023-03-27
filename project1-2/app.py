from flask import Flask
from flask import request
from flask import send_file
import json
import tax
import computation

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('static/index.html')

@app.route('/compute', methods = ['POST'])
def compute():
    params = json.loads(request.get_data())
    earned_income_pay = params.get('earnedIncomePay')
    earned_income_family = params.get('earnedIncomeFamily')
    earned_income_child = params.get('earnedIncomeChild')

    income_tax = computation.compute_income_tax(earned_income_pay, earned_income_family+earned_income_child)
    local_income_tax = computation.compute_local_income_tax(income_tax)

    pension_insurance = computation.compute_pension_insurance(earned_income_pay)

    health_insurance = computation.compute_health_insurance(earned_income_pay)
    longterm_care_insurance = computation.compute_longterm_care_insurance(health_insurance)
    total_health_insurance = computation.compute_total_health_insurance(health_insurance,longterm_care_insurance)

    employment_insurance = computation.compute_employment_insurance(earned_income_pay)

    total_income_tax = computation.compute_total_income_tax(income_tax, local_income_tax)
    total_insurance = computation.compute_total_insurance(pension_insurance,total_health_insurance,employment_insurance)

    total_withholding = computation.compute_total_withholding(total_income_tax,total_insurance)

    return {
                'message': 'success',
                'answer': {
                    'incomeTex': {
                        'value': f'{income_tax:,}',
                        'localIncomeTax': f'{local_income_tax:,}',
                        'total': f'{total_income_tax:,}',
                    },
                    'insurance': {
                        'pension': f'{pension_insurance:,}',
                        'health': {
                            'value': f'{health_insurance:,}',
                            'longtermCare': f'{longterm_care_insurance:,}',
                            'total': f'{total_health_insurance:,}',
                        },
                        'employment': f'{employment_insurance:,}',
                        'total': f'{total_insurance:,}',
                    },
                    'total': f'{total_withholding:,}',
                },
            }




if __name__ == '__main__':  # pragma: no cover
    tax.load_tax_table('tax_table.csv')
    app.run(port=8081)