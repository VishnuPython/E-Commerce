async function fetchData(){
    try{
        const res=await fetch("http://127.0.0.1:5000/products");
        const data=await res.json();
        return data;
    }
    catch(error){
        console.error(error);
    }
}

async function render(){
    const container=document.querySelector('.product-card');
    const data=await fetchData();

    if(!data){
        return;
    }

    data.forEach(product => {
        const card=document.createElement('div');
        card.classList.add('card');

        const Image=document.createElement('img')
        Image.src=product.imagePath;

        const title=document.createElement('h2');
        title.textContent=product.title;

        const price=document.createElement('h5');
        price.textContent='$'+product.price;

        const button=document.createElement('button');
        button.textContent="Add To Cart"


        card.appendChild(Image);
        card.appendChild(title);
        card.appendChild(price);
        card.appendChild(button);
        container.appendChild(card);
    });
}

render()

