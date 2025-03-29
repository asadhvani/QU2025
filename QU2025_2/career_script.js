window.onload = function() {
    document.getElementById('career-out').innerHTML = "xyz";//Add langchain integration
}

document.getElementById("interest-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission

    let inputData = document.getElementById("career-choicef").value;

    fetch("/submit_data", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "data_input=" + encodeURIComponent(inputData)
    })
        .then(response => response.text()) // Get response as text
        .then(data => {
            document.getElementById("career-out").innerText = "Server Response: " + data;
        })
        .catch(error => console.error("Error:", error));
    });