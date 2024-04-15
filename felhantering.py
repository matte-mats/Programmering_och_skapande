a = 10
try:
    c = a/b
except (ZeroDivisionError, NameError):
    print("Något gick fel vid divisionen!")
print("Här fortsätter programmet")

while True:
    try:
        x = int(input("Ange ett heltal: "))
        break
    except:
        print("Fel vid inmatning. Försök igen...")
print("ok!")

try:
    # Block att "försöka"
    x = int(input("Ange ett heltal: "))
    result = 10 / x
except ValueError:
    # Block för att hantera undantaget ValueError (felaktig typ av inmatning)
    print("Felaktig inmatning. Ange ett heltal.")
except ZeroDivisionError:
    # Block för att hantera undantaget ZeroDivisionError (division med noll)
    print("Division med noll är inte tillåten.")
else:
    # Block om allt gick bra (ingen undantag inträffade)
    print("Resultatet är:", result)
finally:
    # Block som alltid utförs, oavsett om undantag inträffade eller inte
    print("Undantagshantering avslutad.")
