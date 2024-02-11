$url = ""
function Async_Data(sql, url) {
    
 $.ajax({
        method: 'post',
        url: url,
        data: {
            'sql': sql
        },
        async: false,
        dataType: 'json',
        success: function (data) {
            if (data.length > 0) {
                datos = data
                // console.log(data)
                // alert('hay datos')
            }   
        }
    })
    return datos    
}

function NotAsync_Data(sql,cod_producto, url) {
    alert()
 $.ajax({
        method: 'post',
        url: url,
     data: {
            'sql': sql,
            'cod_producto': cod_producto
        },
        dataType: 'json',
        success: function (data) {
            if (data.length > 0) {
                alert("entro")
                datos = data
            }   
        }
    })
}

function cargaDatos() {
    // const sql = "select txt_desc,imp_precio,cant,descuento from timagen"
    const sql="select * from timagen"
    const div = document.querySelector('#lista')
    // const p = document.createElement('p')
    // p.innerText = "nuevo"
    // label.innerText="etiqueta nueva"
    
    datos=Async_Data(sql, './cnn/imagen.php');    
    if (datos) {
        datos.forEach(elem => {
            
            const lprecio = document.createElement('p')
            const imp = document.createElement('p')
            const ahorro = document.createElement('p')
            const cant=document.createElement('p')
            const spacio = document.createElement('p')
            const spacio1 = document.createElement('p')
            const spacio2 = document.createElement('p')
            const cod_producto = document.createElement('label')
            const ndiv = document.createElement('div')
            const descuento = document.createElement('div')
            const label = document.createElement('label')
            const img = document.createElement('img')
            // texto 
            lprecio.style.fontWeight = "bold"
            cant.style.fontWeight = "bold"
            img.src = "data:imagen/png;base64," + elem.imagen
            img.style.height="140px"
            descuento.className = "div-des"
            descuento.append('Ahorra ' + elem.descuento + '%')
            spacio.style.color = "white"
            spacio1.style.color = "white"
            spacio2.style.color="white"
            ndiv.style.color="black"
            ndiv.style.height = "20rem"
            label.style.color = "black"
            lprecio.style.color = "rgb(124, 7, 170)"
            cant.style.color = "rgb(124, 7, 170)"
            imp.style.color="rgb(124, 7, 170)"
            ahorro.style.color="rgb(124, 7, 170)"
            cod_producto.style.display = "none"

            spacio.innerText = ".."
            spacio1.innerText = " .."
            spacio2.innerText = " .."
            
            
            ndiv.append(descuento, spacio,img,spacio1)
            cod_producto.innerText=elem.cod_producto
            descuento.className = "div-des"
            // ndiv.style.color="white"
            // Style
            
            label.innerText = elem.txt_desc.toLowerCase().substring(0,24)+'..'
            cant.innerText='Disponible '+elem.cant
            ndiv.className = "div-20"
            // ndiv.style.float="none"
            imp.innerText = 'Antes S/ '+elem.imp_descuento.toFixed(2)
            ndiv.append(label,spacio2,imp)
            ahorro.innerText = 'Ahorro de S/ '+(elem.imp_descuento-elem.imp_precio).toFixed(2)
            ndiv.append(ahorro)
            lprecio.innerText = 'Nuevo Precio S/ ' + elem.imp_precio
            ndiv.id = elem.cod_producto
            ndiv.append(lprecio, cant,cod_producto)
            div.append(ndiv)
            ndiv.addEventListener('click', () => {
                // alert("se presiono click")
                const cod_p = cod_producto.innerText
                // alert(cod_p)    
                $.ajax({
                    method: 'GET',
                    url: './cnn/sesion.php',
                    data: {
                        'cod_producto':cod_p
                    },
                    dataType: 'json',
                    success: function (data) {
                    if (data.length > 0) {
                        // alert("entro")
                        datos = data
                    } 
                    }
                    
                })
                location.replace("./pageDetalle.php");
                // alert(cod_p)
            })
        })
    } 
}

function ver() {
    alert('nuevos')
}

