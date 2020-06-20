def get_product(session, url):
    url = url if url is not None else "https://www.yankeecandle.com/product/lemon-lavender/_/_/R-47069/R-47069"
    r = session.get(url)
    r.html.render()
    product_id = url.split("/")[-1]
    product = {
        product_id: {
            "title": r.html.search('<li aria-current="page"><div>{prod_a}</div></li>')['prod_a'].replace("<!-- -->", ""),
            "price": r.html.search("Price </span><span>$<!-- -->{price}</span>")['price'],
            "top_scents": r.html.search("Top:  </strong> {top_scents}<br>")['top_scents'],
            "mid_scents": r.html.search("Mid:  </strong> {mid_scents}<br>")['mid_scents'],
            "base_scents": r.html.search("Base:  </strong> {base_scents}<br>")['base_scents'],
        }
    }
    return product
