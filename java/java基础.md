[TOC]



# day1【前言、入门程序、常量、变量】  #

## hello world ##

```java
/*
需求：定义一个hello world小程序。

思路：
1，
2，

步骤：
1，通过class关键字定义一个类。将代码都编写到该类中。
2，为了保证该的独立运行。在类中定义个主函数。格式public static void main(String[] args)
3,保存成一个扩展名为java的文件。
4，在dos控制台中通过javac工具对java文件进行编译。
5，在通过java命令对生成的class文件进行执行。
*/

class Demo//定义一个累。
{
	//主函数。
	public static void main(String[] args)
	{
		//输出语句。
		System.out.println("hello haha");
	}
}
```



```java

/**
作者:张三
版本：V1.0
这个类是用于演示hello world。
*/
class Demo //这是我的第一个java小程序，//很爽！
{
	/*
	main函数可以保证该的独立运行。
	它是程序的入口。
	它会被JVM所调用。
	*/
	public static void main(String[] args)
	{
		/*
		System.out.println("hello java");//这是输出语句，可以打印小括号中的内容。
		System.out.println("hello world");//？？？？？
		*/
		System.out.println("hello java")
		System.out.println("hello world");
		
		
	}
}
/*
/*床前明月光*/
疑是地上霜
*/
```

## Demo01Const ##

```java
/*
常量：在程序运行期间，固定不变的量。

常量的分类：
1. 字符串常量：凡是用双引号引起来的部分，叫做字符串常量。例如："abc"、"Hello"、"123"
2. 整数常量：直接写上的数字，没有小数点。例如：100、200、0、-250
3. 浮点数常量：直接写上的数字，有小数点。例如：2.5、-3.14、0.0
4. 字符常量：凡是用单引号引起来的单个字符，就做字符常量。例如：'A'、'b'、'9'、'中'
5. 布尔常量：只有量中取值。true、false。
6. 空常量：null。代表没有任何数据。
*/
public class Demo01Const {
	public static void main(String[] args) {
		// 字符串常量
		System.out.println("ABC");
		System.out.println(""); // 字符串两个双引号中间的内容为空
		System.out.println("XYZ");
		
		// 整数常量
		System.out.println(30);
		System.out.println(-500);
		
		// 浮点数常量（小数）
		System.out.println(3.14);
		System.out.println(-2.5);
		
		// 字符常量
		System.out.println('A');
		System.out.println('6');
		// System.out.println(''); // 两个单引号中间必须有且仅有一个字符，没有不行。
		// System.out.println('AB'); // 两个单引号中间必须有且仅有一个字符，有两个不行。
		
		// 布尔常量
		System.out.println(true);
		System.out.println(false);
		
		// 空常量。空常量不能直接用来打印输出。
		// System.out.println(null);
	}
}
```

## Demo02Variable ##

```java
/*
变量：程序运行期间，内容可以发生改变的量。

创建一个变量并且使用的格式：

数据类型 变量名称; // 创建了一个变量
变量名称 = 数据值; // 赋值，将右边的数据值，赋值交给左边的变量

一步到位的格式：

数据类型 变量名称 = 数据值; // 在创建一个变量的同时，立刻放入指定的数据值
*/
public class Demo02Variable {
	public static void main(String[] args) {
		// 创建一个变量
		// 格式：数据类型 变量名称;
		int num1;
		// 向变量当中存入一个数据
		// 格式：变量名称 = 数据值;
		num1 = 10;
		// 当打印输出变量名称的时候，显示出来的是变量的内容
		System.out.println(num1); // 10
		
		// 改变变量当中本来的数字，变成新的数字
		num1 = 20;
		System.out.println(num1); // 20
		
		// 使用一步到位的格式来定义变量
		// 格式：数据类型 变量名称 = 数据值;
		int num2 = 25;
		System.out.println(num2); // 25
		
		num2 = 35;
		System.out.println(num2); // 35
		System.out.println("===============");
		
		byte num3 = 30; // 注意：右侧数值的范围不能超过左侧数据类型的取值范围
		System.out.println(num3); // 30
		
		// byte num4 = 400; // 右侧超出了byte数据范围，错误！
		
		short num5 = 50;
		System.out.println(num5); // 50
		
		long num6 = 3000000000L;
		System.out.println(num6); // 3000000000
		
		float num7 = 2.5F;
		System.out.println(num7); // 2.5
		
		double num8 = 1.2;
		System.out.println(num8); // 1.2
		
		char zifu1 = 'A';
		System.out.println(zifu1); // A
		
		zifu1 = '中';    //char类型可以是一个中国字
		System.out.println(zifu1); // 中
		
		boolean var1 = true;
		System.out.println(var1); // true
		
		var1 = false;
		System.out.println(var1); // false
		
		// 将一个变量的数据内容，赋值交给另一个变量
		// 右侧的变量名称var1已经存在，里面装的是false布尔值
		// 将右侧变量里面的false值，向左交给var2变量进行存储
		boolean var2 = var1;
		System.out.println(var2); // false
	}
}
```

## Demo03VariableNotice ##

```java
/*
使用变量的时候，有一些注意事项：

1. 如果创建多个变量，那么变量之间的名称不可以重复。
2. 对于float和long类型来说，字母后缀F和L不要丢掉。
3. 如果使用byte或者short类型的变量，那么右侧的数据值不能超过左侧类型的范围。
4. 没有进行赋值的变量，不能直接使用；一定要赋值之后，才能使用。
5. 变量使用不能超过作用域的范围。
【作用域】：从定义变量的一行开始，一直到直接所属的大括号结束为止。
6. 可以通过一个语句来创建多个变量，但是一般情况不推荐这么写。
*/
public class Demo03VariableNotice {
	public static void main(String[] args) {
		int num1 = 10; // 创建了一个新的变量，名叫num1
		// int num1 = 20; // 又创建了另一个新的变量，名字也叫num1，错误！
		
		int num2 = 20;
		
		int num3;
		num3 = 30;
		
		int num4; // 定义了一个变量，但是没有进行赋值
		// System.out.println(num4); // 直接使用打印输出就是错误的！
		
		// System.out.println(num5); // 在创建变量之前，不能使用这个变量
		
		int num5 = 500;
		System.out.println(num5); // 500
		
		{
			int num6 = 60;
			System.out.println(num6); // 60
		}
		// int num6;
		// System.out.println(num6); // 已经超出了大括号的范围，超出了作用域，变量不能再使用了
		
		// 同时创建了三个全都是int类型的变量
		int a, b, c;
		// 各自分别赋值
		a = 10;
		b = 20;
		c = 30;
		System.out.println(a); // 10
		System.out.println(b); // 20
		System.out.println(c); // 30
		
		// 同时创建三个int变量，并且同时各自赋值
		int x = 100, y = 200, z = 300;
		System.out.println(x); // 100
		System.out.println(y); // 200
		System.out.println(z); // 300
	}
}
```

# day2【数据类型转换、运算符、方法入门】 #

## Demo01DataType ##

```java
/*
当数据类型不一样时，将会发生数据类型转换。

自动类型转换（隐式）
	1. 特点：代码不需要进行特殊处理，自动完成。
	2. 规则：数据范围从小到大。

强制类型转换（显式）
*/
public class Demo01DataType {
	public static void main(String[] args) {
		System.out.println(1024); // 这就是一个整数，默认就是int类型
		System.out.println(3.14); // 这就是一个浮点数，默认就是double类型
		
		// 左边是long类型，右边是默认的int类型，左右不一样
		// 一个等号代表赋值，将右侧的int常量，交给左侧的long变量进行存储
		// int --> long，符合了数据范围从小到大的要求
		// 这一行代码发生了自动类型转换。
		long num1 = 100;
		System.out.println(num1); // 100
		
		// 左边是double类型，右边是float类型，左右不一样
		// float --> double，符合从小到大的规则
		// 也发生了自动类型转换
		double num2 = 2.5F;
		System.out.println(num2); // 2.5
		
		// 左边是float类型，右边是long类型，左右不一样
		// long --> float，范围是float更大一些，符合从小到大的规则
		// 也发生了自动类型转换
		float num3 = 30L;
		System.out.println(num3); // 30.0
	}
}
```

## Demo02DataType ##

```java
/*
强制类型转换
	1. 特点：代码需要进行特殊的格式处理，不能自动完成。
	2. 格式：范围小的类型 范围小的变量名 = (范围小的类型) 原本范围大的数据;

注意事项：
	1. 强制类型转换一般不推荐使用，因为有可能发生精度损失、数据溢出。
	2. byte/short/char这三种类型都可以发生数学运算，例如加法“+”.
	3. byte/short/char这三种类型在运算的时候，都会被首先提升成为int类型，然后再计算。
	4. boolean类型不能发生数据类型转换
*/
public class Demo02DataType {
	public static void main(String[] args) {
		// 左边是int类型，右边是long类型，不一样
		// long --> int，不是从小到大
		// 不能发生自动类型转换！
		// 格式：范围小的类型 范围小的变量名 = (范围小的类型) 原本范围大的数据;
		int num = (int) 100L;
		System.out.println(num);
		
		// long强制转换成为int类型 数据溢出
		int num2 = (int) 6000000000L;
		System.out.println(num2); // 1705032704
		
		// double --> int，强制类型转换 精度损失
		int num3 = (int) 3.99;
		System.out.println(num3); // 3，这并不是四舍五入，所有的小数位都会被舍弃掉
		
		char zifu1 = 'A'; // 这是一个字符型变量，里面是大写字母A
		System.out.println(zifu1 + 1); // 66，也就是大写字母A被当做65进行处理
		// 计算机的底层会用一个数字（二进制）来代表字符A，就是65
		// 一旦char类型进行了数学运算，那么字符就会按照一定的规则翻译成为一个数字
		
		byte num4 = 40; // 注意！右侧的数值大小不能超过左侧的类型范围
		byte num5 = 50;
		// byte + byte --> int + int --> int
		int result1 = num4 + num5;
		System.out.println(result1); // 90
		
		short num6 = 60;
		// byte + short --> int + int --> int
		// int强制转换为short：注意必须保证逻辑上真实大小本来就没有超过short范围，否则会发生数据溢出
		short result2 = (short) (num4 + num6);
		System.out.println(result2); // 100
	}
}
```

## Demo03DataTypeChar ##

```java
/*
数字和字符的对照关系表（编码表）：

ASCII码表：American Standard Code for Information Interchange，美国信息交换标准代码。
Unicode码表：万国码。也是数字和符号的对照关系，开头0-127部分和ASCII完全一样，但是从128开始包含有更多字符。

48 - '0'
65 - 'A'
97 - 'a'
*/
public class Demo03DataTypeChar {
	public static void main(String[] args) {
		char zifu1 = '1';
		System.out.println(zifu1 + 0); // 49
		
		char zifu2 = 'A'; // 其实底层保存的是65数字
		
		char zifu3 = 'c';
		// 左侧是int类型，右边是char类型，
		// char --> int，确实是从小到大
		// 发生了自动类型转换
		int num = zifu3;
		System.out.println(num); // 99
		
		char zifu4 = '中'; // 正确写法
		System.out.println(zifu4 + 0); // 20013
	}
}
```

## Demo04Operator ##

```java
/*
运算符：进行特定操作的符号。例如：+
表达式：用运算符连起来的式子叫做表达式。例如：20 + 5。又例如：a + b

四则运算：
加：+
减：-
乘：*
除：/

取模（取余数）：%

首先计算得到表达式的结果，然后再打印输出这个结果。
复习一下小学一年级的除法公式：
被除数 / 除数 = 商 ... 余数

对于一个整数的表达式来说，除法用的是整除，整数除以整数，结果仍然是整数。只看商，不看余数。
只有对于整数的除法来说，取模运算符才有余数的意义。

注意事项：
	1. 一旦运算当中有不同类型的数据，那么结果将会是数据类型范围大的那种。
*/
public class Demo04Operator {
	public static void main(String[] args) {
		// 两个常量之间可以进行数学运算
		System.out.println(20 + 30);
		
		// 两个变量之间也可以进行数学运算
		int a = 20;
		int b = 30;
		System.out.println(a - b); // -10
		
		// 变量和常量之间可以混合使用
		System.out.println(a * 10); // 200
		
		int x = 10;
		int y = 3;
		
		int result1 = x / y;
		System.out.println(result1); // 3
		
		int result2 = x % y;
		System.out.println(result2); // 余数，模，1
		
		// int + double --> double + double --> double
		double result3 = x + 2.5;
		System.out.println(result3); // 12.5
	}
}
```

## Demo05Plus ##

```java
/*
四则运算当中的加号“+”有常见的三种用法：

1. 对于数值来说，那就是加法。
2. 对于字符char类型来说，在计算之前，char会被提升成为int，然后再计算。
char类型字符，和int类型数字，之间的对照关系表：ASCII、Unicode
3. 对于字符串String（首字母大写，并不是关键字）来说，加号代表字符串连接操作。
任何数据类型和字符串进行连接的时候，结果都会变成字符串
*/
public class Demo05Plus {
	public static void main(String[] args) {
		// 字符串类型的变量基本使用
		// 数据类型 变量名称 = 数据值;
		String str1 = "Hello";
		System.out.println(str1); // Hello
		
		System.out.println("Hello" + "World"); // HelloWorld
		
		String str2 = "Java";
		// String + int --> String
		System.out.println(str2 + 20); // Java20
		
		// 优先级问题
		// String + int + int
		// String		+ int
		// String
		System.out.println(str2 + 20 + 30); // Java2030
		
		System.out.println(str2 + (20 + 30)); // Java50
	}
}
```

## Demo06Operator ##

```java
/*
自增运算符：++
自减运算符：--

基本含义：让一个变量涨一个数字1，或者让一个变量降一个数字1
使用格式：写在变量名称之前，或者写在变量名称之后。例如：++num，也可以num++
使用方式：
	1. 单独使用：不和其他任何操作混合，自己独立成为一个步骤。
	2. 混合使用：和其他操作混合，例如与赋值混合，或者与打印操作混合，等。
使用区别：
	1. 在单独使用的时候，前++和后++没有任何区别。也就是：++num;和num++;是完全一样的。
	2. 在混合的时候，有【重大区别】
		A. 如果是【前++】，那么变量【立刻马上+1】，然后拿着结果进行使用。	【先加后用】
		B. 如果是【后++】，那么首先使用变量本来的数值，【然后再让变量+1】。	【先用后加】
		
注意事项：
	只有变量才能使用自增、自减运算符。常量不可发生改变，所以不能用。
*/
public class Demo06Operator {
	public static void main(String[] args) {
		int num1 = 10;
		System.out.println(num1); // 10
		++num1; // 单独使用，前++
		System.out.println(num1); // 11
		num1++; // 单独使用，后++
		System.out.println(num1); // 12
		System.out.println("=================");
		
		// 与打印操作混合的时候
		int num2 = 20;
		// 混合使用，先++，变量立刻马上变成21，然后打印结果21
		System.out.println(++num2); // 21
		System.out.println(num2); // 21
		System.out.println("=================");
		
		int num3 = 30;
		// 混合使用，后++，首先使用变量本来的30，然后再让变量+1得到31
		System.out.println(num3++); // 30
		System.out.println(num3); // 31
		System.out.println("=================");
		
		int num4 = 40;
		// 和赋值操作混合
		int result1 = --num4; // 混合使用，前--，变量立刻马上-1变成39，然后将结果39交给result1变量
		System.out.println(result1); // 39
		System.out.println(num4); // 39
		System.out.println("=================");
		
		int num5 = 50;
		// 混合使用，后--，首先把本来的数字50交给result2，然后我自己再-1变成49
		int result2 = num5--;
		System.out.println(result2); // 50
		System.out.println(num5); // 49
		System.out.println("=================");
		
		int x = 10;
		int y = 20;
		// 11 + 20 = 31
		int result3 = ++x + y--;
		System.out.println(result3); // 31
		System.out.println(x); // 11
		System.out.println(y); // 19
		
		// 30++; // 错误写法！常量不可以使用++或者--
	}
}
```

## Demo07Operator ##

```java
/*
赋值运算符分为：

基本赋值运算符：就是一个等号“=”，代表将右侧的数据交给左侧的变量。
	int a = 30;

复合赋值运算符：
	+=		a += 3		相当于		a = a + 3
	-=		b -= 4		相当于		b = b - 4
	*=		c *= 5		相当于		c = c * 5
	/=		d /= 6		相当于		d = d / 6
	%=		e %= 7		相当于		e = e % 7

注意事项：
	1. 只有变量才能使用赋值运算符，常量不能进行赋值。
	2. 复合赋值运算符其中隐含了一个强制类型转换。
*/
public class Demo07Operator {
	public static void main(String[] args) {
		int a = 10;
		// 按照公式进行翻译：a = a + 5
		// a = 10 + 5;
		// a = 15;
		// a本来是10，现在重新赋值得到15
		a += 5; 
		System.out.println(a); // 15
		
		int x = 10;
		// x = x % 3;
		// x = 10 % 3;
		// x = 1;
		// x本来是10，现在重新赋值得到1
		x %= 3;
		System.out.println(x); // 1
		
		// 50 = 30; // 常量不能进行赋值，不能写在赋值运算符的左边。错误写法！
		
		byte num = 30;
		// num = num + 5;
		// num = byte + int
		// num = int + int
		// num = int
		// num = (byte) int
		num += 5;
		System.out.println(num); // 35
	}
}
```

## Demo08Operator ##

```java
/*
比较运算符：
大于：		>
小于：		<
大于等于：	>=
小于等于：	<=
相等：		==	【两个等号连写才是相等，一个等号代表的是赋值】
不相等：	!=

注意事项：
1. 比较运算符的结果一定是一个boolean值，成立就是true，不成立就是false
2. 如果进行多次判断，不能连着写。
数学当中的写法，例如：1 < x < 3
程序当中【不允许】这种写法。
*/
public class Demo08Operator {
	public static void main(String[] args) {
		System.out.println(10 > 5); // true
		int num1 = 10;
		int num2 = 12;
		System.out.println(num1 < num2); // true
		System.out.println(num2 >= 100); // false
		System.out.println(num2 <= 100); // true
		System.out.println(num2 <= 12); // true
		System.out.println("===============");
		
		System.out.println(10 == 10); // true
		System.out.println(20 != 25); // true
		System.out.println(20 != 20); // false
		
		int x = 2;
		// System.out.println(1 < x < 3); // 错误写法！编译报错！不能连着写。
	}
}
```

## Demo09Logic ##

```java
/*
与（并且）	&&	全都是true，才是true；否则就是false
或（或者）	||	至少一个是true，就是true；全都是false，才是false
非（取反）	!	本来是true，变成false；本来是false，变成true

与“&&”，或“||”，具有短路效果：如果根据左边已经可以判断得到最终结果，那么右边的代码将不再执行，从而节省一定的性能。

注意事项：
1. 逻辑运算符只能用于boolean值。
2. 与、或需要左右各自有一个boolean值，但是取反只要有唯一的一个boolean值即可。
3. 与、或两种运算符，如果有多个条件，可以连续写。
两个条件：条件A && 条件B
多个条件：条件A && 条件B && 条件C

TIPS：
对于1 < x < 3的情况，应该拆成两个部分，然后使用与运算符连接起来：
int x = 2;
1 < x && x < 3
*/
public class Demo09Logic {
	public static void main(String[] args) {
		System.out.println(true && false); // false
		// true && true --> true
		System.out.println(3 < 4 && 10 > 5); // true
		System.out.println("============");
		
		System.out.println(true || false); // true
		System.out.println(true || true); // true
		System.out.println(false || false); // false
		System.out.println("============");
		
		System.out.println(true); // true
		System.out.println(!true); // false	
		System.out.println("============");
		
		int a = 10;
		// false && ... 短路操作
		System.out.println(3 > 4 && ++a < 100); // false
		System.out.println(a); // 10
		System.out.println("============");
		
		int b = 20;
		// true || ...
		System.out.println(3 < 4 || ++b < 100); // true
		System.out.println(b); // 20
	}
}
```

## Demo10Operator运算符 ##

```java
/*
一元运算符：只需要一个数据就可以进行操作的运算符。例如：取反!、自增++、自减--
二元运算符：需要两个数据才可以进行操作的运算符。例如：加法+、赋值=
三元运算符：需要三个数据才可以进行操作的运算符。

格式：
数据类型 变量名称 = 条件判断 ? 表达式A : 表达式B;

流程：
首先判断条件是否成立：
	如果成立为true，那么将表达式A的值赋值给左侧的变量；
	如果不成立为false，那么将表达式B的值赋值给左侧的变量；
二者选其一。

注意事项：
1. 必须同时保证表达式A和表达式B都符合左侧数据类型的要求。
2. 三元运算符的结果必须被使用。
*/
public class Demo10Operator {
	public static void main(String[] args) {
		int a = 10;
		int b = 20;
		
		// 数据类型 变量名称 = 条件判断 ? 表达式A : 表达式B;
		// 判断a > b是否成立，如果成立将a的值赋值给max；如果不成立将b的值赋值给max。二者选其一
		int max = a > b ? a : b; // 最大值的变量
		System.out.println("最大值：" + max); // 20
		
		// int result = 3 > 4 ? 2.5 : 10; // 错误写法！
		
		System.out.println(a > b ? a : b); // 正确写法！
		
		// a > b ? a : b; // 错误写法！
	}
}
```

