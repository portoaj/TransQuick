function summarize(){
  console.log('test');
  const textBoxValue = document.getElementById("transcript").value;

  const options = {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify(textBoxValue),
    };

  fetch("/", options).catch(err => console.log(err)).then(res => {
    console.log(res);
  });
}