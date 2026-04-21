async function send() {
    let input = document.getElementById("msg").value;

    let res = await fetch("http://<EC2-IP>:5000/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: input})
    });

    let data = await res.json();

    document.getElementById("chat").innerHTML += 
        "<p><b>You:</b> " + input + "</p>" +
        "<p><b>AI:</b> " + data.reply + "</p>";
}