## Demo11Method ##

```java
/*
定义一个方法的格式：
public static void 方法名称() {
	方法体
}

方法名称的命名规则和变量一样，使用小驼峰。
方法体：也就是大括号当中可以包含任意条语句。

注意事项：
1. 方法定义的先后顺序无所谓。
2. 方法的定义不能产生嵌套包含关系。
3. 方法定义好了之后，不会执行的。如果要想执行，一定要进行方法的【调用】。

如何调用方法，格式：

方法名称();
*/
public class Demo11Method {
	
	public static void main(String[] args) {
		farmer(); // 调用农民的方法
		seller(); // 调用小商贩的方法
		cook(); // 调用厨子的方法
		me(); // 调用我自己的方法
	}
	
	// 厨子
	public static void cook() {
		System.out.println("洗菜");
		System.out.println("切菜");
		System.out.println("炒菜");
		System.out.println("装盘");
	}
	
	// 我
	public static void me() {
		System.out.println("吃");
	}
	
	// 小商贩
	public static void seller() {
		System.out.println("运输到农贸市场");
		System.out.println("抬高价格");
		System.out.println("吆喝");
		System.out.println("卖给厨子");
	}
	
	// 农民伯伯
	public static void farmer() {
		System.out.println("播种");
		System.out.println("浇水");
		System.out.println("施肥");
		System.out.println("除虫");
		System.out.println("收割");
		System.out.println("卖给小商贩");
	}
}
```

## Demo12Notice隐含补强转 ##

```java
/*
对于byte/short/char三种类型来说，如果右侧赋值的数值没有超过范围，
那么javac编译器将会自动隐含地为我们补上一个(byte)(short)(char)。

1. 如果没有超过左侧的范围，编译器补上强转。
2. 如果右侧超过了左侧范围，那么直接编译器报错。
*/
public class Demo12Notice {
	public static void main(String[] args) {
		// 右侧确实是一个int数字，但是没有超过左侧的范围，就是正确的。
		// int --> byte，不是自动类型转换
		byte num1 = /*(byte)*/ 30; // 右侧没有超过左侧的范围
		System.out.println(num1); // 30
		
		// byte num2 = 128; // 右侧超过了左侧的范围
		
		// int --> char，没有超过范围
		// 编译器将会自动补上一个隐含的(char)
		char zifu = /*(char)*/ 65;
		System.out.println(zifu); // A
	}
}
```

## Demo13Notice编译器的常量优化 ##

```java
/*
在给变量进行赋值的时候，如果右侧的表达式当中全都是常量，没有任何变量，
那么编译器javac将会直接将若干个常量表达式计算得到结果。
short result = 5 + 8; // 等号右边全都是常量，没有任何变量参与运算
编译之后，得到的.class字节码文件当中相当于【直接就是】：
short result = 13;
右侧的常量结果数值，没有超过左侧范围，所以正确。

这称为“编译器的常量优化”。

但是注意：一旦表达式当中有变量参与，那么就不能进行这种优化了。
*/
public class Demo13Notice {
	public static void main(String[] args) {
		short num1 = 10; // 正确写法，右侧没有超过左侧的范围，
		
		short a = 5;
		short b = 8;
		// short + short --> int + int --> int
		// short result = a + b; // 错误写法！左侧需要是int类型
		
		// 右侧不用变量，而是采用常量，而且只有两个常量，没有别人
		short result = 5 + 8;
		System.out.println(result);
		
		//short result2 = 5 + a + 8; // 一旦表达式当中有变量参与，那么就不能进行这种优化了。
	}
}
```

# day3【 流程控制语句】 #

## Demo01Sequence ##

```java
// 顺序结构
public class Demo01Sequence {
	public static void main(String[] args) {
		System.out.println("今天天气不错");
		System.out.println("挺风和日丽的");
		System.out.println("我们下午没课");
		System.out.println("这的确挺爽的");
	}
}
```

## Demo02If ##

```java
// 单if语句
public class Demo02If {
	public static void main(String[] args) {
		System.out.println("今天天气不错，正在压马路……突然发现一个快乐的地方：网吧");
		int age = 19;
		if (age >= 18) {
			System.out.println("进入网吧，开始high！");
			System.out.println("遇到了一群猪队友，开始骂街。");
			System.out.println("感觉不爽，结账走人。");
		}
		System.out.println("回家吃饭");
	}
}
```

## Demo03IfElse ##

```java
// 标准的if-else语句
public class Demo03IfElse {
	public static void main(String[] args) {
		int num = 666;
		
		if (num % 2 == 0) { // 如果除以2能够余数为0，说明是偶数
			System.out.println("偶数");
		} else {
			System.out.println("奇数");
		}
	}
}
```

Demo04IfElseExt

```java
// x和y的关系满足如下：
// 如果x >= 3，那么y = 2x + 1;
// 如果-1 < x < 3，那么y = 2x;
// 如果x <= -1，那么y = 2x – 1;
public class Demo04IfElseExt {
	public static void main(String[] args) {
		int x = -10;
		int y;
		if (x >= 3) {
			y = 2 * x + 1;
		} else if (-1 < x && x < 3) {
			y = 2 * x;
		} else {
			y = 2 * x - 1;
		}
		System.out.println("结果是：" + y);
	}
}
```

## Demo05IfElsePractise ##

```java
public class Demo05IfElsePractise {
	public static void main(String[] args) {
		int score = 120;
		if (score >= 90 && score <= 100) {
			System.out.println("优秀");
		} else if (score >= 80 && score < 90) {
			System.out.println("好");
		} else if (score >= 70 && score < 80) {
			System.out.println("良");
		} else if (score >= 60 && score < 70) {
			System.out.println("及格");
		} else if (score >= 0 && score < 60) {
			System.out.println("不及格");
		} else { // 单独处理边界之外的不合理情况
			System.out.println("数据错误");
		}
	}
}
```

## Demo06Max ##

```java
// 题目：使用三元运算符和标准的if-else语句分别实现：取两个数字当中的最大值
public class Demo06Max {
	public static void main(String[] args) {
		int a = 105;
		int b = 20;
		
		// 首先使用三元运算符
		// int max = a > b ? a : b;
		
		// 使用今天的if语句
		int max;
		if (a > b) {
			max = a;
		} else {
			max = b;
		}
		
		System.out.println("最大值：" + max);
	}
}
```

## Demo07Switch ##

```java
public class Demo07Switch {
	public static void main(String[] args) {
		int num = 10;
		
		switch (num) {
			case 1:
				System.out.println("星期一");
				break;
			case 2:
				System.out.println("星期二");
				break;
			case 3:
				System.out.println("星期三");
				break;
			case 4:
				System.out.println("星期四");
				break;
			case 5:
				System.out.println("星期五");
				break;
			case 6:
				System.out.println("星期六");
				break;
			case 7:
				System.out.println("星期日");
				break;
			default:
				System.out.println("数据不合理");
				break; // 最后一个break语句可以省略，但是强烈推荐不要省略
		}
	}
}
```

## Demo08SwitchNotice ##

```java
/*
switch语句使用的注意事项：

1. 多个case后面的数值不可以重复。

2. switch后面小括号当中只能是下列数据类型：
基本数据类型：byte/short/char/int
引用数据类型：String字符串、enum枚举

3. switch语句格式可以很灵活：前后顺序可以颠倒，而且break语句还可以省略。
“匹配哪一个case就从哪一个位置向下执行，直到遇到了break或者整体结束为止。”
*/
public class Demo08SwitchNotice {
	public static void main(String[] args) {
		int num = 2;
		switch (num) {
			case 1:
				System.out.println("你好");
				break;
			case 2:
				System.out.println("我好");
				// break;
			case 3:
				System.out.println("大家好");
				break;
			default:
				System.out.println("他好，我也好。");
				break;
		} // switch
	}
}
```

## Demo09For ##

```java
/*
循环结构的基本组成部分，一般可以分成四部分：

1. 初始化语句：在循环开始最初执行，而且只做唯一一次。
2. 条件判断：如果成立，则循环继续；如果不成立，则循环退出。
3. 循环体：重复要做的事情内容，若干行语句。
4. 步进语句：每次循环之后都要进行的扫尾工作，每次循环结束之后都要执行一次。
*/
public class Demo09For {
	public static void main(String[] args) {
		for (int i = 1; i <= 100; i++) {
			System.out.println("我错啦！原谅我吧！" + i);
		}
		System.out.println("程序停止");
	}
}
```

## Demo10While ##

```java
/*
while循环有一个标准格式，还有一个扩展格式。

标准格式：
while (条件判断) {
	循环体
}

扩展格式：

初始化语句;
while (条件判断) {
	循环体;
	步进语句;
}
*/
public class Demo10While {
	public static void main(String[] args) {
		for (int i = 1; i <= 10; i++) {
			System.out.println("我错啦！" + i);
		}
		System.out.println("=================");
		
		int i = 1; // 1. 初始化语句
		while (i <= 10) { // 2. 条件判断
			System.out.println("我错啦！" + i); // 3. 循环体
			i++; // 4. 步进语句
		}
	}
}
```

## Demo11DoWhile ##

```java
/*
do-while循环的标准格式：

do {
	循环体
} while (条件判断);

扩展格式：

初始化语句
do {
	循环体
	步进语句
} while (条件判断);
*/
public class Demo11DoWhile {
	public static void main(String[] args) {
		for (int i = 1; i <= 10; i++) {
			System.out.println("原谅你啦！起来吧！地上怪凉！" + i);
		}
		System.out.println("===============");
		
		int i = 1; // 1. 初始化语句
		do {
			System.out.println("原谅你啦！起来吧！地上怪凉！" + i); // 3. 循环体
			i++; // 4. 步进语句
		} while (i <= 10); // 2. 条件判断
	}
}
```

##  Demo12HundredSum

```java
/*
题目：求出1-100之间的偶数和。

思路：
1. 既然范围已经确定了是1到100之间，那么我就从1、2、3……一直到100这么多数字一个一个进行检查。
2. 总共有100个数字，并非所有数字都能用。必须要是偶数才能用，判断（if语句）偶数：num % 2 == 0
3. 需要一个变量，用来进行累加操作。也就好比是一个存钱罐。
*/
public class Demo12HundredSum {
	public static void main(String[] args) {
		int sum = 0; // 用来累加的存钱罐
		
		for (int i = 1; i <= 100; i++) {
			if (i % 2 == 0) { // 如果是偶数
				sum += i;
			}
		}
		System.out.println("结果是：" + sum);
	}
}
```

## Demo13LoopDifference ##

```java
/*
三种循环的区别。

1. 如果条件判断从来没有满足过，那么for循环和while循环将会执行0次，但是do-while循环会执行至少一次。
2. for循环的变量在小括号当中定义，只有循环内部才可以使用。while循环和do-while循环初始化语句本来就在外面，所以出来循环之后还可以继续使用。
*/
public class Demo13LoopDifference {
	public static void main(String[] args) {
		for (int i = 1; i < 0; i++) {
			System.out.println("Hello");
		}
		// System.out.println(i); // 这一行是错误写法！因为变量i定义在for循环小括号内，只有for循环自己才能用。
		System.out.println("================");
		
		int i = 1;
		do {
			System.out.println("World");
			i++;
		} while (i < 0);
		// 现在已经超出了do-while循环的范围，我们仍然可以使用变量i
		System.out.println(i); // 2
	}
}
```

## Demo14Break ##

```java
/*
break关键字的用法有常见的两种：

1. 可以用在switch语句当中，一旦执行，整个switch语句立刻结束。
2. 还可以用在循环语句当中，一旦执行，整个循环语句立刻结束。打断循环。

关于循环的选择，有一个小建议：
凡是次数确定的场景多用for循环；否则多用while循环。
*/
public class Demo14Break {
	public static void main(String[] args) {
		for (int i = 1; i <= 10; i++) {
			// 如果希望从第4次开始，后续全都不要了，就要打断循环
			if (i == 4) { // 如果当前是第4次
				break; // 那么就打断整个循环
			}
			System.out.println("Hello" + i);
		}
	}
}
```

## Demo15Continue ##

```java
/*
另一种循环控制语句是continue关键字。
一旦执行，立刻跳过当前次循环剩余内容，马上开始下一次循环。
*/
public class Demo15Continue {
	public static void main(String[] args) {
		for (int i = 1; i <= 10; i++) {
			if (i == 4) { // 如果当前是第4层
				continue; // 那么跳过当前次循环，马上开始下一次（第5层）
			}
			System.out.println(i + "层到了。");
		}
	}
}
```

## Demo16DeadLoop ##

```java
/*
永远停不下来的循环，叫做死循环。

死循环的标准格式：
while (true) {
	循环体
}
*/
public class Demo16DeadLoop {
	public static void main(String[] args) {
		while (true) {
			System.out.println("I Love Java!");
		}
		
		// System.out.println("Hello");
	}
}
```

## Demo17LoopHourAndMinute ##

```java
public class Demo17LoopHourAndMinute {
	public static void main(String[] args) {
		for (int hour = 0; hour < 24; hour++) { // 外层控制小时

			for (int minute = 0; minute < 60; minute++) { // 内层控制小时之内的分钟
				System.out.println(hour + "点" + minute + "分");
			}

		}
	}
}
```

# day4【Intellij IDEA】 #

## Demo01Method ##

```java
package cn.itcast.day04.demo02;

/*
复习一下此前学习的方法基础入门知识。

定义格式：
public static void 方法名称() {
    方法体
}

调用格式：
方法名称();

注意事项：
1. 方法定义的先后顺序无所谓。
2. 方法定义必须是挨着的，不能在一个方法的内部定义另外一个方法。
3. 方法定义之后，自己不会执行的；如果希望执行，一定要进行方法的调用。
 */
public class Demo01Method {

    public static void main(String[] args) {
        printMethod();
    }

    public static void printMethod() {
        for (int j = 0; j < 5; j++) {
            for (int i = 0; i < 20; i++) {
                System.out.print("*");
            }      // 5.fori
            System.out.println();
        }
    }

}
```

## Demo02MethodDefine ##

```java
package cn.itcast.day04.demo02;

/*
方法其实就是若干语句的功能集合。

方法好比是一个工厂。
蒙牛工厂     原料：奶牛、饲料、水
            产出物：奶制品
钢铁工厂     原料：铁矿石、煤炭
            产出物：钢铁建材

参数（原料）：就是进入方法的数据。
返回值（产出物）：就是从方法中出来的数据。

定义方法的完整格式：
修饰符 返回值类型 方法名称(参数类型 参数名称, ...) {
    方法体
    return 返回值;
}

修饰符：现阶段的固定写法，public static
返回值类型：也就是方法最终产生的数据结果是什么类型
方法名称：方法的名字，规则和变量一样，小驼峰
参数类型：进入方法的数据是什么类型
参数名称：进入方法的数据对应的变量名称
PS：参数如果有多个，使用逗号进行分隔
方法体：方法需要做的事情，若干行代码
return：两个作用，第一停止当前方法，第二将后面的返回值还给调用处
返回值：也就是方法执行后最终产生的数据结果

注意：return后面的“返回值”，必须和方法名称前面的“返回值类型”，保持对应。

定义一个两个int数字相加的方法。三要素：
返回值类型：int
方法名称：sum
参数列表：int a, int b

方法的三种调用格式。
1. 单独调用：方法名称(参数);
2. 打印调用：System.out.println(方法名称(参数));
3. 赋值调用：数据类型 变量名称 = 方法名称(参数);

注意：此前学习的方法，返回值类型固定写为void，这种方法只能够单独调用，不能进行打印调用或者赋值调用。
*/
public class Demo02MethodDefine {

    public static void main(String[] args) {
        // 单独调用
        sum(10, 20);
        System.out.println("===========");

        // 打印调用
        System.out.println(sum(10, 20)); // 30
        System.out.println("===========");

        // 赋值调用
        int number = sum(15, 25);
        number += 100;
        System.out.println("变量的值：" + number); // 140
    }

    public static int sum(int a, int b) {
        System.out.println("方法执行啦！");
        int result = a + b;
        return result;
    }

}

```

## Demo03MethodParam ##

```java
package cn.itcast.day04.demo02;

/*
有参数：小括号当中有内容，当一个方法需要一些数据条件，才能完成任务的时候，就是有参数。
例如两个数字相加，必须知道两个数字是各自多少，才能相加。

无参数：小括号当中留空。一个方法不需要任何数据条件，自己就能独立完成任务，就是无参数。
例如定义一个方法，打印固定10次HelloWorld。
 */
public class Demo03MethodParam {

    public static void main(String[] args) {
        method1(10, 20);
        System.out.println("==============");
        method2();
    }

    // 两个数字相乘，做乘法，必须知道两个数字各自是多少，否则无法进行计算
    // 有参数
    public static void method1(int a, int b) {
        int result = a * b;
        System.out.println("结果是：" + result);
    }

    // 例如打印输出固定10次文本字符串
    public static void method2() {
        for (int i = 0; i < 10; i++) {
            System.out.println("Hello, World!" + i);
        }
    }

}
```

## Demo04MethodReturn ##

```java
package cn.itcast.day04.demo02;

/*
题目要求：定义一个方法，用来【求出】两个数字之和。（你帮我算，算完之后把结果告诉我。）
题目变形：定义一个方法，用来【打印】两个数字之和。（你来计算，算完之后你自己负责显示结果，不用告诉我。）

注意事项：
对于有返回值的方法，可以使用单独调用、打印调用或者赋值调用。
但是对于无返回值的方法，只能使用单独调用，不能使用打印调用或者赋值调用。
 */
public class Demo04MethodReturn {

    public static void main(String[] args) {
        // 我是main方法，我来调用你。
        // 我调用你，你来帮我计算一下，算完了之后，把结果告诉我的num变量
        int num = getSum(10, 20);
        System.out.println("返回值是：" + num);
        System.out.println("==============");

        printSum(100, 200);
        System.out.println("==============");

        System.out.println(getSum(2, 3)); // 正确写法
        getSum(3, 5); // 正确写法，但是返回值没有用到
        System.out.println("==============");

        // 对于void没有返回值的方法，只能单独，不能打印或者赋值
//        System.out.println(printSum(2, 3)); // 错误写法！
//        System.out.println(void);

//        int num2 = printSum(10, 20); // 错误写法！
//        int num3 = void;
//        void num4 = void;
    }

    // 我是一个方法，我负责两个数字相加。
    // 我有返回值int，谁调用我，我就把计算结果告诉谁
    public static int getSum(int a, int b) {
        int result = a + b;
        return result;
    }

    // 我是一个方法，我负责两个数字相加。
    // 我没有返回值，不会把结果告诉任何人，而是我自己进行打印输出。
    public static void printSum(int a, int b) {
        int result = a + b;
        System.out.println("结果是：" + result);
    }

}
```



## Demo01MethodSame ##

```java
package cn.itcast.day04.demo03;

/*
题目要求：
定义一个方法，用来判断两个数字是否相同。
 */
public class Demo01MethodSame {

    public static void main(String[] args) {
        System.out.println(isSame(10, 20)); // false
        System.out.println(isSame(20, 20)); // true
    }

    /*
    三要素：
    返回值类型：boolean
    方法名称：isSame
    参数列表：int a, int b
     */
    public static boolean isSame(int a, int b) {
        /*boolean same;
        if (a == b) {
            same = true;
        } else {
            same = false;
        }*/

        // boolean same = a == b ? true : false;

        // boolean same = a == b;

        return a == b;
    }

}

```

## Demo02MethodSum ##

```java
package cn.itcast.day04.demo03;

/*
题目要求：
定义一个方法，用来求出1-100之间所有数字的和值。
 */
public class Demo02MethodSum {

    public static void main(String[] args) {
        System.out.println("结果是：" + getSum());
    }

    /*
    三要素
    返回值：有返回值，计算结果是一个int数字
    方法名称：getSum
    参数列表：数据范围已经确定，是固定的，所以不需要告诉我任何条件，不需要参数
     */
    public static int getSum() {
        int sum = 0;
        for (int i = 1; i <= 100; i++) {
            sum += i;
        }
        return sum;
    }

}
```

## Demo03MethodPrint ##

```java
package cn.itcast.day04.demo03;

/*
题目要求：
定义一个方法，用来打印指定次数的HelloWorld。
 */
public class Demo03MethodPrint {

    public static void main(String[] args) {
        printCount(10);
    }

    /*
    三要素
    返回值类型：只是进行一大堆打印操作而已，没有计算，也没有结果要告诉调用处
    方法名称：printCount
    参数列表：到底要打印多少次？必须告诉我，否则我不知道多少次，没法打印。次数：int
     */
    public static void printCount(int num) {
        for (int i = 0; i < num; i++) {
            System.out.println("Hello, World!" + (i + 1));
        }//num.fori
    }

}
```

## Demo04MethodNotice ##

