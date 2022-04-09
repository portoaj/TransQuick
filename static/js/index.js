function summarize(){
  console.log('test');
  const textBoxValue = document.getElementById("transcript").value;
  fetch("/",{
    method: "POST",
    headers: {"Content-Type": "text/plain"},
    body: textBoxValue
  }).then(res => {
    console.log(res);
  });
}