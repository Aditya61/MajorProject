<script>
    import { onMount } from "svelte";
    import Chart from 'chart.js';

    let prodcatChart = async function() {
        new Chart("pcat", {
            type: "pie",
            data: {
                labels: Object.keys(cust_data_analyzed.ProdCategory),
                datasets: [{
                    backgroundColor: ["red","blue","yellow","purple"],
                    data: Object.values(cust_data_analyzed.ProdCategory)
                }]
            },
            options: {
                title: {
                    display: true,
                    text: "Product Category"
                }
            }
        });
    } 

    let paymethodChart = async function() {
        new Chart("paym", {
            type: "pie",
            data: {
                labels: Object.keys(cust_data_analyzed.PaymentMethod),
                datasets: [{
                    backgroundColor: ["cyan","lavender","orange","lime"],
                    data: Object.values(cust_data_analyzed.PaymentMethod)
                }]
            },
            options: {
                title: {
                    display: true,
                    text: "Payment Method"
                }
            }
        });
    } 

    let returnChart = async function() {
        new Chart("returns", {
            type: "pie",
            data: {
                labels: Object.keys(cust_data_analyzed.ReturnStatus),
                datasets: [{
                    backgroundColor: ["crimson","purple"],
                    data: Object.values(cust_data_analyzed.ReturnStatus)
                }]
            },
            options: {
                title: {
                    display: true,
                    text: "Returns"
                }
            }
        });
    }

    export let data;
    let cust_data;
    let cust_data_analyzed = {
        "Name":"",
        "Gender":"",
        "TotalExpenses":0,
        "ProdCategory":{
            "Home":0,
            "Electronics":0,
            "Books":0,
            "Clothing":0
        },
        "PaymentMethod":{
            "PayPal":0,
            "Credit Card":0,
            "Cash":0,
            "Crypto":0
        },
        "ReturnStatus":{
            "Returned":0,
            "Not Returned":0
        },
        "Churn": false
    }

    onMount(async function() {
        const endpoint = `http://localhost:8000/api/customers/${data.id}/`
        let response = await fetch(endpoint)
        if (response.status == 200) {
            cust_data = await response.json()
            if(cust_data.length) {
                cust_data_analyzed.Name = cust_data[0].Name
                cust_data_analyzed.Gender = cust_data[0].Gender
                cust_data.forEach(cust => {
                    cust_data_analyzed.TotalExpenses += cust.TPAmt
                    cust_data_analyzed.ProdCategory[cust.Category] += cust.Quantity
                    cust_data_analyzed.PaymentMethod[cust.Payment] += 1
                    if ( cust.Returns == 0 ) {
                        cust_data_analyzed.ReturnStatus["Not Returned"] +=cust.Quantity
                    } else {
                        cust_data_analyzed.ReturnStatus["Returned"] += cust.Quantity
                    }
                    if ( cust.Churn == 1 ) {
                        cust_data_analyzed.Churn = true
                    }
                });
            }
            prodcatChart();
            paymethodChart();
            returnChart();
        } else {
            cust_data = null;
        }
    })
</script>

<div>
    <h1 class="text-2xl font-bold p-10">Individual Dashboard</h1>
    <p class="px-10 py-2 font-semibold">Name : {cust_data_analyzed.Name}</p>
    <p class="px-10 py-2 font-semibold">Gender : {cust_data_analyzed.Gender}</p>
    <p class="px-10 py-2 font-semibold">Total Expenses : {cust_data_analyzed.TotalExpenses}</p>
    <div class="grid grid-cols-3 p-10">
        <div>
            <canvas id="pcat" class=""></canvas>
        </div>
        <div>
            <canvas id="paym" class=""></canvas>
        </div>
        <div>
            <canvas id="returns" class=""></canvas>
        </div>
    </div>
    <p class="px-10 py-5 font-semibold">Churn Status : {cust_data_analyzed.Churn}</p>
</div>