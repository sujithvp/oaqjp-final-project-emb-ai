let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    fetch("/emotionDetector", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ statement: textToAnalyze })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("system_response").innerHTML = data.message;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("system_response").innerHTML = "An error occurred.";
    });
}