```java
package cn.itcast.day04.demo03;

/*
使用方法的时候，注意事项：

1. 方法应该定义在类当中，但是不能在方法当中再定义方法。不能嵌套。
2. 方法定义的前后顺序无所谓。
3. 方法定义之后不会执行，如果希望执行，一定要调用：单独调用、打印调用、赋值调用。
4. 如果方法有返回值，那么必须写上“return 返回值;”，不能没有。
5. return后面的返回值数据，必须和方法的返回值类型，对应起来。
6. 对于一个void没有返回值的方法，不能写return后面的返回值，只能写return自己。
7. 对于void方法当中最后一行的return可以省略不写。
8. 一个方法当中可以有多个return语句，但是必须保证同时只有一个会被执行到，两个return不能连写。
 */
public class Demo04MethodNotice {

    public static int method1() {
        return 10;
    }

    public static void method2() {
//        return 10; // 错误的写法！方法没有返回值，return后面就不能写返回值。
        return; // 没有返回值，只是结束方法的执行而已。
    }

    public static void method3() {
        System.out.println("AAA");
        System.out.println("BBB");
//        return; // 最后一行的return可以省略不写。
    }

    public static int getMax(int a, int b) {
        /*int max;
        if (a > b) {
            max = a;
        } else {
            max = b;
        }
        return max;*/

        if (a > b) {
            return a;
        } else {
            return b;
        }
    }

}
```

## Demo01MethodOverload ##

```java
package cn.itcast.day04.demo04;

/*
对于功能类似的方法来说，因为参数列表不一样，却需要记住那么多不同的方法名称，太麻烦。

方法的重载（Overload）：多个方法的名称一样，但是参数列表不一样。
好处：只需要记住唯一一个方法名称，就可以实现类似的多个功能。

方法重载与下列因素相关：
1. 参数个数不同
2. 参数类型不同
3. 参数的多类型顺序不同

方法重载与下列因素无关：
1. 与参数的名称无关
2. 与方法的返回值类型无关
 */
public class Demo01MethodOverload {

    public static void main(String[] args) {
        /*System.out.println(sumTwo(10, 20)); // 30
        System.out.println(sumThree(10, 20, 30)); // 60
        System.out.println(sumFour(10, 20, 30, 40)); // 100*/

        System.out.println(sum(10, 20)); // 两个参数的方法
        System.out.println(sum(10, 20, 30)); // 三个参数的方法
        System.out.println(sum(10, 20, 30, 40)); // 四个参数的方法
//        System.out.println(sum(10, 20, 30, 40, 50)); // 找不到任何方法来匹配，所以错误！

        sum(10, 20);
    }

    public static int sum(int a, double b) {
        return (int) (a + b);
    }

    public static int sum(double a, int b) {
        return (int) (a + b);
    }

    public static int sum(int a, int b) {
        System.out.println("有2个参数的方法执行！");
        return a + b;
    }

    // 错误写法！与方法的返回值类型无关
//    public static double sum(int a, int b) {
//        return a + b + 0.0;
//    }

    // 错误写法！与参数的名称无关
//    public static int sum(int x, int y) {
//        return x + y;
//    }

    public static int sum(double a, double b) {
        return (int) (a + b);
    }

    public static int sum(int a, int b, int c) {
        System.out.println("有3个参数的方法执行！");
        return a + b + c;
    }

    public static int sum(int a, int b, int c, int d) {
        System.out.println("有4个参数的方法执行！");
        return a + b + c + d;
    }

}
```



## Demo02MethodOverloadSame ##

```java
package cn.itcast.day04.demo04;

/*
题目要求：
比较两个数据是否相等。
参数类型分别为两个byte类型，两个short类型，两个int类型，两个long类型，
并在main方法中进行测试。
 */
public class Demo02MethodOverloadSame {

    public static void main(String[] args) {
        byte a = 10;
        byte b = 20;
        System.out.println(isSame(a, b));

        System.out.println(isSame((short) 20, (short) 20));

        System.out.println(isSame(11, 12));

        System.out.println(isSame(10L, 10L));
    }

    public static boolean isSame(byte a, byte b) {
        System.out.println("两个byte参数的方法执行！");
        boolean same;
        if (a == b) {
            same = true;
        } else {
            same = false;
        }
        return same;
    }

    public static boolean isSame(short a, short b) {
        System.out.println("两个short参数的方法执行！");
        boolean same = a == b ? true : false;
        return same;
    }

    public static boolean isSame(int a, int b) {
        System.out.println("两个int参数的方法执行！");
        return a == b;
    }

    public static boolean isSame(long a, long b) {
        System.out.println("两个long参数的方法执行！");
        if (a == b) {
            return true;
        } else {
            return false;
        }
    }

}
```

## Demo03OverloadJudge ##

```java
package cn.itcast.day04.demo04;

public class Demo03OverloadJudge {

    /*
    public static void open(){} // 正确重载
    public static void open(int a){} // 正确重载
    static void open(int a,int b){} // 代码错误：和第8行冲突
    public static void open(double a,int b){} // 正确重载
    public static void open(int a,double b){} // 代码错误：和第6行冲突
    public void open(int i,double d){} // 代码错误：和第5行冲突
    public static void OPEN(){} // 代码正确不会报错，但是并不是有效重载
    public static void open(int i,int j){} // 代码错误：和第3行冲突
    */

}
```

## Demo04OverloadPrint ##

```java
package cn.itcast.day04.demo04;

// byte short int long float double char boolean
// String
// 在调用输出语句的时候，println方法其实就是进行了多种数据类型的重载形式。
public class Demo04OverloadPrint {

    public static void main(String[] args) {
        myPrint(100); // int
        myPrint("Hello"); // String
    }

    public static void myPrint(byte num) {
        System.out.println(num);
    }

    public static void myPrint(short num) {
        System.out.println(num);
    }

    public static void myPrint(int num) {
        System.out.println(num);
    }

    public static void myPrint(long num) {
        System.out.println(num);
    }

    public static void myPrint(float num) {
        System.out.println(num);
    }

    public static void myPrint(double num) {
        System.out.println(num);
    }

    public static void myPrint(char zifu) {
        System.out.println(zifu);
    }

    public static void myPrint(boolean is) {
        System.out.println(is);
    }

    public static void myPrint(String str) {
        System.out.println(str);
    }

}
```

# day5 【数组】 #

## Demo01Array ##

```java
package cn.itcast.day05.demo01;

/*
数组的概念：是一种容器，可以同时存放多个数据值。

数组的特点：
1. 数组是一种引用数据类型
2. 数组当中的多个数据，类型必须统一
3. 数组的长度在程序运行期间不可改变

数组的初始化：在内存当中创建一个数组，并且向其中赋予一些默认值。

两种常见的初始化方式：
1. 动态初始化（指定长度）
2. 静态初始化（指定内容）

动态初始化数组的格式：
数据类型[] 数组名称 = new 数据类型[数组长度];

解析含义：
左侧数据类型：也就是数组当中保存的数据，全都是统一的什么类型
左侧的中括号：代表我是一个数组
左侧数组名称：给数组取一个名字
右侧的new：代表创建数组的动作
右侧数据类型：必须和左边的数据类型保持一致
右侧中括号的长度：也就是数组当中，到底可以保存多少个数据，是一个int数字
 */
public class Demo01Array {

    public static void main(String[] args) {
        // 创建一个数组，里面可以存放300个int数据
        // 格式：数据类型[] 数组名称 = new 数据类型[数组长度];
        int[] arrayA = new int[300];

        // 创建一个数组，能存放10个double类型的数据
        double[] arrayB = new double[10];

        // 创建一个数组，能存放5个字符串
        String[] arrayC = new String[5];
    }

}
```

## Demo02Array ##

```java
package cn.itcast.day05.demo01;

/*
动态初始化（指定长度）：在创建数组的时候，直接指定数组当中的数据元素个数。
静态初始化（指定内容）：在创建数组的时候，不直接指定数据个数多少，而是直接将具体的数据内容进行指定。

静态初始化基本格式：
数据类型[] 数组名称 = new 数据类型[] { 元素1, 元素2, ... };

注意事项：
虽然静态初始化没有直接告诉长度，但是根据大括号里面的元素具体内容，也可以自动推算出来长度。
 */
public class Demo02Array {

    public static void main(String[] args) {
        // 直接创建一个数组，里面装的全都是int数字，具体为：5、15、25
        int[] arrayA = new int[] { 5, 15, 25, 40 };

        // 创建一个数组，用来装字符串："Hello"、"World"、"Java"
        String[] arrayB = new String[] { "Hello", "World", "Java" };
    }

}
```

## Demo03Array ##

```java
package cn.itcast.day05.demo01;

/*
使用静态初始化数组的时候，格式还可以省略一下。

标准格式：
数据类型[] 数组名称 = new 数据类型[] { 元素1, 元素2, ... };

省略格式：
数据类型[] 数组名称 = { 元素1, 元素2, ... };

注意事项：
1. 静态初始化没有直接指定长度，但是仍然会自动推算得到长度。
2. 静态初始化标准格式可以拆分成为两个步骤。
3. 动态初始化也可以拆分成为两个步骤。
4. 静态初始化一旦使用省略格式，就不能拆分成为两个步骤了。

使用建议：
如果不确定数组当中的具体内容，用动态初始化；否则，已经确定了具体的内容，用静态初始化。
 */
public class Demo03Array {

    public static void main(String[] args) {
        // 省略格式的静态初始化
        int[] arrayA = { 10, 20, 30 };

        // 静态初始化的标准格式，可以拆分成为两个步骤
        int[] arrayB;
        arrayB = new int[] { 11, 21, 31 };

        // 动态初始化也可以拆分成为两个步骤
        int[] arrayC;
        arrayC = new int[5];

        // 静态初始化的省略格式，不能拆分成为两个步骤。
//        int[] arrayD;
//        arrayD = { 10, 20, 30 };
    }

}
```

## Demo04ArrayUse ##

```java
package cn.itcast.day05.demo01;

/*
直接打印数组名称，得到的是数组对应的：内存地址哈希值。
二进制：01
十进制：0123456789
16进制：0123456789abcdef

访问数组元素的格式：数组名称[索引值]
索引值：就是一个int数字，代表数组当中元素的编号。
【注意】索引值从0开始，一直到“数组的长度-1”为止。
 */
public class Demo04ArrayUse {

    public static void main(String[] args) {
        // 静态初始化的省略格式
        int[] array = { 10, 20, 30 };

        System.out.println(array); // [I@75412c2f 数组对应的：内存地址哈希值

        // 直接打印数组当中的元素
        System.out.println(array[0]); // 10
        System.out.println(array[1]); // 20
        System.out.println(array[2]); // 30
        System.out.println("=============");

        // 也可以将数组当中的某一个单个元素，赋值交给变量
        int num = array[1];
        System.out.println(num); // 20
    }

}
```

## Demo05ArrayUse ##

```java
package cn.itcast.day05.demo01;

/*
使用动态初始化数组的时候，其中的元素将会自动拥有一个默认值。规则如下：
如果是整数类型，那么默认为0；
如果是浮点类型，那么默认为0.0；
如果是字符类型，那么默认为'\u0000'；
如果是布尔类型，那么默认为false；
如果是引用类型，那么默认为null。

注意事项：
静态初始化其实也有默认值的过程，只不过系统自动马上将默认值替换成为了大括号当中的具体数值。
 */
public class Demo05ArrayUse {

    public static void main(String[] args) {
        // 动态初始化一个数组
        int[] array = new int[3];

        System.out.println(array); // 内存地址值
        System.out.println(array[0]); // 0
        System.out.println(array[1]); // 0
        System.out.println(array[2]); // 0
        System.out.println("=================");

        // 将数据123赋值交给数组array当中的1号元素
        array[1] = 123;
        System.out.println(array[0]); // 0
        System.out.println(array[1]); // 123
        System.out.println(array[2]); // 0
    }

}
```

## Demo01ArrayOne-Demo03ArraySame ##

```java
package cn.itcast.day05.demo02;

public class Demo01ArrayOne {

    public static void main(String[] args) {
        int[] array = new int[3]; // 动态初始化
        System.out.println(array); // 地址值
        System.out.println(array[0]); // 0
        System.out.println(array[1]); // 0
        System.out.println(array[2]); // 0
        System.out.println("==============");

        // 改变数组当中元素的内容
        array[1] = 10;
        array[2] = 20;
        System.out.println(array); // 地址值
        System.out.println(array[0]); // 0
        System.out.println(array[1]); // 10
        System.out.println(array[2]); // 20
    }

}
package cn.itcast.day05.demo02;

public class Demo02ArrayTwo {

    public static void main(String[] args) {
        int[] arrayA = new int[3];
        System.out.println(arrayA); // 地址值
        System.out.println(arrayA[0]); // 0
        System.out.println(arrayA[1]); // 0
        System.out.println(arrayA[2]); // 0
        System.out.println("==============");

        arrayA[1] = 10;
        arrayA[2] = 20;
        System.out.println(arrayA); // 地址值
        System.out.println(arrayA[0]); // 0
        System.out.println(arrayA[1]); // 10
        System.out.println(arrayA[2]); // 20
        System.out.println("==============");

        int[] arrayB = new int[3];
        System.out.println(arrayB); // 地址值
        System.out.println(arrayB[0]); // 0
        System.out.println(arrayB[1]); // 0
        System.out.println(arrayB[2]); // 0
        System.out.println("==============");

        arrayB[1] = 100;
        arrayB[2] = 200;
        System.out.println(arrayB); // 地址值
        System.out.println(arrayB[0]); // 0
        System.out.println(arrayB[1]); // 100
        System.out.println(arrayB[2]); // 200
    }

}
package cn.itcast.day05.demo02;

public class Demo03ArraySame {

    public static void main(String[] args) {
        int[] arrayA = new int[3];
        System.out.println(arrayA); // 地址值
        System.out.println(arrayA[0]); // 0
        System.out.println(arrayA[1]); // 0
        System.out.println(arrayA[2]); // 0
        System.out.println("==============");

        arrayA[1] = 10;
        arrayA[2] = 20;
        System.out.println(arrayA); // 地址值
        System.out.println(arrayA[0]); // 0
        System.out.println(arrayA[1]); // 10
        System.out.println(arrayA[2]); // 20
        System.out.println("==============");

        // 将arrayA数组的地址值，赋值给arrayB数组
        int[] arrayB = arrayA;
        System.out.println(arrayB); // 地址值
        System.out.println(arrayB[0]); // 0
        System.out.println(arrayB[1]); // 10
        System.out.println(arrayB[2]); // 20
        System.out.println("==============");

        arrayB[1] = 100;
        arrayB[2] = 200;
        System.out.println(arrayB); // 地址值
        System.out.println(arrayB[0]); // 0
        System.out.println(arrayB[1]); // 100
        System.out.println(arrayB[2]); // 200
    }

}
```

## Demo01ArrayIndex ##

```java
package cn.itcast.day05.demo03;

/*
数组的索引编号从0开始，一直到“数组的长度-1”为止。

如果访问数组元素的时候，索引编号并不存在，那么将会发生
数组索引越界异常
ArrayIndexOutOfBoundsException

原因：索引编号写错了。
解决：修改成为存在的正确索引编号。
 */
        public class Demo01ArrayIndex {

            public static void main(String[] args) {
                int[] array = { 15, 25, 35 };

                System.out.println(array[0]); //15
        System.out.println(array[1]); // 25
        System.out.println(array[2]); // 35

        // 错误写法
        // 并不存在3号元素，所以发生异常
        System.out.println(array[3]);
    }

}
```

## Demo02ArrayNull ##

```java
package cn.itcast.day05.demo03;

/*
所有的引用类型变量，都可以赋值为一个null值。但是代表其中什么都没有。

数组必须进行new初始化才能使用其中的元素。
如果只是赋值了一个null，没有进行new创建，
那么将会发生：
空指针异常 NullPointerException

原因：忘了new
解决：补上new
 */
public class Demo02ArrayNull {

    public static void main(String[] args) {
        int[] array = null;
//        array = new int[3];
        System.out.println(array[0]);
    }

}
```

## Demo03ArrayLength ##

```java
package cn.itcast.day05.demo03;

/*
如何获取数组的长度，格式：
数组名称.length

这将会得到一个int数字，代表数组的长度。

数组一旦创建，程序运行期间，长度不可改变。
 */
public class Demo03ArrayLength {

    public static void main(String[] args) {
        int[] arrayA = new int[3];

        int[] arrayB = {10, 20, 30, 3, 5, 4, 6, 7, 8, 8, 65, 4, 44, 6, 10, 3, 5, 4, 6, 7, 8, 8, 65, 4};
        int len = arrayB.length;
        System.out.println("arrayB数组的长度是：" + len);
        System.out.println("=============");

        int[] arrayC = new int[3];
        System.out.println(arrayC.length); // 3
        arrayC = new int[5];
        System.out.println(arrayC.length); // 5
    }

}

```

## Demo01ArrayParam ##

```java
package cn.itcast.day05.demo04;

/*
数组可以作为方法的参数。
当调用方法的时候，向方法的小括号进行传参，传递进去的其实是数组的地址值。
 */
public class Demo01ArrayParam {

    public static void main(String[] args) {
        int[] array = { 10, 20, 30, 40, 50 };

        System.out.println(array); // 地址值

        printArray(array); // 传递进去的就是array当中保存的地址值
        System.out.println("==========AAA==========");
        printArray(array);
        System.out.println("==========BBB==========");
        printArray(array);
    }

    /*
    三要素
    返回值类型：只是进行打印而已，不需要进行计算，也没有结果，用void
    方法名称：printArray
    参数列表：必须给我数组，我才能打印其中的元素。int[] array
     */
    public static void printArray(int[] array) {
        System.out.println("printArray方法收到的参数是：");
        System.out.println(array); // 地址值
        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }
    }

}

```

## Demo02ArrayReturn ##

```java
package cn.itcast.day05.demo04;

/*
一个方法可以有0、1、多个参数；但是只能有0或者1个返回值，不能有多个返回值。
如果希望一个方法当中产生了多个结果数据进行返回，怎么办？
解决方案：使用一个数组作为返回值类型即可。

任何数据类型都能作为方法的参数类型，或者返回值类型。

数组作为方法的参数，传递进去的其实是数组的地址值。
数组作为方法的返回值，返回的其实也是数组的地址值。
 */
public class Demo02ArrayReturn {

    public static void main(String[] args) {
        int[] result = calculate(10, 20, 30);

        System.out.println("main方法接收到的返回值数组是：");
        System.out.println(result); // 地址值

        System.out.println("总和：" + result[0]);
        System.out.println("平均数：" + result[1]);
    }

    public static int[] calculate(int a, int b, int c) {
        int sum = a + b + c; // 总和
        int avg = sum / 3; // 平均数
        // 两个结果都希望进行返回

        // 需要一个数组，也就是一个塑料兜，数组可以保存多个结果
        /*
        int[] array = new int[2];
        array[0] = sum; // 总和
        array[1] = avg; // 平均数
        */

        int[] array = { sum, avg };
        System.out.println("calculate方法内部数组是：");
        System.out.println(array); // 地址值
        return array;
    }

}
```

# day06【类与对象、封装、构造方法】 #

## Demo01PrintArray ##

```java
package cn.itcast.day06.demo01;

import java.util.Arrays;

/*
面向过程：当需要实现一个功能的时候，每一个具体的步骤都要亲力亲为，详细处理每一个细节。
面向对象：当需要实现一个功能的时候，不关心具体的步骤，而是找一个已经具有该功能的人，来帮我做事儿。
 */
public class Demo01PrintArray {

    public static void main(String[] args) {
        int[] array = { 10, 20, 30, 40, 50, 60 };

        // 要求打印格式为：[10, 20, 30, 40, 50]
        // 使用面向过程，每一个步骤细节都要亲力亲为。
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            if (i == array.length - 1) { // 如果是最后一个元素
                System.out.println(array[i] + "]");
            } else { // 如果不是最后一个元素
                System.out.print(array[i] + ", ");
            }
        }
        System.out.println("==============");

        // 使用面向对象
        // 找一个JDK给我们提供好的Arrays类，
        // 其中有一个toString方法，直接就能把数组变成想要的格式的字符串
        System.out.println(Arrays.toString(array));
    }

}
```

## Student类 ##

```java
package cn.itcast.day06.demo01;

/*
定义一个类，用来模拟“学生”事物。其中就有两个组成部分：

属性（是什么）：
    姓名
    年龄
行为（能做什么）：
    吃饭
    睡觉
    学习

对应到Java的类当中：

成员变量（属性）：
    String name; // 姓名
    int age; // 年龄
成员方法（行为）：
    public void eat() {} // 吃饭
    public void sleep() {} // 睡觉
    public void study() {} // 学习

注意事项：
1. 成员变量是直接定义在类当中的，在方法外边。
2. 成员方法不要写static关键字。
 */
public class Student {

    // 成员变量
    String name; // 姓名
    int age; // 姓名

    // 成员方法
    public void eat() {
        System.out.println("吃饭饭！");
    }

    public void sleep() {
        System.out.println("睡觉觉！");
    }

    public void study() {
        System.out.println("学习！");
    }

}
```

## Demo02Student ##