function ShowProduct() {
    const cod_producto = document.getElementById('cod_producto').value
    const sql="select * from timagen where cod_prod='"+cod_producto+"'"
    const div = document.querySelector('#Imagenes')
    const divs = document.querySelector('#limagen')
    // const p = document.createElement('p')
    // p.innerText = "nuevo"
    // label.innerText="etiqueta nueva"
    let imagenes =new Array()
    aDatos=Async_Data(sql, './cnn/imagen.php');    
    if (aDatos) {
        
        aDatos.forEach(elem => {
            const lprecio = document.createElement('p')
            const imp = document.createElement('p')
            const ahorro = document.createElement('p')
            const cant=document.createElement('p')
            const spacio = document.createElement('p')
            const spacio1 = document.createElement('p')
            const spacio2 = document.createElement('p')
            const cod_producto = document.createElement('label')
            const descuento = document.createElement('div')
            const label = document.createElement('label')
            const img = document.createElement('img')
            const img0 = document.createElement('img')
            const img1 = document.createElement('img')
            const img2 = document.createElement('img')
            const img3 = document.createElement('img')
            // texto
            
            lprecio.style.fontWeight = "bold"
            cant.style.fontWeight = "bold"
            img.src = "data:imagen/png;base64," + elem.imagen
            img0.src = "data:imagen/png;base64," + elem.imagen
            img.style.height = "275px"
            if (elem.imagen1 != null) {
                img1.src = "data:imagen/png;base64," + elem.imagen1
                img1.nodeName="imagen1"
            }
            if (elem.imagen2 != null) {
                img2.src = "data:imagen/png;base64," + elem.imagen2
                img1.nodeName="imagen2"
            }
            if (elem.imagen3 != null) {
                img3.src = "data:imagen/png;base64," + elem.imagen3
                img1.nodeName="imagen3"
            }
            img0.style.height = "80px"
            img1.style.height = "80px"
            img2.style.height = "80px"
            img3.style.height = "80px"
            // divs.append(img1)

            descuento.className = "div-des"
            descuento.append('Ahorra ' + elem.descuento + '%')
            spacio.style.color = "white"
            spacio1.style.color = "white"
            spacio2.style.color="white"
            label.style.color = "black"
            lprecio.style.color = "rgb(124, 7, 170)"
            cant.style.color = "rgb(124, 7, 170)"
            imp.style.color="rgb(124, 7, 170)"
            ahorro.style.color="rgb(124, 7, 170)"
            cod_producto.style.display = "none"
            spacio.innerText = ".............."
            spacio1.innerText = " ............"
            spacio2.innerText = " ............"
            
            
            cod_producto.innerText=elem.cod_producto
            descuento.className = "div-des"
            // Style
            // if (elem.txt_desc.length < 30) {
            //     label.innerText = elem.txt_desc+' ..........'
            // } else {
                label.innerText = (elem.txt_desc+'\n').toLowerCase()
            // }
            cant.innerText = 'Disponible ' + elem.cant
            imp.innerText = 'Antes S/'+elem.imp_descuento
            ahorro.innerText = 'Ahorro de S/'+(elem.imp_descuento-elem.imp_precio)
            lprecio.innerText = 'Nuevo Precio S/ ' + elem.imp_precio
            div.append(label,spacio,img, spacio1, spacio2,cant,lprecio,ahorro,imp)
            divs.append(img0,spacio, img1,spacio1, img2,spacio2, img3)
            img0.addEventListener('click', () => {
                img.style.height = "275px"
                img.src="data:imagen/png;base64," + elem.imagen
            })
            img1.addEventListener('click', () => {
                img.style.height = "275px"
                img.src="data:imagen/png;base64," + elem.imagen1
            })
            img2.addEventListener('click', () => {
                img.style.height = "275px"
                img.src="data:imagen/png;base64," + elem.imagen2
            })
            img3.addEventListener('click', () => {
                img.style.height = "275px"
                img.src="data:imagen/png;base64," + elem.imagen3
            })
          
        })
    } 
}