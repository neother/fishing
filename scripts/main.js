let randomNumber = Math.floor(Math.random() * 100) + 1;

const resp = document.querySelector('.resp');

x = 3
const guessSubmit = document.querySelector('.guessSubmit');

  function httprequest() {
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "http://hq.sinajs.cn/list=SR1909", false ); // false for synchronous request
    xmlHttp.setRequestHeader("Access-Control-Allow-Methods", "GET");
    xmlHttp.send( null );
    return xmlHttp.responseText.toString();
}

function test() {
        
        resp.textContent = Math.floor(Math.random() * 1000) + 1;;
        resp.style.fontSize = '200%';
        console.log(resp.textContent);
    }

setInterval(test,1000
    )

  guessSubmit.addEventListener('click', test);