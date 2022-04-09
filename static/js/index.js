function summarize(){
  const textBoxValue = document.getElementById("transcript").value;

  const options = {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify(textBoxValue),
    };

  fetch("/", options).catch(err => console.log(err)).then(res => res.json()).then(res => {
    document.getElementById("transcript").value = res['summary'];
  });
}