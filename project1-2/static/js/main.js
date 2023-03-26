const earnedIncomePayInput = document.getElementById('earnedIncomePay');
const earnedIncomeFamilySelect = document.getElementById('earnedIncomeFamily');
const earnedIncomeChildSelect = document.getElementById('earnedIncomeChild');
const calEarnedIncomeBtn = document.getElementById('cal_earnedIncome');
const clearEarnedIncomeBtn = document.getElementById('clear_earnedIncome');

const resultPannelDiv = document.getElementById('resultPannel');

const totalWithholding = document.getElementById('totalWithholding');

const incomeTax = document.getElementById('incomeTax');
const localIncomeTax = document.getElementById('localIncomeTax');
const totalIncomeTax = document.getElementById('totalIncomeTax');

const pensionInsurance = document.getElementById('pensionInsurance');
const totalPensionInsurance = document.getElementById('totalPensionInsurance');

const healthInsurance = document.getElementById('healthInsurance');
const longtermCareInsurance = document.getElementById('longtermCareInsurance');
const totalHealthInsurance = document.getElementById('totalHealthInsurance');

const employmentInsurance = document.getElementById('employmentInsurance');
const totalEmploymentInsurance = document.getElementById('totalEmploymentInsurance');

const visualizeComputeResult = (computeResult) => {

    totalWithholding.innerText = computeResult.total;

    incomeTax.innerText = computeResult.incomeTex.value;
    localIncomeTax.innerText = computeResult.incomeTex.localIncomeTax;
    totalIncomeTax.innerText = computeResult.incomeTex.total;

    pensionInsurance.innerText = computeResult.insurance.pension;
    totalPensionInsurance.innerText = computeResult.insurance.pension;

    healthInsurance.innerText = computeResult.insurance.health.value;
    longtermCareInsurance.innerText = computeResult.insurance.health.longtermCare;
    totalHealthInsurance.innerText = computeResult.insurance.health.total;

    employmentInsurance.innerText = computeResult.insurance.employment
    totalEmploymentInsurance.innerText = computeResult.insurance.employment
}

async function compute(incomePerMonthValue,famliy,child) {
    data = {
        'earnedIncomePay' : incomePerMonthValue,
        'earnedIncomeFamily' : famliy,
        'earnedIncomeChild' : child,
    }
    const response = await fetch('/compute', {
        method: 'POST',
        cache: 'no-cache',
        headers: {
      'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    resData = await response.json()
    return resData.answer;
}

const _compute = (incomePerMonthValue,famliy,child) => {
    const pensionInsuranceValue = calPensionInsurance(incomePerMonthValue);
    const totalHealthInsuranceValue = calHealthInsurance(incomePerMonthValue);
    const employmentInsuranceValue = calEmploymentInsurance(incomePerMonthValue);

    const totalWithholdingValue =  pensionInsuranceValue + totalHealthInsuranceValue + employmentInsuranceValue;
    const totalWithholdingText = calValueToText(totalWithholdingValue);

    totalWithholding.text = totalWithholdingText;

    return totalWithholdingValue
}

const onClickCalEarnedIncomeBtn = async () => {
    resultPannel.classList.add("hide-result");

    const incomePerMonthValue = Number(earnedIncomePayInput.value.replaceAll(',',''));
    const familyValue = Number(earnedIncomeFamilySelect.value);
    const childValue = Number(earnedIncomeChildSelect.value);

    result = await compute(incomePerMonthValue,familyValue,childValue);

    visualizeComputeResult(result);
    resultPannel.classList.remove("hide-result");
}

const clear = () => {
    earnedIncomePayInput.value = "";
    earnedIncomeFamilySelect.value = "1";
    earnedIncomeChildSelect.value = "0";

    resultPannel.classList.add("hide-result");
}


earnedIncomePayInput.onkeyup = (event) => {
    if(event.which >= 37 && event.which <= 40) return;
    earnedIncomePayInput.value = earnedIncomePayInput.value.replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}



calEarnedIncomeBtn.onclick = () => {
    if(!earnedIncomePayInput.value) {
        alert("급여를 입력해주세요");
        return
    }
    onClickCalEarnedIncomeBtn();
}

clearEarnedIncomeBtn.onclick = () => {
    clear()
}