```java
package cn.itcast.day06.demo01;

/*
通常情况下，一个类并不能直接使用，需要根据类创建一个对象，才能使用。

1. 导包：也就是指出需要使用的类，在什么位置。
import 包名称.类名称;
import cn.itcast.day06.demo01.Student;
对于和当前类属于同一个包的情况，可以省略导包语句不写。

2. 创建，格式：
类名称 对象名 = new 类名称();
Student stu = new Student();

3. 使用，分为两种情况：
使用成员变量：对象名.成员变量名
使用成员方法：对象名.成员方法名(参数)
（也就是，想用谁，就用对象名点儿谁。）

注意事项：
如果成员变量没有进行赋值，那么将会有一个默认值，规则和数组一样。
 */
public class Demo02Student {

    public static void main(String[] args) {
        // 1. 导包。
        // 我需要使用的Student类，和我自己Demo02Student位于同一个包下，所以省略导包语句不写

        // 2. 创建，格式：
        // 类名称 对象名 = new 类名称();
        // 根据Student类，创建了一个名为stu的对象
        Student stu = new Student();

        // 3. 使用其中的成员变量，格式：
        // 对象名.成员变量名
        System.out.println(stu.name); // null
        System.out.println(stu.age); // 0
        System.out.println("=============");

        // 改变对象当中的成员变量数值内容
        // 将右侧的字符串，赋值交给stu对象当中的name成员变量
        stu.name = "赵丽颖";
        stu.age = 18;
        System.out.println(stu.name); // 赵丽颖
        System.out.println(stu.age); // 18
        System.out.println("=============");

        // 4. 使用对象的成员方法，格式：
        // 对象名.成员方法名()
        stu.eat();
        stu.sleep();
        stu.study();
    }

}
```

## Phone类 ##

```java
package cn.itcast.day06.demo02;

/*
定义一个类，用来模拟“手机”事物。
属性：品牌、价格、颜色
行为：打电话、发短信

对应到类当中：
成员变量（属性）：
    String brand; // 品牌
    double price; // 价格
    String color; // 颜色
成员方法（行为）：
    public void call(String who) {} // 打电话
    public void sendMessage() {} // 群发短信
 */
public class Phone {

    // 成员变量
    String brand; // 品牌
    double price; // 价格
    String color; // 颜色

    // 成员方法
    public void call(String who) {
        System.out.println("给" + who + "打电话");
    }

    public void sendMessage() {
        System.out.println("群发短信");
    }
}
```

## Demo01PhoneOne ##

```java
package cn.itcast.day06.demo02;

public class Demo01PhoneOne {

    public static void main(String[] args) {
        // 根据Phone类，创建一个名为one的对象
        // 格式：类名称 对象名 = new 类名称();
        Phone one = new Phone();
        System.out.println(one.brand); // null
        System.out.println(one.price); // 0.0
        System.out.println(one.color); // null
        System.out.println("=========");

        one.brand = "苹果";
        one.price = 8388.0;
        one.color = "黑色";
        System.out.println(one.brand); // 苹果
        System.out.println(one.price); // 8388.0
        System.out.println(one.color); // 黑色
        System.out.println("=========");

        one.call("乔布斯"); // 给乔布斯打电话
        one.sendMessage(); // 群发短信
    }

}
```

## Demo02PhoneTwo ##

```java
package cn.itcast.day06.demo02;

public class Demo02PhoneTwo {

    public static void main(String[] args) {
        Phone one = new Phone();
        System.out.println(one.brand); // null
        System.out.println(one.price); // 0.0
        System.out.println(one.color); // null
        System.out.println("=========");

        one.brand = "苹果";
        one.price = 8388.0;
        one.color = "黑色";
        System.out.println(one.brand); // 苹果
        System.out.println(one.price); // 8388.0
        System.out.println(one.color); // 黑色
        System.out.println("=========");

        one.call("乔布斯"); // 给乔布斯打电话
        one.sendMessage(); // 群发短信
        System.out.println("=========");

        Phone two = new Phone();
        System.out.println(two.brand); // null
        System.out.println(two.price); // 0.0
        System.out.println(two.color); // null
        System.out.println("=========");

        two.brand = "三星";
        two.price = 5999.0;
        two.color = "蓝色";
        System.out.println(two.brand); // 三星
        System.out.println(two.price); // 5999.0
        System.out.println(two.color); // 蓝色
        System.out.println("=========");

        two.call("欧巴"); // 给欧巴打电话
        two.sendMessage(); // 群发短信
    }

}
```

## Demo01VariableDifference ##

```java
package cn.itcast.day06.demo03;

/*
局部变量和成员变量

1. 定义的位置不一样【重点】
局部变量：在方法的内部
成员变量：在方法的外部，直接写在类当中

2. 作用范围不一样【重点】
局部变量：只有方法当中才可以使用，出了方法就不能再用
成员变量：整个类全都可以通用。

3. 默认值不一样【重点】
局部变量：没有默认值，如果要想使用，必须手动进行赋值
成员变量：如果没有赋值，会有默认值，规则和数组一样

4. 内存的位置不一样（了解）
局部变量：位于栈内存
成员变量：位于堆内存

5. 生命周期不一样（了解）
局部变量：随着方法进栈而诞生，随着方法出栈而消失
成员变量：随着对象创建而诞生，随着对象被垃圾回收而消失
 */
public class Demo01VariableDifference {

    String name; // 成员变量

    public void methodA() {
        int num = 20; // 局部变量
        System.out.println(num);
        System.out.println(name);
    }

    public void methodB(int param) { // 方法的参数就是局部变量
        // 参数在方法调用的时候，必然会被赋值的。
        System.out.println(param);

        int age; // 局部变量
//        System.out.println(age); // 没赋值不能用

//        System.out.println(num); // 错误写法！
        System.out.println(name);
    }

}
```

## Demo02Method ##

```java
package cn.itcast.day06.demo03;

/*
面向对象三大特征：封装、继承、多态。

封装性在Java当中的体现：
1. 方法就是一种封装
2. 关键字private也是一种封装

封装就是将一些细节信息隐藏起来，对于外界不可见。
 */
public class Demo02Method {

    public static void main(String[] args) {
        int[] array = {5, 15, 25, 20, 100};

        int max = getMax(array);
        System.out.println("最大值：" + max);
    }

    // 给我一个数组，我还给你一个最大值
    public static int getMax(int[] array) {
        int max = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }
        return max;
    }

}
```

## Person private关键字 ##

```java
package cn.itcast.day06.demo03;

/*
问题描述：定义Person的年龄时，无法阻止不合理的数值被设置进来。
解决方案：用private关键字将需要保护的成员变量进行修饰。

一旦使用了private进行修饰，那么本类当中仍然可以随意访问。
但是！超出了本类范围之外就不能再直接访问了。

间接访问private成员变量，就是定义一对儿Getter/Setter方法

必须叫setXxx或者是getXxx命名规则。
对于Getter来说，不能有参数，返回值类型和成员变量对应；
对于Setter来说，不能有返回值，参数类型和成员变量对应。
 */
public class Person {

    String name; // 姓名
    private int age; // 年龄

    public void show() {
        System.out.println("我叫：" + name + "，年龄：" + age);
    }

    // 这个成员方法，专门用于向age设置数据
    public void setAge(int num) {
        if (num < 100 && num >= 9) { // 如果是合理情况
            age = num;
        } else {
            System.out.println("数据不合理！");
        }
    }

    // 这个成员方法，专门私语获取age的数据
    public int getAge() {
        return age;
    }

}


package cn.itcast.day06.demo03;

public class Demo03Person {

    public static void main(String[] args) {
        Person person = new Person();
        person.show();

        person.name = "赵丽颖";
//        person.age = -20; // 直接访问private内容，错误写法！
        person.setAge(20);
        person.show();
    }

}

```

## Student ##

```java
package cn.itcast.day06.demo03;

/*
对于基本类型当中的boolean值，Getter方法一定要写成isXxx的形式，而setXxx规则不变。
 */
public class Student {

    private String name; // 姓名
    private int age; // 年龄
    private boolean male; // 是不是爷们儿

    public void setMale(boolean b) {
        male = b;
    }

    public boolean isMale() {
        return male;
    }

    public void setName(String str) {
        name = str;
    }

    public String getName() {
        return name;
    }

    public void setAge(int num) {
        age = num;
    }

    public int getAge() {
        return age;
    }
}

package cn.itcast.day06.demo03;

public class Demo04Student {

    public static void main(String[] args) {
        Student stu = new Student();

        stu.setName("鹿晗");
        stu.setAge(20);
        stu.setMale(true);

        System.out.println("姓名：" + stu.getName());
        System.out.println("年龄：" + stu.getAge());
        System.out.println("是不是爷们儿：" + stu.isMale());
    }

}
```

## this ##

```java
package cn.itcast.day06.demo04;

/*
当方法的局部变量和类的成员变量重名的时候，根据“就近原则”，优先使用局部变量。
如果需要访问本类当中的成员变量，需要使用格式：
this.成员变量名

“通过谁调用的方法，谁就是this。”
 */
public class Person {

    String name; // 我自己的名字

    // 参数name是对方的名字
    // 成员变量name是自己的名字
    public void sayHello(String name) {
        System.out.println(name + "，你好。我是" + this.name);
        System.out.println(this);
    }

}
package cn.itcast.day06.demo04;

public class Demo01Person {

    public static void main(String[] args) {
        Person person = new Person();
        // 设置我自己的名字
        person.name = "王健林";
        person.sayHello("王思聪");

        System.out.println(person); // 地址值
    }

}

```

## 构造方法 ##

```java
package cn.itcast.day06.demo04;

/*
构造方法是专门用来创建对象的方法，当我们通过关键字new来创建对象时，其实就是在调用构造方法。
格式：
public 类名称(参数类型 参数名称) {
    方法体
}

注意事项：
1. 构造方法的名称必须和所在的类名称完全一样，就连大小写也要一样
2. 构造方法不要写返回值类型，连void都不写
3. 构造方法不能return一个具体的返回值
4. 如果没有编写任何构造方法，那么编译器将会默认赠送一个构造方法，没有参数、方法体什么事情都不做。
public Student() {}
5. 一旦编写了至少一个构造方法，那么编译器将不再赠送。
6. 构造方法也是可以进行重载的。
重载：方法名称相同，参数列表不同。
 */
public class Student {

    // 成员变量
    private String name;
    private int age;

    // 无参数的构造方法  既然写了全参数构造 那么无参数构造编译器不再赠送要自己加了
    public Student() {
        System.out.println("无参构造方法执行啦！");
    }

    // 全参数的构造方法
    public Student(String name, int age) {
        System.out.println("全参构造方法执行啦！");
        this.name = name;
        this.age = age;
    }

    // Getter Setter
    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getAge() {
        return age;
    }

}
package cn.itcast.day06.demo04;

public class Demo02Student {

    public static void main(String[] args) {
        Student stu1 = new Student(); // 无参构造
        System.out.println("============");

        Student stu2 = new Student("赵丽颖", 20); // 全参构造
        System.out.println("姓名：" + stu2.getName() + "，年龄：" + stu2.getAge());
        // 如果需要改变对象当中的成员变量数据内容，仍然还需要使用setXxx方法
        stu2.setAge(21); // 改变年龄
        System.out.println("姓名：" + stu2.getName() + "，年龄：" + stu2.getAge());

    }

}

```

## 标准的类也叫做Java Bean ##

```java
package cn.itcast.day06.demo05;

/*
一个标准的类通常要拥有下面四个组成部分：

1. 所有的成员变量都要使用private关键字修饰
2. 为每一个成员变量编写一对儿Getter/Setter方法
3. 编写一个无参数的构造方法
4. 编写一个全参数的构造方法

这样标准的类也叫做Java Bean
 */
public class Student {

    private String name; // 姓名
    private int age; // 年龄

    public Student() {
    }

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
```

# day07【Scanner类、Random类、ArrayList类】 #

## Demo01Scanner ##

```java
package cn.itcast.day07.demo01;

import java.util.Scanner; // 1. 导包

/*
Scanner类的功能：可以实现键盘输入数据，到程序当中。

引用类型的一般使用步骤：

1. 导包
import 包路径.类名称;
如果需要使用的目标类，和当前类位于同一个包下，则可以省略导包语句不写。
只有java.lang包下的内容不需要导包，其他的包都需要import语句。

2. 创建
类名称 对象名 = new 类名称();

3. 使用
对象名.成员方法名()

获取键盘输入的一个int数字：int num = sc.nextInt();
获取键盘输入的一个字符串：String str = sc.next();
 */
public class Demo01Scanner {

    public static void main(String[] args) {
        // 2. 创建
        // 备注：System.in代表从键盘进行输入
        Scanner sc = new Scanner(System.in);

        // 3. 获取键盘输入的int数字
        int num = sc.nextInt();
        System.out.println("输入的int数字是：" + num);

        // 4. 获取键盘输入的字符串
        String str = sc.next();
        System.out.println("输入的字符串是：" + str);
    }

}
```

## Demo02ScannerSum ##

```java
package cn.itcast.day07.demo01;

import java.util.Scanner;

/*
题目：
键盘输入两个int数字，并且求出和值。

思路：
1. 既然需要键盘输入，那么就用Scanner
2. Scanner的三个步骤：导包、创建、使用
3. 需要的是两个数字，所以要调用两次nextInt方法
4. 得到了两个数字，就需要加在一起。
5. 将结果打印输出。
 */
public class Demo02ScannerSum {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("请输入第一个数字：");
        int a = sc.nextInt();
        System.out.println("请输入第二个数字：");
        int b = sc.nextInt();

        int result = a + b;
        System.out.println("结果是：" + result);
    }

}
```

## Demo01Anonymous ##

```java
package cn.itcast.day07.demo02;

/*
创建对象的标准格式：
类名称 对象名 = new 类名称();

匿名对象就是只有右边的对象，没有左边的名字和赋值运算符。
new 类名称();

注意事项：匿名对象只能使用唯一的一次，下次再用不得不再创建一个新对象。
使用建议：如果确定有一个对象只需要使用唯一的一次，就可以用匿名对象。
 */
public class Demo01Anonymous {

    public static void main(String[] args) {
        // 左边的one就是对象的名字
        Person one = new Person();
        one.name = "高圆圆";
        one.showName(); // 我叫高圆圆
        System.out.println("===============");

        // 匿名对象
        new Person().name = "赵又廷";
        new Person().showName(); // 我叫：null
    }

}

```

## Demo02Anonymous ##

```java
package cn.itcast.day07.demo02;

import java.util.Scanner;

public class Demo02Anonymous {

    public static void main(String[] args) {
        // 普通使用方式
//        Scanner sc = new Scanner(System.in);
//        int num = sc.nextInt();

        // 匿名对象的方式
//        int num = new Scanner(System.in).nextInt();
//        System.out.println("输入的是：" + num);

        // 使用一般写法传入参数
//        Scanner sc = new Scanner(System.in);
//        methodParam(sc);

        // 使用匿名对象来进行传参
//        methodParam(new Scanner(System.in));

        Scanner sc = methodReturn();
        int num = sc.nextInt();
        System.out.println("输入的是：" + num);
    }

    public static void methodParam(Scanner sc) {
        int num = sc.nextInt();
        System.out.println("输入的是：" + num);
    }

    public static Scanner methodReturn() {
//        Scanner sc = new Scanner(System.in);
//        return sc;
        return new Scanner(System.in);
    }

}
```

## Demo01Random ##

```java
package cn.itcast.day07.demo03;

import java.util.Random;

/*
Random类用来生成随机数字。使用起来也是三个步骤：

1. 导包
import java.util.Random;

2. 创建
Random r = new Random(); // 小括号当中留空即可

3. 使用
获取一个随机的int数字（范围是int所有范围，有正负两种）：int num = r.nextInt()
获取一个随机的int数字（参数代表了范围，左闭右开区间）：int num = r.nextInt(3)
实际上代表的含义是：[0,3)，也就是0~2
 */
public class Demo01Random {

    public static void main(String[] args) {
        Random r = new Random();

        int num = r.nextInt();
        System.out.println("随机数是：" + num);
    }

}
package cn.itcast.day07.demo03;

import java.util.Random;

public class Demo02Random {

    public static void main(String[] args) {
        Random r = new Random();

        for (int i = 0; i < 100; i++) {
            int num = r.nextInt(10); // 范围实际上是0~9
            System.out.println(num);
        }
    }

}
package cn.itcast.day07.demo03;

import java.util.Random;

/*
题目要求：
根据int变量n的值，来获取随机数字，范围是[1,n]，可以取到1也可以取到n。

思路：
1. 定义一个int变量n，随意赋值
2. 要使用Random：三个步骤，导包、创建、使用
3. 如果写10，那么就是0~9，然而想要的是1~10，可以发现：整体+1即可。
4. 打印随机数字
 */
public class Demo03Random {

    public static void main(String[] args) {
        int n = 5;
        Random r = new Random();

        for (int i = 0; i < 100; i++) {
            // 本来范围是[0,n)，整体+1之后变成了[1,n+1)，也就是[1,n]
            int result = r.nextInt(n) + 1;
            System.out.println(result);
        }

    }

}
package cn.itcast.day07.demo03;

import java.util.Random;
import java.util.Scanner;

/*
题目：
用代码模拟猜数字的小游戏。

思路：
1. 首先需要产生一个随机数字，并且一旦产生不再变化。用Random的nextInt方法
2. 需要键盘输入，所以用到了Scanner
3. 获取键盘输入的数字，用Scanner当中的nextInt方法
4. 已经得到了两个数字，判断（if）一下：
    如果太大了，提示太大，并且重试；
    如果太小了，提示太小，并且重试；
    如果猜中了，游戏结束。
5. 重试就是再来一次，循环次数不确定，用while(true)。
 */
public class Demo04RandomGame {

    public static void main(String[] args) {
        Random r = new Random();
        int randomNum = r.nextInt(100) + 1; // [1,100]
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("请输入你猜测的数字：");
            int guessNum = sc.nextInt(); // 键盘输入猜测的数字

            if (guessNum > randomNum) {
                System.out.println("太大了，请重试。");
            } else if (guessNum < randomNum) {
                System.out.println("太小了，请重试。");
            } else {
                System.out.println("恭喜你，猜中啦！");
                break; // 如果猜中，不再重试
            }
        }

        System.out.println("游戏结束。");
    }

}
```

## Demo02ArrayList ##

```java
package cn.itcast.day07.demo04;

public class Person {

    private String name;
    private int age;

    public Person() {
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
package cn.itcast.day07.demo04;

/*
题目：
定义一个数组，用来存储3个Person对象。

数组有一个缺点：一旦创建，程序运行期间长度不可以发生改变。
 */
public class Demo01Array {

    public static void main(String[] args) {
        // 首先创建一个长度为3的数组，里面用来存放Person类型的对象
        Person[] array = new Person[3];

        Person one = new Person("迪丽热巴", 18);
        Person two = new Person("古力娜扎", 28);
        Person three = new Person("玛尔扎哈", 38);

        // 将one当中的地址值赋值到数组的0号元素位置
        array[0] = one;
        array[1] = two;
        array[2] = three;

        System.out.println(array[0]); // 地址值
        System.out.println(array[1]); // 地址值
        System.out.println(array[2]); // 地址值

        System.out.println(array[1].getName()); // 古力娜扎
    }

}
package cn.itcast.day07.demo04;

import java.util.ArrayList;

/*
数组的长度不可以发生改变。
但是ArrayList集合的长度是可以随意变化的。

对于ArrayList来说，有一个尖括号<E>代表泛型。
泛型：也就是装在集合当中的所有元素，全都是统一的什么类型。
注意：泛型只能是引用类型，不能是基本类型。

注意事项：
对于ArrayList集合来说，直接打印得到的不是地址值，而是内容。
如果内容是空，得到的是空的中括号：[]
 */
public class Demo02ArrayList {

    public static void main(String[] args) {
        // 创建了一个ArrayList集合，集合的名称是list，里面装的全都是String字符串类型的数据
        // 备注：从JDK 1.7+开始，右侧的尖括号内部可以不写内容，但是<>本身还是要写的。
        ArrayList<String> list = new ArrayList<>();
        System.out.println(list); // []

        // 向集合当中添加一些数据，需要用到add方法。
        list.add("赵丽颖");
        System.out.println(list); // [赵丽颖]

        list.add("迪丽热巴");
        list.add("古力娜扎");
        list.add("玛尔扎哈");
        System.out.println(list); // [赵丽颖, 迪丽热巴, 古力娜扎, 玛尔扎哈]

//        list.add(100); // 错误写法！因为创建的时候尖括号泛型已经说了是字符串，添加进去的元素就必须都是字符串才行

    }

}

```

## Demo03ArrayListMethod ##

```java
package cn.itcast.day07.demo04;

import java.util.ArrayList;

/*
ArrayList当中的常用方法有：

public boolean add(E e)：向集合当中添加元素，参数的类型和泛型一致。返回值代表添加是否成功。
备注：对于ArrayList集合来说，add添加动作一定是成功的，所以返回值可用可不用。
但是对于其他集合（今后学习）来说，add添加动作不一定成功。

public E get(int index)：从集合当中获取元素，参数是索引编号，返回值就是对应位置的元素。

public E remove(int index)：从集合当中删除元素，参数是索引编号，返回值就是被删除掉的元素。

public int size()：获取集合的尺寸长度，返回值是集合中包含的元素个数。
 */
public class Demo03ArrayListMethod {

    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        System.out.println(list); // []

        // 向集合中添加元素：add
        boolean success = list.add("柳岩");
        System.out.println(list); // [柳岩]
        System.out.println("添加的动作是否成功：" + success); // true

        list.add("高圆圆");
        list.add("赵又廷");
        list.add("李小璐");
        list.add("贾乃亮");
        System.out.println(list); // [柳岩, 高圆圆, 赵又廷, 李小璐, 贾乃亮]

        // 从集合中获取元素：get。索引值从0开始
        String name = list.get(2);
        System.out.println("第2号索引位置：" + name); // 赵又廷

        // 从集合中删除元素：remove。索引值从0开始。
        String whoRemoved = list.remove(3);
        System.out.println("被删除的人是：" + whoRemoved); // 李小璐
        System.out.println(list); // [柳岩, 高圆圆, 赵又廷, 贾乃亮]

        // 获取集合的长度尺寸，也就是其中元素的个数
        int size = list.size();
        System.out.println("集合的长度是：" + size);
    }

}
```

