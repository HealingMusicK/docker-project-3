<html>
    <head>
        <title> 마켓컬리 :: 내일의 장보기, 마켓컬리 (아닙니다) </title>
    </head>

    <body>
        <h1> 마켓컬리(?)에 오신 것을 환영합니다 </h1>
        <ul>
            <?php

            $json = file_get_contents('http://product-info/');
            $obj = json_decode($json);

            $products = $obj->products;

            foreach ($products as $product) {
                echo "<li>$product</li>";
            }

            ?>
        </ul>
    </body>
</html>
