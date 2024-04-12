<script>
    import { onMount } from 'svelte';
    import Chart from 'chart.js';

    export let data;

    let cust_data_analyzed = {
        No_of_items : 0,
        ProductCategory : {
            "Home":0,
            "Electronics":0,
            "Books":0,
            "Clothing":0
        },
        PaymentMethod : {
            "PayPal":0,
            "Credit Card":0,
            "Cash":0,
            "Crypto":0
        },
        Gender : {
            "Male":0,
            "Female":0
        },
        Age : {},
        Returns : {
            Returned : 0,
            Not_Returned : 0
        },
        Churn : {
            Churned : 0,
            Not_Churned : 0
        }
    }

    let ageChart = async function() {
        new Chart("age", {
            type: "bar",
            data: {
                labels: Object.keys(cust_data_analyzed.Age),
                datasets: [{
                    backgroundColor: 'purple',
                    data: Object.values(cust_data_analyzed.Age)
                }]
            },
            options: {
                legend: {display: false},
                title: {
                    display: true,
                    text: "Age of Customers"
                }
            }
        });
    } 

    let prodcatChart = async function() {
        new Chart("pcat", {
            type: "bar",
            data: {
                labels: Object.keys(cust_data_analyzed.ProductCategory),
                datasets: [{
                    backgroundColor: 'red',
                    data: Object.values(cust_data_analyzed.ProductCategory)
                }]
            },
            options: {
                legend: {display: false},
                title: {
                    display: true,
                    text: "Product Category"
                }
            }
        });
    } 

    let paymethodChart = async function() {
        new Chart("paym", {
            type: "bar",
            data: {
                labels: Object.keys(cust_data_analyzed.PaymentMethod),
                datasets: [{
                    backgroundColor: 'blue',
                    data: Object.values(cust_data_analyzed.PaymentMethod)
                }]
            },
            options: {
                legend: {display: false},
                title: {
                    display: true,
                    text: "Payment Method"
                }
            }
        });
    } 

    let genderChart = async function() {
        new Chart("gender", {
            type: "pie",
            data: {
                labels: Object.keys(cust_data_analyzed.Gender),
                datasets: [{
                    backgroundColor: ["orange","green"],
                    data: Object.values(cust_data_analyzed.Gender)
                }]
            },
            options: {
                title: {
                    display: true,
                    text: "Gender"
                }
            }
        });
    } 

    let returnChart = async function() {
        new Chart("returns", {
            type: "pie",
            data: {
                labels: Object.keys(cust_data_analyzed.Returns),
                datasets: [{
                    backgroundColor: ["crimson","lime"],
                    data: Object.values(cust_data_analyzed.Returns)
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

    let churnChart = async function() {
        new Chart("churn", {
            type: "pie",
            data: {
                labels: Object.keys(cust_data_analyzed.Churn),
                datasets: [{
                    backgroundColor: ["lavender","magenta"],
                    data: Object.values(cust_data_analyzed.Churn)
                }]
            },
            options: {
                title: {
                    display: true,
                    text: "Churn"
                }
            }
        });
    } 



    let cust_data;
    let attrib=data.attrib
    let val=data.val
    if ( attrib == "Month" ) {
        attrib = "P_Date/"+attrib;
    } else if ( attrib == "Year" ) {
        attrib = "P_Date/"+attrib;
    } else if ( attrib == "Date" ) {
        attrib = "P_Date/"+attrib;
    }
    onMount(async function() {
        const endpoint = `http://localhost:8000/api/customers/${attrib}/${val}/`
        let response = await fetch(endpoint)
        if (response.status == 200) {
            cust_data = await response.json()
            cust_data_analyzed.No_of_items = cust_data.length
            cust_data.forEach(cust => {
                cust_data_analyzed.ProductCategory[cust.Category] += cust.Quantity
                cust_data_analyzed.PaymentMethod[cust.Payment] += 1
                cust_data_analyzed.Gender[cust.Gender] += 1
                if (cust_data_analyzed.Age[cust.Age]) {
                    cust_data_analyzed.Age[cust.Age] += 1
                } else {
                    cust_data_analyzed.Age[cust.Age] = 1
                }
                if ( cust.Returns == 0 ) {
                    cust_data_analyzed.Returns.Not_Returned += cust.Quantity
                } else {
                    cust_data_analyzed.Returns.Returned += cust.Quantity
                }
                if ( cust.Churn == 0 ) {
                    cust_data_analyzed.Churn.Not_Churned += 1
                } else {
                    cust_data_analyzed.Churn.Churned += 1
                }
            });
            ageChart();
            prodcatChart();
            paymethodChart();
            genderChart();
            returnChart();
            churnChart();
        } else {
            cust_data = null;
        }
    })
</script>

<div>
    <h1 class="text-2xl font-bold p-10">Grouped Dashboard</h1>
    <p class="px-10 py-5 font-semibold"> Number of data points retrieved : {cust_data_analyzed.No_of_items}</p>
    <div class="p-10 grid grid-cols-3">
        <div class="col-span-2 row-span-2">
            <canvas id="age" class="h-auto w-auto"></canvas>
        </div>
        <div>
            <canvas id="pcat" class=""></canvas>
        </div>
        <div>
            <canvas id="paym" class=""></canvas>
        </div>
        <div class="row-span-2">
            <canvas id="gender" class=""></canvas>
        </div>
        <div class="row-span-2">
            <canvas id="returns" class=""></canvas>
        </div>
        <div class="row-span-2">
            <canvas id="churn" class=""></canvas>
        </div>
    </div>
</div>