## Demo05ArrayListBasic ##

```java
package cn.itcast.day07.demo04;

import java.util.ArrayList;

/*
如果希望向集合ArrayList当中存储基本类型数据，必须使用基本类型对应的“包装类”。

基本类型    包装类（引用类型，包装类都位于java.lang包下）
byte        Byte
short       Short
int         Integer     【特殊】
long        Long
float       Float
double      Double
char        Character   【特殊】
boolean     Boolean

从JDK 1.5+开始，支持自动装箱、自动拆箱。

自动装箱：基本类型 --> 包装类型
自动拆箱：包装类型 --> 基本类型
 */
public class Demo05ArrayListBasic {

    public static void main(String[] args) {
        ArrayList<String> listA = new ArrayList<>();
        // 错误写法！泛型只能是引用类型，不能是基本类型    Arraylist中放的是地址
//        ArrayList<int> listB = new ArrayList<>();

        ArrayList<Integer> listC = new ArrayList<>();
        listC.add(100);
        listC.add(200);
        System.out.println(listC); // [100, 200]

        int num = listC.get(1);
        System.out.println("第1号元素是：" + num);
    }

}
```

## Demo01ArrayListRandom ##

```java
package cn.itcast.day07.demo05;

import java.util.ArrayList;
import java.util.Random;

/*
题目：
生成6个1~33之间的随机整数，添加到集合，并遍历集合。

思路：
1. 需要存储6个数字，创建一个集合，<Integer>
2. 产生随机数，需要用到Random
3. 用循环6次，来产生6个随机数字：for循环
4. 循环内调用r.nextInt(int n)，参数是33，0~32，整体+1才是1~33
5. 把数字添加到集合中：add
6. 遍历集合：for、size、get
 */
public class Demo01ArrayListRandom {

    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        Random r = new Random();
        for (int i = 0; i < 6; i++) {
            int num = r.nextInt(33) + 1;
            list.add(num);
        }
        // 遍历集合
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }
    }

}
```

## Demo02ArrayListStudent ##

```java
package cn.itcast.day07.demo05;

import java.util.ArrayList;

/*
题目：
自定义4个学生对象，添加到集合，并遍历。

思路：
1. 自定义Student学生类，四个部分。
2. 创建一个集合，用来存储学生对象。泛型：<Student>
3. 根据类，创建4个学生对象。
4. 将4个学生对象添加到集合中：add
5. 遍历集合：for、size、get
 */
public class Demo02ArrayListStudent {

    public static void main(String[] args) {
        ArrayList<Student> list = new ArrayList<>();

        Student one = new Student("洪七公", 20);
        Student two = new Student("欧阳锋", 21);
        Student three = new Student("黄药师", 22);
        Student four = new Student("段智兴", 23);

        list.add(one);
        list.add(two);
        list.add(three);
        list.add(four);

        // 遍历集合
        for (int i = 0; i < list.size(); i++) {
            Student stu = list.get(i);
            System.out.println("姓名：" + stu.getName() + "，年龄" + stu.getAge());
        }
    }

}
```

## Demo03ArrayListPrint ##

```java
package cn.itcast.day07.demo05;

import java.util.ArrayList;

/*
题目：
定义以指定格式打印集合的方法(ArrayList类型作为参数)，使用{}扩起集合，使用@分隔每个元素。
格式参照 {元素@元素@元素}。

System.out.println(list);       [10, 20, 30]
printArrayList(list);           {10@20@30}
 */
public class Demo03ArrayListPrint {

    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("张三丰");
        list.add("宋远桥");
        list.add("张无忌");
        list.add("张翠山");
        System.out.println(list); // [张三丰, 宋远桥, 张无忌, 张翠山]

        printArrayList(list);
    }

    /*
    定义方法的三要素
    返回值类型：只是进行打印而已，没有运算，没有结果；所以用void
    方法名称：printArrayList
    参数列表：ArrayList
     */
    public static void printArrayList(ArrayList<String> list) {
        // {10@20@30}
        System.out.print("{");
        for (int i = 0; i < list.size(); i++) {
            String name = list.get(i);
            if (i == list.size() - 1) {
                System.out.println(name + "}");
            } else {
                System.out.print(name + "@");
            }
        }
    }

}
```

## Demo04ArrayListReturn ##

```java
japackage cn.itcast.day07.demo05;

import java.util.ArrayList;
import java.util.Random;

/*
题目：
用一个大集合存入20个随机数字，然后筛选其中的偶数元素，放到小集合当中。
要求使用自定义的方法来实现筛选。

分析：
1. 需要创建一个大集合，用来存储int数字：<Integer>
2. 随机数字就用Random nextInt
3. 循环20次，把随机数字放入大集合：for循环、add方法
4. 定义一个方法，用来进行筛选。
筛选：根据大集合，筛选符合要求的元素，得到小集合。
三要素
返回值类型：ArrayList小集合（里面元素个数不确定）
方法名称：getSmallList
参数列表：ArrayList大集合（装着20个随机数字）
5. 判断（if）是偶数：num % 2 == 0
6. 如果是偶数，就放到小集合当中，否则不放。
 */
public class Demo04ArrayListReturn {

    public static void main(String[] args) {
        ArrayList<Integer> bigList = new ArrayList<>();
        Random r = new Random();
        for (int i = 0; i < 20; i++) {
            int num = r.nextInt(100) + 1; // 1~100
            bigList.add(num);
        }

        ArrayList<Integer> smallList = getSmallList(bigList);

        System.out.println("偶数总共有多少个：" + smallList.size());
        for (int i = 0; i < smallList.size(); i++) {
            System.out.println(smallList.get(i));
        }
    }

    // 这个方法，接收大集合参数，返回小集合结果
    public static ArrayList<Integer> getSmallList(ArrayList<Integer> bigList) {
        // 创建一个小集合，用来装偶数结果
        ArrayList<Integer> smallList = new ArrayList<>();
        for (int i = 0; i < bigList.size(); i++) {
            int num = bigList.get(i);
            if (num % 2 == 0) {
                smallList.add(num);
            }
        }
        return smallList;
    }

}
```

# day08【String类、static、Arrays类、Math类】 #

## Demo01String ##

```java
package cn.itcast.day08.demo01;

/*
java.lang.String类代表字符串。
API当中说：Java 程序中的所有字符串字面值（如 "abc" ）都作为此类的实例实现。
其实就是说：程序当中所有的双引号字符串，都是String类的对象。（就算没有new，也照样是。）

字符串的特点：
1. 字符串的内容永不可变。【重点】
2. 正是因为字符串不可改变，所以字符串是可以共享使用的。
3. 字符串效果上相当于是char[]字符数组，但是底层原理是byte[]字节数组。

创建字符串的常见3+1种方式。
三种构造方法：
public String()：创建一个空白字符串，不含有任何内容。
public String(char[] array)：根据字符数组的内容，来创建对应的字符串。
public String(byte[] array)：根据字节数组的内容，来创建对应的字符串。
一种直接创建：
String str = "Hello"; // 右边直接用双引号

注意：直接写上双引号，就是字符串对象。
 */
public class Demo01String {

    public static void main(String[] args) {
        // 使用空参构造
        String str1 = new String(); // 小括号留空，说明字符串什么内容都没有。
        System.out.println("第1个字符串：" + str1);

        // 根据字符数组创建字符串
        char[] charArray = { 'A', 'B', 'C' };
        String str2 = new String(charArray);
        System.out.println("第2个字符串：" + str2);

        // 根据字节数组创建字符串
        byte[] byteArray = { 97, 98, 99 };
        String str3 = new String(byteArray);
        System.out.println("第3个字符串：" + str3);

        // 直接创建
        String str4 = "Hello";
        System.out.println("第4个字符串：" + str4);
    }

}
```

## Demo02StringPool ##

```java
package cn.itcast.day08.demo01;

/*
字符串常量池：程序当中直接写上的双引号字符串，就在字符串常量池中。

对于基本类型来说，==是进行数值的比较。
对于引用类型来说，==是进行【地址值】的比较。
 */
public class Demo02StringPool {

    public static void main(String[] args) {
        String str1 = "abc";
        String str2 = "abc";

        char[] charArray = {'a', 'b', 'c'};

        String str3 = new String(charArray);
        String str4 = new String("ABC");

        System.out.println(str1 == str2); // true
        System.out.println(str1 == str3); // false
        System.out.println(str2 == str3); // false
        System.out.println(str2 == str4); // false
    }
}
```

## Demo01StringEquals ##

```JAVA
package cn.itcast.day08.demo02;

/*
==是进行对象的地址值比较，如果确实需要字符串的内容比较，可以使用两个方法：

public boolean equals(Object obj)：参数可以是任何对象，只有参数是一个字符串并且内容相同的才会给true；否则返回false。
注意事项：
1. 任何对象都能用Object进行接收。
2. equals方法具有对称性，也就是a.equals(b)和b.equals(a)效果一样。
3. 如果比较双方一个常量一个变量，推荐把常量字符串写在前面。
推荐："abc".equals(str)    不推荐：str.equals("abc")

public boolean equalsIgnoreCase(String str)：忽略大小写，进行内容比较。
 */
public class Demo01StringEquals {

    public static void main(String[] args) {
        String str1 = "Hello";
        String str2 = "Hello";
        char[] charArray = {'H', 'e', 'l', 'l', 'o'};
        String str3 = new String(charArray);

        System.out.println(str1.equals(str2)); // true
        System.out.println(str2.equals(str3)); // true
        System.out.println(str3.equals("Hello")); // true
        System.out.println("Hello".equals(str1)); // true

        String str4 = "hello";
        System.out.println(str1.equals(str4)); // false
        System.out.println("=================");

        String str5 = null;
        System.out.println("abc".equals(str5)); // 推荐：false
//        System.out.println(str5.equals("abc")); // 不推荐：报错，空指针异常NullPointerException
        System.out.println("=================");

        String strA = "Java";
        String strB = "java";
        System.out.println(strA.equals(strB)); // false，严格区分大小写
        System.out.println(strA.equalsIgnoreCase(strB)); // true，忽略大小写

        // 注意，只有英文字母区分大小写，其他都不区分大小写
        System.out.println("abc一123".equalsIgnoreCase("abc壹123")); // false
    }

}
```

## Demo02StringGet ##

```java
package cn.itcast.day08.demo02;

/*
String当中与获取相关的常用方法有：

public int length()：获取字符串当中含有的字符个数，拿到字符串长度。
public String concat(String str)：将当前字符串和参数字符串拼接成为返回值新的字符串。
public char charAt(int index)：获取指定索引位置的单个字符。（索引从0开始。）
public int indexOf(String str)：查找参数字符串在本字符串当中首次出现的索引位置，如果没有返回-1值。
 */
public class Demo02StringGet {

    public static void main(String[] args) {
        // 获取字符串的长度
        int length = "asdasfeutrvauevbueyvb".length();
        System.out.println("字符串的长度是：" + length);

        // 拼接字符串
        String str1 = "Hello";
        String str2 = "World";
        String str3 = str1.concat(str2);
        System.out.println(str1); // Hello，原封不动
        System.out.println(str2); // World，原封不动
        System.out.println(str3); // HelloWorld，新的字符串
        System.out.println("==============");

        // 获取指定索引位置的单个字符
        char ch = "Hello".charAt(1);
        System.out.println("在1号索引位置的字符是：" + ch);
        System.out.println("==============");

        // 查找参数字符串在本来字符串当中出现的第一次索引位置
        // 如果根本没有，返回-1值
        String original = "HelloWorldHelloWorld";
        int index = original.indexOf("llo");
        System.out.println("第一次索引值是：" + index); // 2

        System.out.println("HelloWorld".indexOf("abc")); // -1
    }
}
```

## Demo03Substring ##

```java
package cn.itcast.day08.demo02;

/*
字符串的截取方法：

public String substring(int index)：截取从参数位置一直到字符串末尾，返回新字符串。
public String substring(int begin, int end)：截取从begin开始，一直到end结束，中间的字符串。
备注：[begin,end)，包含左边，不包含右边。
 */
public class Demo03Substring {

    public static void main(String[] args) {
        String str1 = "HelloWorld";
        String str2 = str1.substring(5);
        System.out.println(str1); // HelloWorld，原封不动
        System.out.println(str2); // World，新字符串
        System.out.println("================");

        String str3 = str1.substring(4, 7);
        System.out.println(str3); // oWo  [begin, end)
        System.out.println("================");

        // 下面这种写法，字符串的内容仍然是没有改变的
        // 下面有两个字符串："Hello"，"Java"
        // strA当中保存的是地址值。
        // 本来地址值是Hello的0x666，
        // 后来地址值变成了Java的0x999
        String strA = "Hello";
        System.out.println(strA); // Hello
        strA = "Java";
        System.out.println(strA); // Java
    }
}
```

## Demo04StringConvert ##

```java
package cn.itcast.day08.demo02;

/*
String当中与转换相关的常用方法有：

public char[] toCharArray()：将当前字符串拆分成为字符数组作为返回值。
public byte[] getBytes()：获得当前字符串底层的字节数组。
public String replace(CharSequence oldString, CharSequence newString)：
将所有出现的老字符串替换成为新的字符串，返回替换之后的结果新字符串。
备注：CharSequence意思就是说可以接受字符串类型。
 */
public class Demo04StringConvert {

    public static void main(String[] args) {
        // 转换成为字符数组
        char[] chars = "Hello".toCharArray();
        System.out.println(chars[0]); // H
        System.out.println(chars.length); // 5
        System.out.println("==============");

        // 转换成为字节数组
        byte[] bytes = "abc".getBytes();
        for (int i = 0; i < bytes.length; i++) {
            System.out.println(bytes[i]);
        }
        System.out.println("==============");

        // 字符串的内容替换
        String str1 = "How do you do?";
        String str2 = str1.replace("o", "*");
        System.out.println(str1); // How do you do?
        System.out.println(str2); // H*w d* y*u d*?
        System.out.println("==============");

        String lang1 = "会不会玩儿呀！你大爷的！你大爷的！你大爷的！！！";
        String lang2 = lang1.replace("你大爷的", "****");
        System.out.println(lang2); // 会不会玩儿呀！****！****！****！！！
    }

}
```

## Demo05StringSplit ##

```java
package cn.itcast.day08.demo02;

/*
分割字符串的方法：
public String[] split(String regex)：按照参数的规则，将字符串切分成为若干部分。

注意事项：
split方法的参数其实是一个“正则表达式”，今后学习。
今天要注意：如果按照英文句点“.”进行切分，必须写"\\."（两个反斜杠）
 */
public class Demo05StringSplit {

    public static void main(String[] args) {
        String str1 = "aaa,bbb,ccc";
        String[] array1 = str1.split(",");
        for (int i = 0; i < array1.length; i++) {
            System.out.println(array1[i]);
        }
        System.out.println("===============");

        String str2 = "aaa bbb ccc";
        String[] array2 = str2.split(" ");
        for (int i = 0; i < array2.length; i++) {
            System.out.println(array2[i]);
        }
        System.out.println("===============");

        String str3 = "XXX.YYY.ZZZ";
        String[] array3 = str3.split("\\.");
        System.out.println(array3.length); // 0
        for (int i = 0; i < array3.length; i++) {
            System.out.println(array3[i]);
        }
    }
}
```

## Demo06StringPractise ##

```java
package cn.itcast.day08.demo02;

/*
题目：
定义一个方法，把数组{1,2,3}按照指定格式拼接成一个字符串。格式参照如下：[word1#word2#word3]。

分析：
1. 首先准备一个int[]数组，内容是：1、2、3
2. 定义一个方法，用来将数组变成字符串
三要素
返回值类型：String
方法名称：fromArrayToString
参数列表：int[]
3. 格式：[word1#word2#word3]
用到：for循环、字符串拼接、每个数组元素之前都有一个word字样、分隔使用的是#、区分一下是不是最后一个
4. 调用方法，得到返回值，并打印结果字符串
 */
public class Demo06StringPractise {

    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4};

        String result = fromArrayToString(array);
        System.out.println(result);
    }

    public static String fromArrayToString(int[] array) {
        String str = "[";
        for (int i = 0; i < array.length; i++) {
            if (i == array.length - 1) {
                str += "word" + array[i] + "]";
            } else {
                str += "word" + array[i] + "#";
            }
        }
        return str;
    }

}
```

## Demo07StringCount ##

```java
package cn.itcast.day08.demo02;

import java.util.Scanner;

/*
题目：
键盘输入一个字符串，并且统计其中各种字符出现的次数。
种类有：大写字母、小写字母、数字、其他

思路：
1. 既然用到键盘输入，肯定是Scanner
2. 键盘输入的是字符串，那么：String str = sc.next();
3. 定义四个变量，分别代表四种字符各自的出现次数。
4. 需要对字符串一个字、一个字检查，String-->char[]，方法就是toCharArray()
5. 遍历char[]字符数组，对当前字符的种类进行判断，并且用四个变量进行++动作。
6. 打印输出四个变量，分别代表四种字符出现次数。
 */
public class Demo07StringCount {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个字符串：");
        String input = sc.next(); // 获取键盘输入的一个字符串

        int countUpper = 0; // 大写字母
        int countLower = 0; // 小写字母
        int countNumber = 0; // 数字
        int countOther = 0; // 其他字符

        char[] charArray = input.toCharArray();
        for (int i = 0; i < charArray.length; i++) {
            char ch = charArray[i]; // 当前单个字符
            if ('A' <= ch && ch <= 'Z') {
                countUpper++;
            } else if ('a' <= ch && ch <= 'z') {
                countLower++;
            } else if ('0' <= ch && ch <= '9') {
                countNumber++;
            } else {
                countOther++;
            }
        }

        System.out.println("大写字母有：" + countUpper);
        System.out.println("小写字母有：" + countLower);
        System.out.println("数字有：" + countNumber);
        System.out.println("其他字符有：" + countOther);
    }

}
```

## Demo01StaticField ##

```java
package cn.itcast.day08.demo03;

public class Student {

    private int id; // 学号
    private String name; // 姓名
    private int age; // 年龄
    static String room; // 所在教室
    private static int idCounter = 0; // 学号计数器，每当new了一个新对象的时候，计数器++

    public Student() {
        this.id = ++idCounter;
    }

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
        this.id = ++idCounter;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
package cn.itcast.day08.demo03;

/*
如果一个成员变量使用了static关键字，那么这个变量不再属于对象自己，而是属于所在的类。多个对象共享同一份数据。
 */
public class Demo01StaticField {

    public static void main(String[] args) {

        Student two = new Student("黄蓉", 16);
        two.room = "101教室";
        System.out.println("姓名：" + two.getName()
                + "，年龄：" + two.getAge() + "，教室：" + two.room
                + "，学号：" + two.getId());

        Student one = new Student("郭靖", 19);
        System.out.println("姓名：" + one.getName()
                + "，年龄：" + one.getAge() + "，教室：" + one.room
                + "，学号：" + one.getId());
    }

}

```

## Demo02StaticMethod静态不能直接访问非静态 ##

```java
package cn.itcast.day08.demo03;

public class MyClass {

    int num; // 成员变量
    static int numStatic; // 静态变量

    // 成员方法
    public void method() {
        System.out.println("这是一个成员方法。");
        // 成员方法可以访问成员变量
        System.out.println(num);
        // 成员方法可以访问静态变量
        System.out.println(numStatic);
    }

    // 静态方法
    public static void methodStatic() {
        System.out.println("这是一个静态方法。");
        // 静态方法可以访问静态变量
        System.out.println(numStatic);
        // 静态不能直接访问非静态【重点】
//        System.out.println(num); // 错误写法！

        // 静态方法中不能使用this关键字。
//        System.out.println(this); // 错误写法！
    }

}

package cn.itcast.day08.demo03;

/*
一旦使用static修饰成员方法，那么这就成为了静态方法。静态方法不属于对象，而是属于类的。

如果没有static关键字，那么必须首先创建对象，然后通过对象才能使用它。
如果有了static关键字，那么不需要创建对象，直接就能通过类名称来使用它。

无论是成员变量，还是成员方法。如果有了static，都推荐使用类名称进行调用。
静态变量：类名称.静态变量
静态方法：类名称.静态方法()

注意事项：
1. 静态不能直接访问非静态。
原因：因为在内存当中是【先】有的静态内容，【后】有的非静态内容。
“先人不知道后人，但是后人知道先人。”
2. 静态方法当中不能用this。
原因：this代表当前对象，通过谁调用的方法，谁就是当前对象。
 */
public class Demo02StaticMethod {

    public static void main(String[] args) {
        MyClass obj = new MyClass(); // 首先创建对象
        // 然后才能使用没有static关键字的内容
        obj.method();

        // 对于静态方法来说，可以通过对象名进行调用，也可以直接通过类名称来调用。
        obj.methodStatic(); // 正确，不推荐，这种写法在编译之后也会被javac翻译成为“类名称.静态方法名”
        MyClass.methodStatic(); // 正确，推荐

        // 对于本来当中的静态方法，可以省略类名称
        myMethod();
        Demo02StaticMethod.myMethod(); // 完全等效
    }

    public static void myMethod() {
        System.out.println("自己的方法！");
    }

}
```

