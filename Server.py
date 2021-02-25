# First HTTP Server
import socket;

# Define the host as a tuple
HOST, PORT = "", 8080;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
s.bind((HOST, PORT));
s.listen(True);

print("Serving HTTP on port %s...." % PORT);

while True:
    client_connection, client_address = s.accept();
    request = client_connection.recv(1024);  # Buffer Size
    print(request.decode("utf-8"));  # Display the HTTP request
    # Define the Web response message
    http_reponse = """\

HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

<html>
<head>
<title>Skyscraper</title>
</head>

<body>
<h1>Mohammed Shaheer    PI2004K</h1>
<img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw8ODw8PDw8NDg8NDw0NEA0PDQ8NDQ4PFREWFhURFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OFRAQFy0fHx0uLS4tLS0tKy0tLS0rKy0tLS0tLSstLS0tLS0tKy0tLS0rLS0rLS0tLS0tLS0tLS0tLf/AABEIASkAqgMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAAAAQMEBQIGB//EAEMQAAEDAwEEBggDBgILAAAAAAEAAhEDEiEEBTFBUQYTIiNhcTIzQoGRobHBFHJzQ1KywtHwYqIVJGNkgoOSo7Ph8f/EABkBAQEBAQEBAAAAAAAAAAAAAAABAgMEBf/EACYRAQEAAgEEAgEEAwAAAAAAAAABAhEDEiExMhNBIyIzcZFCUWH/2gAMAwEAAhEDEQA/AKaSEL6jwBJCSASTSQIoQUlAJIQgRSXTWkkACSSABzJXKKSSEkAUISQCSEIoK5TSQIoQkg0UkIVZJJNJAJIQopJJlJAJIQgn0PrqX6lP+IKsruyWXaig3nWoj/OFTcPdHA71PtfpyUkJKoCkhCAKSCkihJCEAkgpINFIppKskkmkgEkIUUkk0kAkhJBq9GaJqazTAcKrH55NNx+iztX6yp+d/wDEVe2ESK0jBFKuQeI7t2Vn1zLnfmd9Vie9/hv/ABRpISW2AkgoRSQhIoBJCEAkhCDQSQhVkkk0kUJISUAUk0kCQhJBqbBHeOPBtGsTid7bR8yFnan03ea0djehqD/gb9Ss/WDvHef2XKX8l/h0s/REKSCkurASQkUAkmkgEkJIBCEINBIoSVQJIQoEhCRQCSEkAhJCDX2L6vU/kb/Ms7Xesf5j6L0PRbTB1DVui4mk4AROWxEePaWBtFsVX8PRxx9ELhjfy12s/HFUrlMrld3ISkhKUAUJIQCEJIBCClKDQKEJKoEkJKASQhAkpQkgEwkgIr23QUd1V8z4e1TXnukQ7bTzDgTvOI4rX2dVdR0TXMNpqsrkuETiocj/AKW/BY+33T1LuLmvJ5elGPgvJj+7/b0ZftsgpFBXK9bzhCEkAkhCAQkhAISQitBJNJGSQhJAJFBSKBIQkgEwkreyaQfXpNcJaajQRzE5S3U2s716inRI0FCR2hR1TiMSAajoJHvHxWV0j0pbS0zz7TarYjk+Z+a9u/TaQ0nkuc0GnVIfukXAOgRjevMdLtU0abT6eb3U3VHsqxF9EmAT4yCPcvBx5b5JXqyn6HjiuSuiuV73lJJNJAJIQgEimkgEkIRWghCSMhIoQgSRTXKASQkihWtnOirTPJwVVT6L1jPNTLxVx8x7PXVCKFOMTR1In/jZhec23UupaXmGVR7r5H3W9tQ91RA39VqAIGfWM8Fj9JqNjmMtAa2kwtgAWktJxnIkcV4OO6ylerKbxrz5KSEivoPISSaSAQhCBJJpIBCEIrQSTSVZJIppIEkmkopJFMpIBTaL1jPNQqbResZO64KZeKs8x6raD+703HsVcbv2gzKp9Kz3g8aNE/5SpdXqmVG6djT6LH78NPaJMHjgFUukuqa9w9nu6IEi0u7O/wCa+dL3eu+Hn0imkV9J4ySTSQCEJIBCEIpITQgvpJoVZclIppIEkmkVFIpJpIEptK2XtHNwUK2ujOiZVqtL5hrhjh/7Wc7JjVxm7GltKm2zSCItpvgjBE1Ij5kKl0uaHObjIpUSDyIAhT6ytd1IgQzrWADwrxOVX6TntN/Rp/Rq8GPl6r4edQhC+i8hJJoQJCaSASThEIpIThEIL6S6KSqOUl0QuYRCSTQoOSkulygS9B0TMPH593uCwFu9F/THDtb+WFz5vV04/ZzWd2mRgzWPu65c9JMubvjqaXu7LP79y5rb2cu/zxPff38Vo631VQx2h1AByI7vPuXjnl6K8imu6pkzj4AT8FyvfLubeWzVcoTQqhIhOEQgSS6hEIrlELuEoVF8hKF3CUIjghckKSEoQRwkQuyEoRHBCULshKEHELa6N+mBEkuOOeAseFr7AqODoBgE5M53Llzerpx+yCo7NPn38t5d6VoauTRqRcR3AkNJnuzjHFZDqr2inJD2nrw2TJb2yJg4+Cv69r303lzs9xzO6njevF3enswnfDw5eCULoknJMkxn3IhfQw9Y8uXmuYRC6hELTLmEQuoThBxCIXcIhBzCIXcIhBdIShSQlCCMhKFJCIQRQlCkhKEEZCUKQhK1ERwtfZwbStcbjc8MwIyfmsy1XyTZSzg16Z+a4c97SOvFO6hUcLaM49dHD9qVpas91U3/ALIHh+zKzKpxS5RW4f7YrQ1ZJY/zpjx9DwXmd2O3cPIfRdQnTGB5BdQvdh6x5cvNcQiFJalC0y4hELu1O1BHCIUlqIRXEIhdwiEF61KFLalaiooShS2otREMJQpS1K1BFaiFLalaiIgFYcOxSPDrmYwuLVJVbDaJJAmq0xc2cb8zHHmvPz3w7cX2zqu6nO6K0c/XLWbN2f36QI3AjqzvWVUBIp7z2ah7Iu31uNq1gw3CS0HrKe94IPd/4Z+i8+47aZbiS944CIG+MlMNSpODnvgtO7dPM8wFPavZw+sebk9kVqLVLai1dWEVqLVLanaiorUWqW1FqCK1FqmtRaoLpalap7UWLO1V7UrVYtSsV2K9qVqsWJWKor2otVixKxEVwyeEqtXpm2lMyKrcRDhkYncrtVoETxdzjgVTqOJqEAudFdoBJkARuXm5ru6d+Odts5zXN6u3EsqDPawap5DC1g0l+ZnrKeCcer5iFm6gCKU/uv5Y7wrWjtZJI61mf+X4LjqOihpaUVKm7cN08yrlii0bR1lSOTc75y5XLF6+L1efk9kNqLFOGJ2Lqwr2otVixFiCCxFinsRYoqC1OxTWLklv7zfiFNmmhYlYrNiLFy26aVbErFaLEdSYmMbpV6pE6dqtiVitWJWLW00rWJWKzYjq06k0o6hu7z+xWY/0yZAArjJE+z4q5UfGoe1zoaG0oGAJN2VSrV23OkO9edzxnsiOC8uee7Xoxx1IqVT6HgHcx7YP3WqAbsRHWtwf0hlZIc027x2XHgfaaIWyx1O/l3wntCPVDhCxtrSt1hBpxIksBwIOeOPErTsWXVqiaNoBk0pzmZGFu2L0cN7Vx5Yr9WixWbFk7e1j6FhYWi66Q4NIMbt5H1XTLk6ZtjHHd0u2KLUVWUxL3BoJAk8yY+6y9Pt53tsBH7zZb9cfNVNs1Ovh03U8tjcRPAjyG8eK5/PL4b+Kzy9JYixRbHqGpQpuOXAWOPNzcT74n3q7YukyY08/t7Uupmm1pIDg4mPMAfdYXWHmtjpQzvaX5R/GsZtEwPIcVzy710naPpdqVq6lErj1t9Li1Uds1XN09cA4aKZA5FzgCceC0lkdInW6bUO3+rHLdlY5Mtxvjx1Umxtoh2mp13g1ZDgR2WkuBLcxjgnptYJDKnZc5xDT7J4hpP7wBAPCdyytk42dpxzqP/8AM8qptIOcxzGvpsLzgulstDicETxs/sKfJZYvRLLts6LVPq6usHEGKNI7hwAAz5LWsXn9j1A3V1b30+3SotabgA5w3gc9y3a+pawAkiCQ3Enny8lvjz1ixnjbXm9Y9zda8YyaIG84Nv8AUqOsTLh/vDhy/YgqfaBY8moCBWa9hJHGJjhwA4LPlrwaubDqHVZJMx1QZuwd6x1eW9IK8CJI3O3xzC26MkgjjVYf+yF52vTkUyJi1oJ7XA/2Vs6OoypUaGPa6HscbXTupBp4802aRVtSGv07c3PqUQMGIuaCV6yxeU02ibVqU3Ev7mHAE4uDrhgj/Cdy29nbScbGVhFR+QQ18ObGCTEA4PEcFvDk0xlhtoWLx+36kkmSO08RMHAjmPuvYGs0e034heL247f+pUx2uZU5c96Xjx1tQpN4xwOYP1t+6lYTaY3OLQfHjmJ5c1Tov8Ofsx/L91bp1QRHGQc8oPGTzC5y927Oz03RkdyRye76Ba1q8roNt09LSdfEXXTJgDA3+a16G3aLqfWOcAIccZ7ILsxv3Nd8DyXackcuiqPSWmetonha4eE3ArOp6NxaDLMgH0s7lo7RrHUVKbA+mWtJsyB6QBg8Z/omzZ9QAC+ngAek7+ixefH7rXw5fUTv6TUG1GUgS59USwNcwy69rbMHB7QKt6zaT6dJ1QUahtDj2hYABvJ4gLzLzs0PeD1Yc0Ui6RUbnrbCTPuWg40KlN50wo1nUi0OgB7mSMTdncud3/tuZT7jij0seZJZSMQ2GudIePSB8l3t7b9CrQdSp33VIJL29gQIInxGVG3TgjtUaEgAyacekfDiuNp6XqmX9Rpoa+0G04JaT8cLndtTKM7S66rTpPpE4AxJltKCSSMcZI96wtqVOttsc0wXzgtz2YElgn5r1LKriC4UmwM3X1RP+ZZ+p1tsX0KZuLj6ysSd2T2le6XKMLSueyHSGlhcR3lhqQDlsZ/+L0p2kTTbNR24AgOe5wInkJ4qr+PYQO4AMOgCpUdid0EnfHzVyrSaRc7Tty076tUmLTjfyV3kbijW1lxZUa82i24y4TDYkiJOVWGoeSAHOtNRpw1zWxcDmcLbp6jTU22O0dNxMA5mZzEnK7O1dDgfg6cElttrSA7Hh5BN07PRt6TaFtIsL39YN8aeu4ZkSCGwRg5C8ZX1LvxIewuDHslrgzN10Z4jcvTt09MMNT8EyyG9kNpugRO7hvVT/SejDg06Zk27uqpYE/LKm6dmNV19gZaXS7rTItpkkQ2N/ArvT7Tl7XPZWAIeR6q0jM+14rbq7T0jYLqDO1JB/D0jAB8vFT09t0LbWANkGG9QA3HIQm6vZ5LU1XOAPWOaHEOGWPtzk2F0E4+Si2yajXtpgN1BcabhUptaWvBbIfGTx4L2n+ntNABySAM0mmTu3QrB29TpODOuYwuIDQQAJ3CD8E7m48MzSvIzp68gGSaLqclruZgZCdOjVgllGq6WgNJ9kzMEHxXt9XtUkBrq1B7RMC5rreJxnwVSntNhkl7ASW5a8tmHTy5QsdP/AFeqPOUti6p4N1EQcxF3ZmYOIHD4KXVbH11pDaAqtuebbKL8FhaQQ4gbncDx960NXXquLSzV1Wgl4cGtDy8cAS7AA+aezqlRoM6mtV7TO09lNjoBNzQLogzywtdJvFHoKVUVW/6r1bnGm0C+i0uhgaX4PEic8zv416O0GUmtpvq9um1tN8kk3NEGTxyFsAB83MdvbHbE32kXYcZxw8F5vUdG9O973Oe8Oc5znABkSTJS4S+Vmevt5K4PJFPTuhxDi2XPLogiSAC4Yle26At1IdqJotpNf1bzLQLnEukmSTuVXZHoNXrujvo1PNv0XeeXgvNbdNSnT5hpPgIVPbGna+iQR+0B5eyQtNqrbS9UfzfYplPDMzvdmHZoNGk1vJpIPHsnisHXbMBIuxBt95K9jT9XS8m/RZO1fSb7v5lmzuuOVs7sbQbJYarpMikQPOQVs19O0gADwPlCr7P9ZX/M37q8VuY7h1WMbVaUYcQCQQG+8QqDtAwgGIde74jK1dT7P52qod7f1Kv0KzGrlYtO229tJrAAZAO+cGVl0tLNaajQc2iHQd07ih+5v6bFe1G4fnH8CaWclvlDphSfa12LQ6LmjIPuVlgpucx1MsiBJtGHRkfNZlL06X5fuFNs70B5n7Kybrp9Ln4GmXyYcJJgMMLH2m7tEWMDWvIBJAIyVv0ePuWFtH0j+o9XLHWkl8oKeon2ASQczvnB+SlyWx1ZiMQdxOFQb6Y96v6XefcsTGUyukuipuJhocLcxv8Acr34Auabi4GcY8FLodzvMLXG5dPjjn8nZjU3hgpHMFzBkQZDIKqVNGwuJvGSTx5rW2v6DP1D9AsZ+8+ZXO46vl1xylmtP//Z" alt="Skyscraper">

</head>
<body>
"""
    client_connection.sendall(bytes(http_reponse, "utf-8"));
    client_connection.close();
