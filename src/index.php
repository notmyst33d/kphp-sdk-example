<!doctype html>
<html>
    <head>
        <title>KPHP SDK Example</title>
    </head>
    <body>
        <h1>KPHP SDK Example</h1>
        <?php
        require("time.php");
        print("<strong>This webpage is served by " . PHP_SAPI . "</strong><br>");
        print('It is currently <span id="time">' . omskTime() . "</span> in Omsk<br>");
        ?>
        <script>
            async function updateTime() {
                document.getElementById("time").innerText = await (await fetch("/time.php")).text();
                setTimeout(updateTime, 1000);
            }
            setTimeout(updateTime, 1000);
        </script>
    </body>
</html>
