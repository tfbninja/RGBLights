# from https://pypi.org/project/wolframalpha/
import wolframalpha
app_id = 'V9U4JW-T8YXU6Y5QP'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)

const = 0.68
neededResult = 235/255.0
res = client.query('integral(max(0,sin(x) + " + const + "),0,2*pi) / integral(abs(sin(x) + " + const + "),0,2*pi)')
print(next(res.results).plainText)
