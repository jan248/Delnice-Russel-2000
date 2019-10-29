import orodja
import re

url_link = "C:\\Users\\jansk\\Documents\\GitHub\\Delnice-Russel-2000\\stran\\page_source"

def pridobi_stran(url):
    orodja.shrani_spletno_stran(url,url_link, False)

def pridobi_podatke():
    vsebina = orodja.vsebina_datoteke(url_link)

    reg = (
        r'\s*<tr id="table_..?_row_..?">\n' #start
        r'\s*<td style="">(?P<oznaka_na_borzi>.*)</td>\n'
        r'\s*<td style="">(?P<cena_delnice>.*)</td>\n'
        r'\s*<td style="">(?P<dividendna_donosnost>.*)</td>\n'
        r'\s*<td style="">(?P<trzna_kapitalizacija>.*)</td>\n'
        r'\s*<td style="">(?P<pe_razmerje>.*)</td>\n'
        r'\s*<td style="">(?P<div_na_prihodke>.*)</td>\n'
    )

    final = []

    for match in re.finditer(reg, vsebina):
        final.append(match.groupdict())
    return final


def main():
    pridobi_stran("https://www.suredividend.com/russell-2000-stocks/")
    final = pridobi_podatke()

    orodja.zapisi_json(final, "C:\\Users\\jansk\\Documents\\GitHub\\Delnice-Russel-2000\\stran\\jsonfile" )
    orodja.zapisi_csv(final, final[0].keys(), "C:\\Users\\jansk\\Documents\\GitHub\\Delnice-Russel-2000\\stran\\csv_file")

if __name__== "__main__":
  main()