## Demo04Static静态代码块 ##

```java
package cn.itcast.day08.demo03;


public class Person {

    static {
        System.out.println("静态代码块执行！");
    }

    public Person() {
        System.out.println("构造方法执行！");
    }

}
package cn.itcast.day08.demo03;

/*
静态代码块的格式是：

public class 类名称 {
    static {
        // 静态代码块的内容
    }
}

特点：当第一次用到本类时，静态代码块执行唯一的一次。
静态内容总是优先于非静态，所以静态代码块比构造方法先执行。

静态代码块的典型用途：
用来一次性地对静态成员变量进行赋值。
 */
public class Demo04Static {

    public static void main(String[] args) {
        Person one = new Person();
        Person two = new Person();
    }

}
```

## Demo01Arrays ##

```java
package cn.itcast.day08.demo04;

import java.util.Arrays;

/*
java.util.Arrays是一个与数组相关的工具类，里面提供了大量静态方法，用来实现数组常见的操作。

public static String toString(数组)：将参数数组变成字符串（按照默认格式：[元素1, 元素2, 元素3...]）
public static void sort(数组)：按照默认升序（从小到大）对数组的元素进行排序。

备注：
1. 如果是数值，sort默认按照升序从小到大
2. 如果是字符串，sort默认按照字母升序
3. 如果是自定义的类型，那么这个自定义的类需要有Comparable或者Comparator接口的支持。（今后学习）
 */
public class Demo01Arrays {

    public static void main(String[] args) {
        int[] intArray = {10, 20, 30};
        // 将int[]数组按照默认格式变成字符串
        String intStr = Arrays.toString(intArray);
        System.out.println(intStr); // [10, 20, 30]

        int[] array1 = {2, 1, 3, 10, 6};
        Arrays.sort(array1);
        System.out.println(Arrays.toString(array1)); // [1, 2, 3, 6, 10]

        String[] array2 = {"bbb", "aaa", "ccc"};
        Arrays.sort(array2);
        System.out.println(Arrays.toString(array2)); // [aaa, bbb, ccc]
    }

}
package cn.itcast.day08.demo04;

import java.util.Arrays;

/*
题目：
请使用Arrays相关的API，将一个随机字符串中的所有字符升序排列，并倒序打印。
 */
public class Demo02ArraysPractise {

    public static void main(String[] args) {
        String str = "asv76agfqwdfvasdfvjh";

        // 如何进行升序排列：sort
        // 必须是一个数组，才能用Arrays.sort方法
        // String --> 数组，用toCharArray
        char[] chars = str.toCharArray();
        Arrays.sort(chars); // 对字符数组进行升序排列

        // 需要倒序遍历  chars.forr倒序遍历
        for (int i = chars.length - 1; i >= 0; i--) {
            System.out.println(chars[i]);
        }
    }

}

```

## Demo03Math ##

```java
package cn.itcast.day08.demo04;

/*
java.util.Math类是数学相关的工具类，里面提供了大量的静态方法，完成与数学运算相关的操作。

public static double abs(double num)：获取绝对值。有多种重载。
public static double ceil(double num)：向上取整。
public static double floor(double num)：向下取整。
public static long round(double num)：四舍五入。

Math.PI代表近似的圆周率常量（double）。
 */
public class Demo03Math {

    public static void main(String[] args) {
        // 获取绝对值
        System.out.println(Math.abs(3.14)); // 3.14
        System.out.println(Math.abs(0)); // 0
        System.out.println(Math.abs(-2.5)); // 2.5
        System.out.println("================");

        // 向上取整
        System.out.println(Math.ceil(3.9)); // 4.0
        System.out.println(Math.ceil(3.1)); // 4.0
        System.out.println(Math.ceil(3.0)); // 3.0
        System.out.println("================");

        // 向下取整，抹零
        System.out.println(Math.floor(30.1)); // 30.0
        System.out.println(Math.floor(30.9)); // 30.0
        System.out.println(Math.floor(31.0)); // 31.0
        System.out.println("================");

        System.out.println(Math.round(20.4)); // 20
        System.out.println(Math.round(10.5)); // 11
    }

}
package cn.itcast.day08.demo04;

/*
题目：
计算在-10.8到5.9之间，绝对值大于6或者小于2.1的整数有多少个？

分析：
1. 既然已经确定了范围，for循环
2. 起点位置-10.8应该转换成为-10，两种办法：
    2.1 可以使用Math.ceil方法，向上（向正方向）取整
    2.2 强转成为int，自动舍弃所有小数位
3. 每一个数字都是整数，所以步进表达式应该是num++，这样每次都是+1的。
4. 如何拿到绝对值：Math.abs方法。
5. 一旦发现了一个数字，需要让计数器++进行统计。

备注：如果使用Math.ceil方法，-10.8可以变成-10.0。注意double也是可以进行++的。
 */
public class Demo04MathPractise {

    public static void main(String[] args) {
        int count = 0; // 符合要求的数量

        double min = -10.8;
        double max = 5.9;
        // 这样处理，变量i就是区间之内所有的整数
        for (int i = (int) min; i < max; i++) {
            int abs = Math.abs(i); // 绝对值
            if (abs > 6 || abs < 2.1) {
                System.out.println(i);
                count++;
            }
        }

        System.out.println("总共有：" + count); // 9
    }

}

```

# day09【继承、super、this、抽象类】 #

## Demo01Extends ##

```java
package cn.itcast.day09.demo01;

/*
在继承的关系中，“子类就是一个父类”。也就是说，子类可以被当做父类看待。
例如父类是员工，子类是讲师，那么“讲师就是一个员工”。关系：is-a。

定义父类的格式：（一个普通的类定义）
public class 父类名称 {
    // ...
}

定义子类的格式：
public class 子类名称 extends 父类名称 {
    // ...
}
 */
public class Demo01Extends {

    public static void main(String[] args) {
        // 创建了一个子类对象
        Teacher teacher = new Teacher();
        // Teacher类当中虽然什么都没写，但是会继承来自父类的method方法。
        teacher.method();

        // 创建另一个子类助教的对象
        Assistant assistant = new Assistant();
        assistant.method();
    }

}
package cn.itcast.day09.demo01;

// 定义一个父类：员工
public class Employee {

    public void method() {
        System.out.println("方法执行！");
    }

}
package cn.itcast.day09.demo01;

// 定义了一个员工的子类：讲师
public class Teacher extends Employee {

}
package cn.itcast.day09.demo01;

// 定义了员工的另一个子类：助教
public class Assistant extends Employee {
}
```

## Demo01ExtendsField ##

```java
package cn.itcast.day09.demo02;

public class Fu {

    int numFu = 10;

    int num = 100;

    public void methodFu() {
        // 使用的是本类当中的，不会向下找子类的
        System.out.println(num);
    }

}
package cn.itcast.day09.demo02;

public class Zi extends Fu {

    int numZi = 20;

    int num = 200;

    public void methodZi() {
        // 因为本类当中有num，所以这里用的是本类的num
        System.out.println(num);
    }

}
package cn.itcast.day09.demo02;

/*
在父子类的继承关系当中，如果成员变量重名，则创建子类对象时，访问有两种方式：

直接通过子类对象访问成员变量：
    等号左边是谁，就优先用谁，没有则向上找。 Zi zi = new Zi();
间接通过成员方法访问成员变量：
    该方法属于谁，就优先用谁，没有则向上找。
 */
public class Demo01ExtendsField {

    public static void main(String[] args) {
        Fu fu = new Fu(); // 创建父类对象
        System.out.println(fu.numFu); // 只能使用父类的东西，没有任何子类内容
        System.out.println("===========");

        Zi zi = new Zi();

        System.out.println(zi.numFu); // 10
        System.out.println(zi.numZi); // 20
        System.out.println("===========");

        // 等号左边是谁，就优先用谁
        System.out.println(zi.num); // 优先子类，200
//        System.out.println(zi.abc); // 到处都没有，编译报错！
        System.out.println("===========");

        // 这个方法是子类的，优先用子类的，没有再向上找
        zi.methodZi(); // 200
        // 这个方法是在父类当中定义的，
        zi.methodFu(); // 100
    }

}

```

## Demo01ExtendsField 继承后的成员变量 ##

```java
package cn.itcast.day09.demo03;

public class Fu {

    int num = 10;

}
package cn.itcast.day09.demo03;

public class Zi extends Fu {

    int num = 20;

    public void method() {
        int num = 30;
        System.out.println(num); // 30，局部变量
        System.out.println(this.num); // 20，本类的成员变量
        System.out.println(super.num); // 10，父类的成员变量
    }

}
package cn.itcast.day09.demo03;

/*
局部变量：         直接写成员变量名
本类的成员变量：    this.成员变量名
父类的成员变量：    super.成员变量名
 */
public class Demo01ExtendsField {

    public static void main(String[] args) {
        Zi zi = new Zi();

        zi.method();
    }

}

```

## Demo01ExtendsMethod重写/重载 ##

```java
package cn.itcast.day09.demo04;

public class Fu {

    public void methodFu() {
        System.out.println("父类方法执行！");
    }

    public void method() {
        System.out.println("父类重名方法执行！");
    }

}
package cn.itcast.day09.demo04;

public class Zi extends Fu {

    public void methodZi() {
        System.out.println("子类方法执行！");
    }

    public void method() {
        System.out.println("子类重名方法执行！");
    }

}
package cn.itcast.day09.demo04;

/*
在父子类的继承关系当中，创建子类对象，访问成员方法的规则：
    创建的对象是谁，就优先用谁，如果没有则向上找。

注意事项：
无论是成员方法还是成员变量，如果没有都是向上找父类，绝对不会向下找子类的。

重写（Override）
概念：在继承关系当中，方法的名称一样，参数列表也一样。

重写（Override）：方法的名称一样，参数列表【也一样】。覆盖、覆写。
重载（Overload）：方法的名称一样，参数列表【不一样】。

方法的覆盖重写特点：创建的是子类对象，则优先用子类方法。
 */
public class Demo01ExtendsMethod {

    public static void main(String[] args) {
        Zi zi = new Zi();

        zi.methodFu();
        zi.methodZi();

        // 创建的是new了子类对象，所以优先用子类方法
        zi.method();
    }

}
```

## Demo01Override @Override ##

```java
package cn.itcast.day09.demo05;

public class Fu {

    public String method() {
        return null;
    }

}
package cn.itcast.day09.demo05;

public class Zi extends Fu {

    @Override
    public String method() {
        return null;
    }

}
package cn.itcast.day09.demo05;

/*
方法覆盖重写的注意事项：

1. 必须保证父子类之间方法的名称相同，参数列表也相同。
@Override：写在方法前面，用来检测是不是有效的正确覆盖重写。
这个注解就算不写，只要满足要求，也是正确的方法覆盖重写。

2. 子类方法的返回值必须【小于等于】父类方法的返回值范围。
小扩展提示：java.lang.Object类是所有类的公共最高父类（祖宗类），java.lang.String就是Object的子类。

3. 子类方法的权限必须【大于等于】父类方法的权限修饰符。
小扩展提示：public > protected > (default) > private
备注：(default)不是关键字default，而是什么都不写，留空。
 */
public class Demo01Override {

}
```

## Demo01Phone ##

```java
package cn.itcast.day09.demo06;

// 本来的老款手机
public class Phone {

    public void call() {
        System.out.println("打电话");
    }

    public void send() {
        System.out.println("发短信");
    }

    public void show() {
        System.out.println("显示号码");
    }

}
package cn.itcast.day09.demo06;

// 定义一个新手机，使用老手机作为父类
public class NewPhone extends Phone {

    @Override
    public void show() {
        super.show(); // 把父类的show方法拿过来重复利用
        // 自己子类再来添加更多内容
        System.out.println("显示姓名");
        System.out.println("显示头像");
    }
}
package cn.itcast.day09.demo06;

public class Demo01Phone {

    public static void main(String[] args) {
        Phone phone = new Phone();
        phone.call();
        phone.send();
        phone.show();
        System.out.println("==========");

        NewPhone newPhone = new NewPhone();
        newPhone.call();
        newPhone.send();
        newPhone.show();
    }
}
```

## Demo01Constructor父子类构造方法 ##

```java
package cn.itcast.day09.demo07;

public class Fu {

    public Fu() {
        System.out.println("父类无参构造");
    }

    public Fu(int num) {
        System.out.println("父类有参构造！");
    }

}
package cn.itcast.day09.demo07;

public class Zi extends Fu {

    public Zi() {
        super(); // 在调用父类无参构造方法
//        super(20); // 在调用父类重载的构造方法
        System.out.println("子类构造方法！");
    }
    public Zi(int n){
//构造过程中默认调用父类的super() 无参构造
    }

    public void method() {
//        super(); // 错误写法！只有子类构造方法，才能调用父类构造方法。
    }

}
package cn.itcast.day09.demo07;

/*
继承关系中，父子类构造方法的访问特点：

1. 子类构造方法当中有一个默认隐含的“super()”调用，所以一定是先调用的父类构造，后执行的子类构造。
2. 子类构造可以通过super关键字来调用父类重载构造。
3. super的父类构造调用，必须是"子类构造方法"的第一个语句。不能一个子类构造调用多次super构造。
总结：
子类必须调用父类构造方法，不写则赠送super()；写了则用写的指定的super调用，super只能有一个，还必须是第一个。
 */
public class Demo01Constructor {

    public static void main(String[] args) {
        Zi zi = new Zi();
    }

}

```

## super关键字的用法有三种： ##

```java
package cn.itcast.day09.demo08;

public class Fu {

    int num = 10;

    public void method() {
        System.out.println("父类方法");
    }

}
package cn.itcast.day09.demo08;

/*
super关键字的用法有三种：
1. 在子类的成员方法中，访问父类的成员变量。
2. 在子类的成员方法中，访问父类的成员方法。
3. 在子类的构造方法中，访问父类的构造方法。
 */
public class Zi extends Fu {

    int num = 20;

    public Zi() {
        super();
    }

    public void methodZi() {
        System.out.println(super.num); // 父类中的num
    }

    public void method() {
        super.method(); // 访问父类中的method
        System.out.println("子类方法");
    }

}
```

## supre+this ##

```java
package cn.itcast.day09.demo09;

public class Fu {

    int num = 30;

}
package cn.itcast.day09.demo09;

/*
super关键字用来访问父类内容，而this关键字用来访问本类内容。用法也有三种：

1. 在本类的成员方法中，访问本类的成员变量。
2. 在本类的成员方法中，访问本类的另一个成员方法。
3. 在本类的构造方法中，访问本类的另一个构造方法。
在第三种用法当中要注意：
A. this(...)调用也必须是构造方法的第一个语句，唯一一个。
B. super和this两种构造调用，不能同时使用。
 */
public class Zi extends Fu {

    int num = 20;

    public Zi() {
//        super(); // 这一行不再赠送
        this(123); // 本类的无参构造，调用本类的有参构造
//        this(1, 2); // 错误写法！
    }

    public Zi(int n) {
        this(1, 2);
    }

    public Zi(int n, int m) {
    }

    public void showNum() {
        int num = 10;
        System.out.println(num); // 局部变量
        System.out.println(this.num); // 本类中的成员变量
        System.out.println(super.num); // 父类中的成员变量
    }

    public void methodA() {
        System.out.println("AAA");
    }

    public void methodB() {
        this.methodA();
        System.out.println("BBB");
    }

}

```

##  supre+this

```java
package cn.itcast.day09.demo10;

public class Fu {

    int num = 10;

    public void method() {
        System.out.println("父类方法");
    }

}
package cn.itcast.day09.demo10;

public class Zi extends Fu {

    int num = 20;

    @Override
    public void method() {
        super.method(); // 调用了父类方法
        System.out.println("子类方法");
    }

    public void show() {
        int num = 30;
        System.out.println(num); // 30
        System.out.println(this.num); // 20
        System.out.println(super.num); // 10
    }
}
```

## 抽象类 ##

```java
package cn.itcast.day09.demo11;

/*
抽象方法：就是加上abstract关键字，然后去掉大括号，直接分号结束。
抽象类：抽象方法所在的类，必须是抽象类才行。在class之前写上abstract即可。

如何使用抽象类和抽象方法：
1. 不能直接创建new抽象类对象。
2. 必须用一个子类来继承抽象父类。
3. 子类必须覆盖重写抽象父类当中所有的抽象方法。
覆盖重写（实现）：子类去掉抽象方法的abstract关键字，然后补上方法体大括号。
4. 创建子类对象进行使用。
 */
public abstract class Animal {

    // 这是一个抽象方法，代表吃东西，但是具体吃什么（大括号的内容）不确定。
    public abstract void eat();

    // 这是普通的成员方法
//    public void normalMethod() {
//
//    }

}
package cn.itcast.day09.demo11;

public class Cat extends Animal {

    @Override
    public void eat() {
        System.out.println("猫吃鱼");
    }

}
package cn.itcast.day09.demo11;

public class DemoMain {

    public static void main(String[] args) {
//        Animal animal = new Animal(); // 错误写法！不能直接创建抽象类对象

        Cat cat = new Cat();
        cat.eat();
    }

}
```

##  不能直接创建抽象类对象

```java
package cn.itcast.day09.demo13;

// 最高的抽象父类
public abstract class Animal {

    public abstract void eat();

    public abstract void sleep();

}
package cn.itcast.day09.demo13;

// 子类也是一个抽象类
public abstract class Dog extends Animal {

    @Override
    public void eat() {
        System.out.println("狗吃骨头");
    }

    // public abstract void sleep();
}
package cn.itcast.day09.demo13;

public class Dog2Ha extends Dog {
    @Override
    public void sleep() {
        System.out.println("嘿嘿嘿……");
    }
}
package cn.itcast.day09.demo13;

public class DogGolden extends Dog {
    @Override
    public void sleep() {
        System.out.println("呼呼呼……");
    }
}
package cn.itcast.day09.demo13;

public class DemoMain {

    public static void main(String[] args) {
//        Animal animal = new Animal(); // 错误！

//        Dog dog = new Dog(); // 错误，这也是抽象类

        Dog2Ha ha = new Dog2Ha(); // 这是普通类，可以直接new对象。
        ha.eat();
        ha.sleep();
        System.out.println("==========");

        DogGolden golden = new DogGolden();
        golden.eat();
        golden.sleep();
    }
}
```

## MainRedPacket收发红包 ##

```java
package cn.itcast.day09.demo14;

public class User {

    private String name; // 姓名
    private int money; // 余额，也就是当前用户拥有的钱数

    public User() {
    }

    public User(String name, int money) {
        this.name = name;
        this.money = money;
    }

    // 展示一下当前用户有多少钱
    public void show() {
        System.out.println("我叫：" + name + "，我有多少钱：" + money);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
    }
}

package cn.itcast.day09.demo14;

import java.util.ArrayList;

// 群主的类
public class Manager extends User {

    public Manager() {
    }

    public Manager(String name, int money) {
        super(name, money);
    }

    public ArrayList<Integer> send(int totalMoney, int count) {
        // 首先需要一个集合，用来存储若干个红包的金额
        ArrayList<Integer> redList = new ArrayList<>();

        // 首先看一下群主自己有多少钱
        int leftMoney = super.getMoney(); // 群主当前余额
        if (totalMoney > leftMoney) {
            System.out.println("余额不足");
            return redList; // 返回空集合
        }

        // 扣钱，其实就是重新设置余额
        super.setMoney(leftMoney - totalMoney);

        // 发红包需要平均拆分成为count份
        int avg = totalMoney / count;
        int mod = totalMoney % count; // 余数，也就是甩下的零头

        // 除不开的零头，包在最后一个红包当中
        // 下面把红包一个一个放到集合当中
        for (int i = 0; i < count - 1; i++) {
            redList.add(avg);
        }

        // 最后一个红包
        int last = avg + mod;
        redList.add(last);

        return redList;
    }
}
package cn.itcast.day09.demo14;

import java.util.ArrayList;
import java.util.Random;

// 普通成员
public class Member extends User {

    public Member() {
    }

    public Member(String name, int money) {
        super(name, money);
    }

    public void receive(ArrayList<Integer> list) {
        // 从多个红包当中随便抽取一个，给我自己。
        // 随机获取一个集合当中的索引编号
        int index = new Random().nextInt(list.size());
        // 根据索引，从集合当中删除，并且得到被删除的红包，给我自己
        int delta = list.remove(index);
        // 当前成员自己本来有多少钱：
        int money = super.getMoney();
        // 加法，并且重新设置回去
        super.setMoney(money + delta);
    }
}
package cn.itcast.day09.demo14;

import java.util.ArrayList;

public class MainRedPacket {

    public static void main(String[] args) {
        Manager manager = new Manager("群主", 100);

        Member one = new Member("成员A", 0);
        Member two = new Member("成员B", 0);
        Member three = new Member("成员C", 0);

        manager.show(); // 100
        one.show(); // 0
        two.show(); // 0
        three.show(); // 0
        System.out.println("===============");

        // 群主总共发20块钱，分成3个红包
        ArrayList<Integer> redList = manager.send(20, 3);
        // 三个普通成员收红包
        one.receive(redList);
        two.receive(redList);
        three.receive(redList);

        manager.show(); // 100-20=80
        // 6、6、8，随机分给三个人
        one.show();
        two.show();
        three.show();
    }

}
```

