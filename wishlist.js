const product = [
    {
        id: 0,
        image: 'IMG-20241121-WA0020.jpg',
        title: 'John Deere 5425 DI',
        price: 35899,
    },
    {
        id: 1,
        image: 'IMG-20241121-WA0018.jpg',
        title: 'Mahindra 275 DI TU',
        price: 26799,
    },
    {
        id: 2,
        image: 'IMG-20241123-WA0001.jpg',
        title: 'Claas 620C Arion',
        price: 32699,
    },
    {
        id: 3,
        image: 'IMG-20241123-WA0002.jpg',
        title: 'Tafe 241 DI DYNATRACK',
        price: 29599,
    },
    {
        id: 4,
        image: 'IMG-20241121-WA0007.jpg',
        title: 'CAT D Series Dozers',
        price: 42399,
    },
    {
        id: 5,
        image: 'IMG-20241121-WA0009.jpg',
        title: 'Caterpillar Challenger MT700',
        price: 45799,
    },
    {
        id: 6,
        image: 'IMG-20241121-WA0011.jpg',
        title: 'Claas Jaguar 950 Forage Harvester',
        price: 49699,
    },
    {
        id: 7,
        image: 'IMG-20241121-WA0017.jpg',
        title: 'Fendt 724 Vario',
        price: 33799,
    },
    {
        id: 8,
        image: 'IMG-20241121-WA0016.jpg',
        title: 'Ford 5000',
        price: 38999,
    },
    {
        id: 9,
        image: 'IMG-20241123-WA0007.jpg',
        title: 'Ford 4860',
        price: 35399,
    },
    {
        id: 10,
        image: 'IMG-20241123-WA0005.jpg',
        title: 'New Holland Workmaster 25',
        price: 45899,
    },
    {
        id: 11,
        image: 'IMG-20241121-WA0006.jpg',
        title: 'Mahindra Arjun 6051',
        price: 39599,
    }
];
const categories = [...new Set(product.map((item)=>
    {return item}))]
    let i=0;
document.getElementById('root').innerHTML = categories.map((item)=>
{
    var {image, title, price} = item;
    return(
        `<div class='box'>
            <div class='img-box'>
                <img class='images' src=${image}></img>
            </div>
        <div class='bottom'>
        <p>${title}</p>
        <h2>$ ${price}.00</h2>`+
        "<button onclick='addtocart("+(i++)+")'>Wish</button>"+
        `</div>
        </div>`
    )
}).join('')

var cart =[];

function addtocart(a){
    cart.push({...categories[a]});
    displaycart();
}
function delElement(a){
    cart.splice(a, 1);
    displaycart();
}

function displaycart(){
    let j = 0, total=0;
    document.getElementById("count").innerHTML=cart.length;
    if(cart.length==0){
        document.getElementById('cartItem').innerHTML = "Your cart is empty";
        document.getElementById("total").innerHTML = "$ "+0+".00";
    }
    else{
        document.getElementById("cartItem").innerHTML = cart.map((items)=>
        {
            var {image, title, price} = items;
            total=total+price;
            document.getElementById("total").innerHTML = "$ "+total+".00";
            return(
                `<div class='cart-item'>
                <div class='row-img'>
                    <img class='rowimg' src=${image}>
                </div>
                <p style='font-size:12px;'>${title}</p>
                <h2 style='font-size: 15px;'>$ ${price}.00</h2>`+
                "<i class='bx bxs-trash' onclick='delElement("+ (j++) +")'></i></div>"
            );
        }).join('');
    }

    
}