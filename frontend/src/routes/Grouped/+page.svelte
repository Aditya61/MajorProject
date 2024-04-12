<script>
    function analyze()
    {
        const attrib = document.getElementById("attribs").value;
        const val = document.getElementById("vals").value;
        let slug;
        if ( attrib == "Product Category" ) {
            slug = "ProductCategory,"+val;
        } else if ( attrib == "Payment Method" ) {
            slug = "PaymentMethod,"+val;
        } else if ( attrib == "Gender" ) {
            slug = "Gender,"+val;
        } else if ( attrib == "Age" ) {
            slug = "Age,"+val;
        } else if ( attrib == "Purchase Month" ) {
            slug = "Month,"+val;
        } else if ( attrib == "Purchase Year" ) {
            slug = "Year,"+val;
        } else if ( attrib == "Purchase Date" ) {
            let date = document.getElementById('date').value;
            slug = "Date,"+date;
        } else if ( attrib == "Total Purchase Amount" ) {
            slug = "TPAmt,"+val;
        } else if ( attrib == "Returns" ) {
            slug = "Returns,"+val;
        } else if ( attrib == "Churn" ) {
            slug = "Churn,"+val;
        }
        window.location.href = `http://localhost:5173/Grouped/${slug}`
    }
    function valoptions()
    {
        const select = document.getElementById('attribs');
        const valselect = document.getElementById('vals');
        valselect.innerHTML="";
        const parent = document.getElementById('Values');
        const attrib = select.value;
        let opts;
        if ( attrib == "Product Category" ) {
            opts = ["Home","Electronics","Books","Clothing"]
        } else if ( attrib == "Payment Method" ) {
            opts = ["PayPal","Credit Card","Cash","Crypto"]
        } else if ( attrib == "Gender" ) {
            opts = ["Male","Female"]
        } else if ( attrib == "Age" ) {
            opts = ["10-20","20-30","30-40","40-50","50-60","60-70","70-80"]
        } else if ( attrib == "Purchase Month" ) {
            opts = ["01","02","03","04","05","06","07","08","09","10","11","12"]
        } else if ( attrib == "Purchase Year" ) {
            opts = ["2020","2021","2022","2023"]
        } else if ( attrib == "Purchase Date" ) {
            let ip = document.createElement('input');
            ip.type = "date";
            ip.id = "date";
            parent.appendChild(ip);
        } else if ( attrib == "Total Purchase Amount" ) {
            opts = ["0-500","500-1000","1000-1500","1500-2000","2000-3000","3000-3500","3500-4000","4000-4500","4500-5000","5000-5500"]
        } else if ( attrib == "Returns" ) {
            opts = ["1","0"]
        } else if ( attrib == "Churn" ) {
            opts = ["1","0"]
        }
        if (opts.length) {
            opts.forEach(opt => {
                const option = document.createElement('option');
                option.innerHTML=opt;
                valselect.appendChild(option);
            });
        }
    }
</script>




<div class="w-full h-96 bg-slate-300 flex flex-wrap justify-around">
    <div class="h-40 p-8 w-auto">
        <center>
            <div class="flex flex-wrap gap-40 py-16">
                <div id="Attribues" class="w-56">
                    <p class="py-5 font-semibold">Select Attribute :</p>
                    <select id="attribs" on:change={valoptions} class="h-8 rounded-sm px-2">
                        <option>Attribues</option>
                        <option>Product Category</option>
                        <option>Payment Method</option>
                        <option>Gender</option>
                        <option>Age</option>
                        <option>Purchase Month</option>
                        <option>Purchase Year</option>
                        <option>Purchase Date</option>
                        <option>Total Purchase Amount</option>
                        <option>Returns</option>
                        <option>Churn</option>
                    </select>
                </div>
                <div id="Values" class="w-56">
                    <p class="py-5 font-semibold">Select Value :</p>
                    <select id="vals" class="w-48 h-8 rounded-sm px-2">
                    </select>
                </div>
            </div>
            <button on:click={analyze} class="h-10 w-40 border-2 m-2 hover:bg-purple-500 border-black bg-[#8ED1CD] font-semibold rounded-sm">Analyze</button>
        </center>
    </div>
</div>