# day10【接口、多态】 #

## Demo01Interface 接口的抽象方法，通过类创建对象 ##

```java
package cn.itcast.day10.demo01;

/*
在任何版本的Java中，接口都能定义抽象方法。
格式：
public abstract 返回值类型 方法名称(参数列表);

注意事项：
1. 接口当中的抽象方法，修饰符必须是两个固定的关键字：public abstract
2. 这两个关键字修饰符，可以选择性地省略。（今天刚学，所以不推荐。）
3. 方法的三要素，可以随意定义。
 */
public interface MyInterfaceAbstract {

    // 这是一个抽象方法
    public abstract void methodAbs1();

    // 这也是抽象方法
    abstract void methodAbs2();

    // 这也是抽象方法
    public void methodAbs3();

    // 这也是抽象方法
    void methodAbs4();

}
package cn.itcast.day10.demo01;

public class MyInterfaceAbstractImpl implements MyInterfaceAbstract {
    @Override
    public void methodAbs1() {
        System.out.println("这是第一个方法！");
    }

    @Override
    public void methodAbs2() {
        System.out.println("这是第二个方法！");
    }

    @Override
    public void methodAbs3() {
        System.out.println("这是第三个方法！");
    }

    @Override
    public void methodAbs4() {
        System.out.println("这是第四个方法！");
    }
}
package cn.itcast.day10.demo01;

/*
接口就是多个类的公共规范。
接口是一种引用数据类型，最重要的内容就是其中的：抽象方法。

如何定义一个接口的格式：
public interface 接口名称 {
    // 接口内容
}

备注：换成了关键字interface之后，编译生成的字节码文件仍然是：.java --> .class。

如果是Java 7，那么接口中可以包含的内容有：
1. 常量
2. 抽象方法

如果是Java 8，还可以额外包含有：
3. 默认方法
4. 静态方法

如果是Java 9，还可以额外包含有：
5. 私有方法

接口使用步骤：
1. 接口不能直接使用，必须有一个“实现类”来“实现”该接口。
格式：
public class 实现类名称 implements 接口名称 {
    // ...
}
2. 接口的实现类必须覆盖重写（实现）接口中所有的抽象方法。
实现：去掉abstract关键字，加上方法体大括号。
3. 创建实现类的对象，进行使用。

注意事项：
如果实现类并没有覆盖重写接口中所有的抽象方法，那么这个实现类自己就必须是抽象类。
 */
public class Demo01Interface {

    public static void main(String[] args) {
        // 错误写法！不能直接new接口对象使用。
//        MyInterfaceAbstract inter = new MyInterfaceAbstract();

        // 创建实现类的对象使用
        MyInterfaceAbstractImpl impl = new MyInterfaceAbstractImpl();
        impl.methodAbs1();
        impl.methodAbs2();
    }

}
```

## Demo02 default关键字,接口升级的默认方法 ##

```java
package cn.itcast.day10.demo01;

/*
从Java 8开始，接口里允许定义默认方法。
格式：
public default 返回值类型 方法名称(参数列表) {
    方法体
}

备注：接口当中的默认方法，可以解决接口升级的问题。
 */
public interface MyInterfaceDefault {

    // 抽象方法
    public abstract void methodAbs();

    // 新添加了一个抽象方法  接口升级添加抽象方法使得旧的AB需要改动
//    public abstract void methodAbs2();

    // 新添加的方法，改成默认方法
    public default void methodDefault() {
        System.out.println("这是新添加的默认方法");
    }

}
package cn.itcast.day10.demo01;

public class MyInterfaceDefaultA implements MyInterfaceDefault {
    @Override
    public void methodAbs() {
        System.out.println("实现了抽象方法，AAA");
    }
}
package cn.itcast.day10.demo01;

public class MyInterfaceDefaultB implements MyInterfaceDefault {
    @Override
    public void methodAbs() {
        System.out.println("实现了抽象方法，BBB");
    }

    @Override
    public void methodDefault() {
        System.out.println("实现类B覆盖重写了接口的默认方法");
    }
}
package cn.itcast.day10.demo01;

/*
1. 接口的默认方法，可以通过接口实现类对象，直接调用。
2. 接口的默认方法，也可以被接口实现类进行覆盖重写。
 */
public class Demo02Interface {

    public static void main(String[] args) {
        // 创建了实现类对象
        MyInterfaceDefaultA a = new MyInterfaceDefaultA();
        a.methodAbs(); // 调用抽象方法，实际运行的是右侧实现类。

        // 调用默认方法，如果实现类当中没有，会向上找接口
        a.methodDefault(); // 这是新添加的默认方法
        System.out.println("==========");

        MyInterfaceDefaultB b = new MyInterfaceDefaultB();
        b.methodAbs();
        b.methodDefault(); // 实现类B覆盖重写了接口的默认方法
    }
}
```

## Demo03Interface 接口的静态方法 ##

```java
package cn.itcast.day10.demo01;

/*
从Java 8开始，接口当中允许定义静态方法。
格式：
public static 返回值类型 方法名称(参数列表) {
    方法体
}
提示：就是将abstract或者default换成static即可，带上方法体。
 */
public interface MyInterfaceStatic {

    public static void methodStatic() {
        System.out.println("这是接口的静态方法！");
    }
}
package cn.itcast.day10.demo01;

public class MyInterfaceStaticImpl implements MyInterfaceStatic {
}
package cn.itcast.day10.demo01;

/*
注意事项：不能通过接口实现类的对象来调用接口当中的静态方法。
正确用法：通过接口名称，直接调用其中的静态方法。
格式：
接口名称.静态方法名(参数);
 */
public class Demo03Interface {

    public static void main(String[] args) {
        // 创建了实现类对象
        MyInterfaceStaticImpl impl = new MyInterfaceStaticImpl();

        // 错误写法！
//        impl.methodStatic();

        // 直接通过接口名称调用静态方法
        MyInterfaceStatic.methodStatic();
    }

}
```

## Demo04Interface 接口的私有方法(默认/静态) ##

```java
package cn.itcast.day10.demo01;

/*
问题描述：
我们需要抽取一个共有方法，用来解决两个默认方法之间重复代码的问题。
但是这个共有方法不应该让实现类使用，应该是私有化的。

解决方案：
从Java 9开始，接口当中允许定义私有方法。
1. 普通私有方法，解决多个默认方法之间重复代码问题
格式：
private 返回值类型 方法名称(参数列表) {
    方法体
}

2. 静态私有方法，解决多个静态方法之间重复代码问题
格式：
private static 返回值类型 方法名称(参数列表) {
    方法体
}
 */
public interface MyInterfacePrivateA {

    public default void methodDefault1() {
        System.out.println("默认方法1");
        methodCommon();
    }

    public default void methodDefault2() {
        System.out.println("默认方法2");
        methodCommon();
    }

    private void methodCommon() {
        System.out.println("AAA");
        System.out.println("BBB");
        System.out.println("CCC");
    }
}
package cn.itcast.day10.demo01;

public class MyInterfacePrivateAImpl implements MyInterfacePrivateA {

    public void methodAnother() {
        // 直接访问到了接口中的默认方法，这样是错误的！
//        methodCommon();
    }

}
package cn.itcast.day10.demo01;

public interface MyInterfacePrivateB {

    public static void methodStatic1() {
        System.out.println("静态方法1");
        methodStaticCommon();
    }

    public static void methodStatic2() {
        System.out.println("静态方法2");
        methodStaticCommon();
    }

    private static void methodStaticCommon() {
        System.out.println("AAA");
        System.out.println("BBB");
        System.out.println("CCC");
    }
}
package cn.itcast.day10.demo01;

public class Demo04Interface {

    public static void main(String[] args) {
        MyInterfacePrivateB.methodStatic1();
        MyInterfacePrivateB.methodStatic2();
        // 错误写法！
//        MyInterfacePrivateB.methodStaticCommon();
    }

}

```

## Demo05Interface 接口的变量(不可修改的常量) ##

```java
package cn.itcast.day10.demo01;

/*
接口当中也可以定义“成员变量”，但是必须使用public static final三个关键字进行修饰。
从效果上看，这其实就是接口的【常量】。
格式：
public static final 数据类型 常量名称 = 数据值;
备注：
一旦使用final关键字进行修饰，说明不可改变。

注意事项：
1. 接口当中的常量，可以省略public static final，注意：不写也照样是这样。
2. 接口当中的常量，必须进行赋值；不能不赋值。
3. 接口中常量的名称，使用完全大写的字母，用下划线进行分隔。（推荐命名规则）
 */
public interface MyInterfaceConst {

    // 这其实就是一个常量，一旦赋值，不可以修改
    public static final int NUM_OF_MY_CLASS = 12;
}
package cn.itcast.day10.demo01;

public class Demo05Interface {

    public static void main(String[] args) {
        // 访问接口当中的常量
        System.out.println(MyInterfaceConst.NUM_OF_MY_CLASS);
    }
}
```

## Demo01Interface 多个接口(默认/抽象)方法重复 ##

```java
package cn.itcast.day10.demo02;

public interface MyInterfaceA {

    // 错误写法！接口不能有静态代码块
//    static {
//
//    }

    // 错误写法！接口不能有构造方法
//    public MyInterfaceA() {
//
//    }

    public abstract void methodA();

    public abstract void methodAbs();

    public default void methodDefault() {
        System.out.println("默认方法AAA");
    }

}
package cn.itcast.day10.demo02;

public interface MyInterfaceB {

    // 错误写法！接口不能有静态代码块
//    static {
//
//    }

    // 错误写法！接口不能有构造方法
//    public MyInterfaceA() {
//
//    }

    public abstract void methodB();

    public abstract void methodAbs();

    public default void methodDefault() {
        System.out.println("默认方法BBB");
    }

}
package cn.itcast.day10.demo02;

public abstract class MyInterfaceAbstract implements MyInterfaceA, MyInterfaceB {
    @Override
    public void methodA() {

    }

    @Override
    public void methodAbs() {

    }

    @Override
    public void methodDefault() {

    }


}
package cn.itcast.day10.demo02;

public class MyInterfaceImpl /*extends Object*/ implements MyInterfaceA, MyInterfaceB {

    @Override
    public void methodA() {
        System.out.println("覆盖重写了A方法");
    }


    @Override
    public void methodB() {
        System.out.println("覆盖重写了B方法");
    }

    @Override
    public void methodAbs() {
        System.out.println("覆盖重写了AB接口都有的抽象方法");
    }

    @Override
    public void methodDefault() {
        System.out.println("对多个接口当中冲突的默认方法进行了覆盖重写");
    }
}
package cn.itcast.day10.demo02;

/*
使用接口的时候，需要注意：

1. 接口是没有静态代码块或者构造方法的。
2. 一个类的直接父类是唯一的，但是一个类可以同时实现多个接口。
格式：
public class MyInterfaceImpl implements MyInterfaceA, MyInterfaceB {
    // 覆盖重写所有抽象方法
}
3. 如果实现类所实现的多个接口当中，存在重复的抽象方法，那么只需要覆盖重写一次即可。
4. 如果实现类没有覆盖重写所有接口当中的所有抽象方法，那么实现类就必须是一个抽象类。
5. 如果实现类锁实现的多个接口当中，存在重复的默认方法，那么实现类一定要对冲突的默认方法进行覆盖重写。
6. 一个类如果直接父类当中的方法，和接口当中的默认方法产生了冲突，优先用父类当中的方法。
 */
public class Demo01Interface {

    public static void main(String[] args) {
        Zi zi = new Zi();
        zi.method();
    }

}

```

## Demo01Interface 多个接口 (父类/接口)方法重复 ##

```java
package cn.itcast.day10.demo02;

public class Fu {

    public void method() {
        System.out.println("父类方法");
    }

}
package cn.itcast.day10.demo02;

public interface MyInterface {

    public default void method() {
        System.out.println("接口的默认方法");
    }

}
package cn.itcast.day10.demo02;

public class Zi extends Fu implements MyInterface {
}
package cn.itcast.day10.demo02;

/*
使用接口的时候，需要注意：

1. 接口是没有静态代码块或者构造方法的。
2. 一个类的直接父类是唯一的，但是一个类可以同时实现多个接口。
格式：
public class MyInterfaceImpl implements MyInterfaceA, MyInterfaceB {
    // 覆盖重写所有抽象方法
}
3. 如果实现类所实现的多个接口当中，存在重复的抽象方法，那么只需要覆盖重写一次即可。
4. 如果实现类没有覆盖重写所有接口当中的所有抽象方法，那么实现类就必须是一个抽象类。
5. 如果实现类锁实现的多个接口当中，存在重复的默认方法，那么实现类一定要对冲突的默认方法进行覆盖重写。
6. 一个类如果直接父类当中的方法，和接口当中的默认方法产生了冲突，优先用父类当中的方法。
 */
public class Demo01Interface {

    public static void main(String[] args) {
        Zi zi = new Zi();
        zi.method();//父类方法
    }

}
```

## Demo01Relations 接口的多继承 ##

```java
package cn.itcast.day10.demo03;

public interface MyInterfaceA {

    public abstract void methodA();

    public abstract void methodCommon();

    public default void methodDefault() {
        System.out.println("AAA");
    }

}
package cn.itcast.day10.demo03;

public interface MyInterfaceB {

    public abstract void methodB();

    public abstract void methodCommon();

    public default void methodDefault() {
        System.out.println("BBB");
    }

}
package cn.itcast.day10.demo03;

/*
这个子接口当中有几个方法？答：4个。
methodA 来源于接口A
methodB 来源于接口B
methodCommon 同时来源于接口A和B
method 来源于我自己
 */
public interface MyInterface extends MyInterfaceA, MyInterfaceB {

    public abstract void method();

    @Override
    public default void methodDefault() {

    }
}
package cn.itcast.day10.demo03;

public class MyInterfaceImpl implements MyInterface {
    @Override
    public void method() {

    }

    @Override
    public void methodA() {

    }

    @Override
    public void methodB() {

    }

    @Override
    public void methodCommon() {

    }
}
package cn.itcast.day10.demo03;

/*
1. 类与类之间是单继承的。直接父类只有一个。
2. 类与接口之间是多实现的。一个类可以实现多个接口。
3. 接口与接口之间是多继承的。

注意事项：
1. 多个父接口当中的抽象方法如果重复，没关系。
2. 多个父接口当中的默认方法如果重复，那么子接口必须进行默认方法的覆盖重写，【而且带着default关键字】。
 */
public class Demo01Relations {
}

```

## 多态 ##

## Demo01Multi  ##

```java
package cn.itcast.day10.demo04;

public class Fu {

    public void method() {
        System.out.println("父类方法");
    }

    public void methodFu() {
        System.out.println("父类特有方法");
    }

}
package cn.itcast.day10.demo04;

public class Zi extends Fu {

    @Override
    public void method() {
        System.out.println("子类方法");
    }
}
package cn.itcast.day10.demo04;

/*
代码当中体现多态性，其实就是一句话：父类引用指向子类对象。

格式：
父类名称 对象名 = new 子类名称();
或者：
接口名称 对象名 = new 实现类名称();
 */
public class Demo01Multi {

    public static void main(String[] args) {
        // 使用多态的写法
        // 左侧父类的引用，指向了右侧子类的对象
        Fu obj = new Zi();

        obj.method();//子类方法
        obj.methodFu();//父类特有方法
    }
}
```

## Demo01MultiField 多态中的成员变量 ##

```java
package cn.itcast.day10.demo05;

public class Fu /*extends Object*/ {

    int num = 10;

    public void showNum() {
        System.out.println(num);
    }

    public void method() {
        System.out.println("父类方法");
    }

    public void methodFu() {
        System.out.println("父类特有方法");
    }

}
package cn.itcast.day10.demo05;

public class Zi extends Fu {

    int num = 20;

    int age = 16;

    @Override
    public void showNum() {
        System.out.println(num);
    }

    @Override
    public void method() {
        System.out.println("子类方法");
    }

    public void methodZi() {
        System.out.println("子类特有方法");
    }
}
package cn.itcast.day10.demo05;

/*
访问成员变量的两种方式：

1. 直接通过对象名称访问成员变量：看等号左边是谁，优先用谁，没有则向上找。
2. 间接通过成员方法访问成员变量：看该方法属于谁，优先用谁，没有则向上找。
 */
public class Demo01MultiField {

    public static void main(String[] args) {
        // 使用多态的写法，父类引用指向子类对象
        Fu obj = new Zi();
        System.out.println(obj.num); // 父：10
//        System.out.println(obj.age); // 错误写法！
        System.out.println("=============");

        // 子类没有覆盖重写，就是父：10
        // 子类如果覆盖重写，就是子：20
        obj.showNum();
    }
}

```

## Demo02MultiMethod 多态中的成员方法 ##

```java
package cn.itcast.day10.demo05;

/*
在多态的代码当中，成员方法的访问规则是：
    看new的是谁，就优先用谁，没有则向上找。

口诀：编译看左边，运行看右边。

对比一下：
成员变量：编译看左边，运行还看左边。
成员方法：编译看左边，运行看右边。
 */
public class Demo02MultiMethod {

    public static void main(String[] args) {
        Fu obj = new Zi(); // 多态

        obj.method(); // 父子都有，优先用子
        obj.methodFu(); // 子类没有，父类有，向上找到父类

        // 编译看左边，左边是Fu，Fu当中没有methodZi方法，所以编译报错。
//        obj.methodZi(); // 错误写法！    子类有父类没有 编译不会通过(编译看左)
    }

}
```

## Demo01Main 对象的向上向下转型 ##

```java
package cn.itcast.day10.demo06;

public abstract class Animal {

    public abstract void eat();

}
package cn.itcast.day10.demo06;

public class Cat extends Animal {
    @Override
    public void eat() {
        System.out.println("猫吃鱼");
    }

    // 子类特有方法
    public void catchMouse() {
        System.out.println("猫抓老鼠");
    }
}
package cn.itcast.day10.demo06;

/*
向上转型一定是安全的，没有问题的，正确的。但是也有一个弊端：
对象一旦向上转型为父类，那么就无法调用子类原本特有的内容。

解决方案：用对象的向下转型【还原】。
 */
public class Demo01Main {

    public static void main(String[] args) {
        // 对象的向上转型，就是：父类引用指向之类对象。
        Animal animal = new Cat(); // 本来创建的时候是一只猫
        animal.eat(); // 猫吃鱼

//        animal.catchMouse(); // 错误写法！

        // 向下转型，进行“还原”动作
        Cat cat = (Cat) animal;
        cat.catchMouse(); // 猫抓老鼠

        // 下面是错误的向下转型
        // 本来new的时候是一只猫，现在非要当做狗
        // 错误写法！编译不会报错，但是运行会出现异常：
        // java.lang.ClassCastException，类转换异常
        Dog dog = (Dog) animal;
    }
}
package cn.itcast.day10.demo06;

public class Dog extends Animal {
    @Override
    public void eat() {
        System.out.println("狗吃SHIT");
    }

    public void watchHouse() {
        System.out.println("狗看家");
    }
}
```

## Demo02Instanceof 判断原型是什么 ##

```java
package cn.itcast.day10.demo06;

/*
如何才能知道一个父类引用的对象，本来是什么子类？
格式：
对象 instanceof 类名称
这将会得到一个boolean值结果，也就是判断前面的对象能不能当做后面类型的实例。
 */
public class Demo02Instanceof {

    public static void main(String[] args) {
        Animal animal = new Dog(); // 本来是一只狗
        animal.eat(); // 狗吃SHIT

        // 如果希望掉用子类特有方法，需要向下转型
        // 判断一下父类引用animal本来是不是Dog
        if (animal instanceof Dog) {
            Dog dog = (Dog) animal;
            dog.watchHouse();
        }
        // 判断一下animal本来是不是Cat
        if (animal instanceof Cat) {
            Cat cat = (Cat) animal;
            cat.catchMouse();
        }

        giveMeAPet(new Dog());
    }

    public static void giveMeAPet(Animal animal) {
        if (animal instanceof Dog) {
            Dog dog = (Dog) animal;
            dog.watchHouse();
        }
        if (animal instanceof Cat) {
            Cat cat = (Cat) animal;
            cat.catchMouse();
        }
    }

}
```

## * Computer 接口基本使用 对象上下转型 接口作为方法参数 ##

```java
package cn.itcast.day10.demo07;

public interface USB {

    public abstract void open(); // 打开设备

    public abstract void close(); // 关闭设备

}
package cn.itcast.day10.demo07;

// 鼠标就是一个USB设备
public class Mouse implements USB {
    @Override
    public void open() {
        System.out.println("打开鼠标");
    }

    @Override
    public void close() {
        System.out.println("关闭鼠标");
    }

    public void click() {
        System.out.println("鼠标点击");
    }
}
package cn.itcast.day10.demo07;

// 键盘就是一个USB设备
public class Keyboard implements USB {
    @Override
    public void open() {
        System.out.println("打开键盘");
    }

    @Override
    public void close() {
        System.out.println("关闭键盘");
    }

    public void type() {
        System.out.println("键盘输入");
    }
}
package cn.itcast.day10.demo07;

public class Computer {

    public void powerOn() {
        System.out.println("笔记本电脑开机");
    }

    public void powerOff() {
        System.out.println("笔记本电脑关机");
    }

    // 使用USB设备的方法，使用接口作为方法的参数
    public void useDevice(USB usb) {
        usb.open(); // 打开设备
        if (usb instanceof Mouse) { // 一定要先判断
            Mouse mouse = (Mouse) usb; // 向下转型
            mouse.click();
        } else if (usb instanceof Keyboard) { // 先判断
            Keyboard keyboard = (Keyboard) usb; // 向下转型
            keyboard.type();
        }
        usb.close(); // 关闭设备
    }

}
package cn.itcast.day10.demo07;

public class DemoMain {

    public static void main(String[] args) {
        // 首先创建一个笔记本电脑
        Computer computer = new Computer();
        computer.powerOn();

        // 准备一个鼠标，供电脑使用
//        Mouse mouse = new Mouse();
        // 首先进行向上转型
        USB usbMouse = new Mouse(); // 多态写法
        // 参数是USB类型，我正好传递进去的就是USB鼠标
        computer.useDevice(usbMouse);

        // 创建一个USB键盘
        Keyboard keyboard = new Keyboard(); // 没有使用多态写法
        // 方法参数是USB类型，传递进去的是实现类对象
        computer.useDevice(keyboard); // 正确写法！也发生了向上转型(小范围到大范围自动向上转型了)
        // 使用子类对象，匿名对象，也可以
//        computer.useDevice(new Keyboard()); // 也是正确写法

        computer.powerOff();
        System.out.println("==================");

        method(10.0); // 正确写法，double --> double
        method(20); // 正确写法，int --> double
        int a = 30;
        method(a); // 正确写法，int --> double
    }

    public static void method(double num) {
        System.out.println(num);
    }

}

```

# day11【final、权限、内部类】 #

## final关键字用来修饰一个类 ##

```java
package cn.itcast.day11.demo01;

/*
当final关键字用来修饰一个类的时候，格式：
public final class 类名称 {
    // ...
}

含义：当前这个类不能有任何的子类。（太监类）
注意：一个类如果是final的，那么其中所有的成员方法都无法进行覆盖重写（因为没儿子。）
 */
public final class MyClass /*extends Object*/ {

    public void method() {
        System.out.println("方法执行！");
    }

}
package cn.itcast.day11.demo01;

// 不能使用一个final类来作为父类
public class MySubClass /*extends MyClass*/ {
}
```

## final关键字用来修饰一个方法 ##

```java
package cn.itcast.day11.demo01;

/*
当final关键字用来修饰一个方法的时候，这个方法就是最终方法，也就是不能被覆盖重写。
格式：
修饰符 final 返回值类型 方法名称(参数列表) {
    // 方法体
}

注意事项：
对于类、方法来说，abstract关键字和final关键字不能同时使用，因为矛盾。
 */
public abstract class Fu {

    public final void method() {
        System.out.println("父类方法执行！");
    }

    public abstract /*final*/ void methodAbs() ;

}
package cn.itcast.day11.demo01;

public class Zi extends Fu {
    @Override
    public void methodAbs() {

    }
    // 错误写法！不能覆盖重写父类当中final的方法
//    @Override
//    public void method() {
//        System.out.println("子类覆盖重写父类的方法！");
//    }
}

```

## final关键字修饰一个局部变量 ##

```java
package cn.itcast.day11.demo01;

/*
final关键字代表最终、不可改变的。

常见四种用法：
1. 可以用来修饰一个类
2. 可以用来修饰一个方法
3. 还可以用来修饰一个局部变量
4. 还可以用来修饰一个成员变量
 */
public class Demo01Final {

    public static void main(String[] args) {
        int num1 = 10;
        System.out.println(num1); // 10
        num1 = 20;
        System.out.println(num1); // 20

        // 一旦使用final用来修饰局部变量，那么这个变量就不能进行更改。
        // “一次赋值，终生不变”
        final int num2 = 200;
        System.out.println(num2); // 200

//        num2 = 250; // 错误写法！不能改变！
//        num2 = 200; // 错误写法！

        // 正确写法！只要保证有唯一一次赋值即可
        final int num3;
        num3 = 30;

        // 对于基本类型来说，不可变说的是变量当中的数据不可改变
        // 对于引用类型来说，不可变说的是变量当中的地址值不可改变
        Student stu1 = new Student("赵丽颖");
        System.out.println(stu1);
        System.out.println(stu1.getName()); // 赵丽颖
        stu1 = new Student("霍建华");
        System.out.println(stu1);
        System.out.println(stu1.getName()); // 霍建华
        System.out.println("===============");

        final Student stu2 = new Student("高圆圆");
        // 错误写法！final的引用类型变量，其中的地址不可改变
//        stu2 = new Student("赵又廷");
        System.out.println(stu2.getName()); // 高圆圆
        stu2.setName("高圆圆圆圆圆圆");
        System.out.println(stu2.getName()); // 高圆圆圆圆圆圆
    }

}
```

## final关键字修饰一个成员变量 ##

```java
package cn.itcast.day11.demo01;

/*
对于成员变量来说，如果使用final关键字修饰，那么这个变量也照样是不可变。

1. 由于成员变量具有默认值，所以用了final之后必须手动赋值，不会再给默认值了。
2. 对于final的成员变量，要么使用直接赋值，要么通过构造方法赋值。二者选其一。
3. 必须保证类当中所有重载的构造方法，都最终会对final的成员变量进行赋值。
 */
public class Person {

    private final String name/* = "鹿晗"*/;


    public Person() {
        name = "关晓彤";
    }

    public Person(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

//    public void setName(String name) {
//        this.name = name;
//    }
}
```

## 四种权限修饰符 ##

```java
package cn.itcast.day11.demo02;

/*
Java中有四种权限修饰符：
                      public  >   protected   >   (default)   >   private
同一个类（我自己）         YES         YES             YES             YES
同一个包（我邻居）         YES         YES             YES             NO
不同包子类（我儿子）       YES         YES             NO              NO
不同包非子类（陌生人）     YES         NO              NO              NO

注意事项：(default)并不是关键字“default”，而是根本不写。
 */
public class Demo01Main {
}

package cn.itcast.day11.demo02;

public class MyClass {

    public int num = 10;

    public void method() {
        System.out.println(num);
    }
}
package cn.itcast.day11.demo02;

public class MyAnother {

    public void anotherMethod() {
//        System.out.println(new MyClass().num);
    }
}
package cn.itcast.day11.demo02.sub;

import cn.itcast.day11.demo02.MyClass;

public class MySon extends MyClass {


    public void methodSon() {
//        System.out.println(super.num);
    }
}
package cn.itcast.day11.demo02.sub;

import cn.itcast.day11.demo02.MyClass;

public class Stranger {

    public void methodStrange() {
        System.out.println(new MyClass().num);
    }
}
```

## 成员内部类 ##

```java
package cn.itcast.day11.demo03;

public class Body { // 外部类

    public class Heart { // 成员内部类

        // 内部类的方法
        public void beat() {
            System.out.println("心脏跳动：蹦蹦蹦！");
            System.out.println("我叫：" + name); // 正确写法！
        }

    }

    // 外部类的成员变量
    private String name;

    // 外部类的方法
    public void methodBody() {
        System.out.println("外部类的方法");
        new Heart().beat();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
package cn.itcast.day11.demo03;

/*
如果一个事物的内部包含另一个事物，那么这就是一个类内部包含另一个类。
例如：身体和心脏的关系。又如：汽车和发动机的关系。

分类：
1. 成员内部类
2. 局部内部类（包含匿名内部类）

成员内部类的定义格式：
修饰符 class 外部类名称 {
    修饰符 class 内部类名称 {
        // ...
    }
    // ...
}

注意：内用外，随意访问；外用内，需要内部类对象。

==========================
如何使用成员内部类？有两种方式：
1. 间接方式：在外部类的方法当中，使用内部类；然后main只是调用外部类的方法。
2. 直接方式，公式：
类名称 对象名 = new 类名称();
【外部类名称.内部类名称 对象名 = new 外部类名称().new 内部类名称();】
 */
public class Demo01InnerClass {

    public static void main(String[] args) {
        Body body = new Body(); // 外部类的对象
        // 通过外部类的对象，调用外部类的方法，里面间接在使用内部类Heart
        body.methodBody();
        System.out.println("=====================");

        // 按照公式写：
        Body.Heart heart = new Body().new Heart();
        heart.beat();
    }
}
```

## 访问重名的内外类的成员变量和局部变量 ##

```java
package cn.itcast.day11.demo03;

// 如果出现了重名现象，那么格式是：外部类名称.this.外部类成员变量名
public class Outer {

    int num = 10; // 外部类的成员变量

    public class Inner /*extends Object*/ {

        int num = 20; // 内部类的成员变量

        public void methodInner() {
            int num = 30; // 内部类方法的局部变量
            System.out.println(num); // 局部变量，就近原则
            System.out.println(this.num); // 内部类的成员变量
            System.out.println(Outer.this.num); // 外部类的成员变量
        }
    }
}
package cn.itcast.day11.demo03;

public class Demo02InnerClass {

    public static void main(String[] args) {
        // 外部类名称.内部类名称 对象名 = new 外部类名称().new 内部类名称();
        Outer.Inner obj = new Outer().new Inner();
        obj.methodInner();
    }
}
```

## 局部内部类 ##

```java
package cn.itcast.day11.demo04;

/*
如果一个类是定义在一个方法内部的，那么这就是一个局部内部类。
“局部”：只有当前所属的方法才能使用它，出了这个方法外面就不能用了。

定义格式：
修饰符 class 外部类名称 {
    修饰符 返回值类型 外部类方法名称(参数列表) {
        class 局部内部类名称 {
            // ...
        }
    }
}

小节一下类的权限修饰符：
public > protected > (default) > private
定义一个类的时候，权限修饰符规则：
1. 外部类：public / (default)
2. 成员内部类：public / protected / (default) / private
3. 局部内部类：什么都不能写
 */
class Outer {

    public void methodOuter() {
        class Inner { // 局部内部类
            int num = 10;
            public void methodInner() {
                System.out.println(num); // 10
            }
        }

        Inner inner = new Inner();
        inner.methodInner();
    }

}
package cn.itcast.day11.demo04;

public class DemoMain {

    public static void main(String[] args) {
        Outer obj = new Outer();
        obj.methodOuter();
    }

}
package cn.itcast.day11.demo04;

/*
局部内部类，如果希望访问所在方法的局部变量，那么这个局部变量必须是【有效final的】。

备注：从Java 8+开始，只要局部变量事实不变，那么final关键字可以省略。

原因：
1. new出来的对象在堆内存当中。
2. 局部变量是跟着方法走的，在栈内存当中。
3. 方法运行结束之后，立刻出栈，局部变量就会立刻消失。
4. 但是new出来的对象会在堆当中持续存在，直到垃圾回收消失。
 */
public class MyOuter {

    public void methodOuter() {
        int num = 10; // 所在方法的局部变量  最好是 final int num 

        class MyInner {
            public void methodInner() {
                System.out.println(num);
            }
        }
    }
}
```

## 匿名内部类  ##

```java
package cn.itcast.day11.demo05;

public interface MyInterface {

    void method1(); // 抽象方法

    void method2();
}
package cn.itcast.day11.demo05;

/*
如果接口的实现类（或者是父类的子类）只需要使用唯一的一次，
那么这种情况下就可以省略掉该类的定义，而改为使用【匿名内部类】。

匿名内部类的定义格式：
接口名称 对象名 = new 接口名称() {
    // 覆盖重写所有抽象方法
};

对格式“new 接口名称() {...}”进行解析：
1. new代表创建对象的动作
2. 接口名称就是匿名内部类需要实现哪个接口
3. {...}这才是匿名内部类的内容

另外还要注意几点问题：
1. 匿名内部类，在【创建对象】的时候，只能使用唯一一次。
如果希望多次创建对象，而且类的内容一样的话，那么就需要使用单独定义的实现类了。
2. 匿名对象，在【调用方法】的时候，只能调用唯一一次。
如果希望同一个对象，调用多次方法，那么必须给对象起个名字。
3. 匿名内部类是省略了【实现类/子类名称】，但是匿名对象是省略了【对象名称】
强调：匿名内部类和匿名对象不是一回事！！！
 */
public class DemoMain {

    public static void main(String[] args) {
//        MyInterface obj = new MyInterfaceImpl();
//        obj.method();

//        MyInterface some = new MyInterface(); // 错误写法！

        // 使用匿名内部类，但不是匿名对象，对象名称就叫objA   省去了再次定义接口的实现类
        MyInterface objA = new MyInterface() {
            @Override
            public void method1() {
                System.out.println("匿名内部类实现了方法！111-A");
            }

            @Override
            public void method2() {
                System.out.println("匿名内部类实现了方法！222-A");
            }
        };
        objA.method1();
        objA.method2();
        System.out.println("=================");

        // 使用了匿名内部类，而且省略了对象名称，也是匿名对象
        new MyInterface() {
            @Override
            public void method1() {
                System.out.println("匿名内部类实现了方法！111-B");
            }

            @Override
            public void method2() {
                System.out.println("匿名内部类实现了方法！222-B");
            }
        }.method1();
        // 因为匿名对象无法调用第二次方法，所以需要再创建一个匿名内部类的匿名对象
        new MyInterface() {
            @Override
            public void method1() {
                System.out.println("匿名内部类实现了方法！111-B");
            }

            @Override
            public void method2() {
                System.out.println("匿名内部类实现了方法！222-B");
            }
        }.method2();
    }
}
```

## 类作为成员变量类型 ##

```java
package cn.itcast.day11.demo06;

// 游戏当中的英雄角色类
public class Hero {

    private String name; // 英雄的名字
    private int age; // 英雄的年龄
    private Weapon weapon; // 英雄的武器

    public Hero() {
    }

    public Hero(String name, int age, Weapon weapon) {
        this.name = name;
        this.age = age;
        this.weapon = weapon;
    }

    public void attack() {
        System.out.println("年龄为" + age + "的" + name + "用" + weapon.getCode() + "攻击敌方。");
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public Weapon getWeapon() {
        return weapon;
    }

    public void setWeapon(Weapon weapon) {
        this.weapon = weapon;
    }
}
package cn.itcast.day11.demo06;

public class Weapon {

    private String code; // 武器的代号

    public Weapon() {
    }

    public Weapon(String code) {
        this.code = code;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
}
package cn.itcast.day11.demo06;

public class DemoMain {

    public static void main(String[] args) {
        // 创建一个英雄角色
        Hero hero = new Hero();
        // 为英雄起一个名字，并且设置年龄
        hero.setName("盖伦");
        hero.setAge(20);

        // 创建一个武器对象
        Weapon weapon = new Weapon("AK-47");
        // 为英雄配备武器
        hero.setWeapon(weapon);

        // 年龄为20的盖伦用多兰剑攻击敌方。
        hero.attack();
    }
}
```

## 接口作为成员变量类型 ##

```java
package cn.itcast.day11.demo07;

public class Hero {

    private String name; // 英雄的名称
    private Skill skill; // 英雄的技能

    public Hero() {
    }

    public Hero(String name, Skill skill) {
        this.name = name;
        this.skill = skill;
    }

    public void attack() {
        System.out.println("我叫" + name + "，开始施放技能：");
        skill.use(); // 调用接口中的抽象方法
        System.out.println("施放技能完成。");
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Skill getSkill() {
        return skill;
    }

    public void setSkill(Skill skill) {
        this.skill = skill;
    }
}
package cn.itcast.day11.demo07;

public interface Skill {

    void use(); // 释放技能的抽象方法

}
package cn.itcast.day11.demo07;

public class DemoGame {

    public static void main(String[] args) {
        Hero hero = new Hero();
        hero.setName("艾希"); // 设置英雄的名称

        // 设置英雄技能
//        hero.setSkill(new SkillImpl()); // 使用单独定义的实现类

        // 还可以改成使用匿名内部类
//        Skill skill = new Skill() {
//            @Override
//            public void use() {
//                System.out.println("Pia~pia~pia~");
//            }
//        };
//        hero.setSkill(skill);

        // 进一步简化，同时使用匿名内部类和匿名对象
        hero.setSkill(new Skill() {
            @Override
            public void use() {
                System.out.println("Biu~Pia~Biu~Pia~");
            }
        });

        hero.attack();
    }
}
```

## 接口作为方法的参数/返回值 ##

```java
package cn.itcast.day11.demo07;

import java.util.ArrayList;
import java.util.List;

/*
java.util.List正是ArrayList所实现的接口。
 */
public class DemoInterface {

    public static void main(String[] args) {
        // 左边是接口名称，右边是实现类名称，这就是多态写法
        List<String> list = new ArrayList<>();

        List<String> result = addNames(list);
        for (int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));
        }
    }

    public static List<String> addNames(List<String> list) {
        list.add("迪丽热巴");
        list.add("古力娜扎");
        list.add("玛尔扎哈");
        list.add("沙扬娜拉");
        return list;
    }
}
```

## 发红包 均分/随机 ##

```java
package cn.itcast.day11.demo08;

import cn.itcast.day11.red.RedPacketFrame;

public class MyRed extends RedPacketFrame {
    /**
     * 构造方法：生成红包界面。
     *
     * @param title 界面的标题
     */
    public MyRed(String title) {
        super(title);
    }
}
package cn.itcast.day11.demo08;

import cn.itcast.day11.red.OpenMode;

/*
场景说明：
    红包发出去之后，所有人都有红包，大家抢完了之后，最后一个红包给群主自己。
大多数代码都是现成的，我们需要做的就是填空题。
我们自己要做的事情有：
    1. 设置一下程序的标题，通过构造方法的字符串参数
    2. 设置群主名称
    3. 设置分发策略：平均，还是随机？

红包分发的策略：
    1. 普通红包（平均）：totalMoney / totalCount，余数放在最后一个红包当中。
    2. 手气红包（随机）：最少1分钱，最多不超过平均数的2倍。应该越发越少。
Bootstrap启动
 */
public class Bootstrap {

    public static void main(String[] args) {
        MyRed red = new MyRed("传智播客双元课程");
        // 设置群主名称
        red.setOwnerName("王思聪");

        // 普通红包
//        OpenMode normal = new NormalMode();
//        red.setOpenWay(normal);

        // 手气红包
        OpenMode random = new RandomMode();
        red.setOpenWay(random);
    }

}
package cn.itcast.day11.demo08;

import cn.itcast.day11.red.OpenMode;

import java.util.ArrayList;

public class NormalMode implements OpenMode {
    @Override
    public ArrayList<Integer> divide(final int totalMoney, final int totalCount) {
        ArrayList<Integer> list = new ArrayList<>();

        int avg = totalMoney / totalCount; // 平均值
        int mod = totalMoney % totalCount; // 余数，模，零头

        // 注意totalCount - 1代表，最后一个先留着
        for (int i = 0; i < totalCount - 1; i++) {
            list.add(avg);
        }

        // 有零头，需要放在最后一个红包当中
        list.add(avg + mod);

        return list;
    }
}
package cn.itcast.day11.demo08;

import cn.itcast.day11.red.OpenMode;

import java.util.ArrayList;
import java.util.Random;

public class RandomMode implements OpenMode {
    @Override
    public ArrayList<Integer> divide(final int totalMoney, final int totalCount) {
        ArrayList<Integer> list = new ArrayList<>();

        // 随机分配，有可能多，有可能少。
        // 最少1分钱，最多不超过“剩下金额平均数的2倍”
        // 第一次发红包，随机范围是0.01元~6.66元
        // 第一次发完之后，剩下的至少是3.34元。
        // 此时还需要再发2个红包
        // 此时的再发范围应该是0.01元~3.34元（取不到右边，剩下0.01）

        // 总结一下，范围的【公式】是：1 + random.nextInt(leftMoney / leftCount * 2);
        Random r = new Random(); // 首先创建一个随机数生成器
        // totalMoney是总金额，totalCount是总份数，不变
        // 额外定义两个变量，分别代表剩下多少钱，剩下多少份
        int leftMoney = totalMoney;
        int leftCount = totalCount;

        // 随机发前n-1个，最后一个不需要随机
        for (int i = 0; i < totalCount - 1; i++) {
            // 按照公式生成随机金额
            int money = r.nextInt(leftMoney / leftCount * 2) + 1;
            list.add(money); // 将一个随机红包放入集合
            leftMoney -= money; // 剩下的金额越发越少
            leftCount--; // 剩下还应该再发的红包个数，递减
        }

        // 最后一个红包不需要随机，直接放进去就得了
        list.add(leftMoney);

        return list;
    }
}
```

