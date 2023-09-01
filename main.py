import json

rawResult = "{\"service\":\"Private person\",\"version\":1,\"requestID\":1693392409,\"result\":{\"endpoint\":\"RR437\",\"response\":{\"r:report\":{\"prod:RR437Response\":{\"request\":{\"Isikukood\":\"49310052510\"},\"response\":{\"Isik\":{\"Isik.Isikukood\":\"49310052510\",\"Isik.Eesnimi\":\"IRINA\",\"Isik.Perenimi\":\"LOSSEVA\",\"Isik.Sugu\":\"NAINE\",\"Isik.Synniaeg\":\"1993-10-05\",\"Isik.IsikuStaatus\":\"E\",\"Isik.KirjeStaatus\":\"K\",\"Isik.Kodakondsus\":\"0\",\"Elukoht\":{\"Elukoht.RiigiKood\":\"EST\",\"Elukoht.RiigiNimi\":\"Eesti\",\"Elukoht.MaakonnaKood\":\"45\",\"Elukoht.MaakonnaNimi\":\"Ida-Viru maakond\",\"Elukoht.VallaKood\":\"321\",\"Elukoht.VallaNimi\":\"Kohtla-Järve linn\",\"Elukoht.AsulaKood\":\"120\",\"Elukoht.AsulaNimi\":\"Ahtme linnaosa\",\"Elukoht.TanavaNimi\":\"Puru tee\",\"Elukoht.Majanr\":\"80\",\"Elukoht.Korternr\":\"6\",\"Elukoht.Postiindeks\":\"31024\",\"Elukoht.Alates\":\"2022-07-01\",\"Elukoht.AadressTekstina\":\"Eesti, Ida-Viru maakond, Kohtla-Järve linn, Ahtme linnaosa, Puru tee 80-6\",\"Elukoht.AdsAdrID\":\"2769629\",\"Elukoht.AdsOid\":\"ER01395247\"},\"ElamisDokumendiTunnus\":\"2\",\"ElamisDokument\":\"ELAMISÕIGUS\",\"LasteArv\":\"3\",\"Dokumendid\":{\"Dokument\":[{\"Dokument.Liik\":\"ELAMISLUBA\",\"Dokument.Number\":\"TE334973847\",\"Dokument.ValjaAntud\":\"1995-10-13\",\"Dokument.KehtibKuni\":\"2000-10-14\",\"Dokument.Staatus\":\"KEHTETU\",\"Dokument.Asutus\":\"KODAKONDSUS- JA MIGRATSIOONIOSAKOND - PPA\"},{\"Dokument.Liik\":\"ELAMISLUBA\",\"Dokument.Number\":\"EL33D992970\",\"Dokument.ValjaAntud\":\"1999-10-06\",\"Dokument.KehtibKuni\":\"2014-02-10\",\"Dokument.Staatus\":\"KEHTETU\",\"Dokument.Asutus\":\"KODAKONDSUS- JA MIGRATSIOONIOSAKOND - PPA\"},{\"Dokument.Liik\":\"VÄLISMAALASE PASS\",\"Dokument.Number\":\"V0439089\",\"Dokument.ValjaAntud\":\"2003-10-28\",\"Dokument.KehtibKuni\":\"2008-08-22\",\"Dokument.Staatus\":\"KEHTETU\",\"Dokument.Asutus\":\"KODAKONDSUS- JA MIGRATSIOONIOSAKOND - PPA\"},{\"Dokument.Liik\":\"ISIKUTUNNISTUS\",\"Dokument.Number\":\"B0045726\",\"Dokument.ValjaAntud\":\"2003-10-28\",\"Dokument.KehtibKuni\":\"2008-08-22\",\"Dokument.Staatus\":\"KEHTETU\",\"Dokument.Asutus\":\"KODAKONDSUS- JA MIGRATSIOONIOSAKOND - PPA\"},{\"Dokument.Liik\":\"VÄLISMAALASE PASS\",\"Dokument.Number\":\"VB0004964\",\"Dokument.ValjaAntud\":\"2008-07-24\",\"Dokument.KehtibKuni\":\"2013-07-25\",\"Dokument.Staatus\":\"KEHTETU\",\"Dokument.Asutus\":\"KODAKONDSUS- JA MIGRATSIOONIOSAKOND - PPA\"},{\"Dokument.Liik\":\"ISIKUTUNNISTUS\",\"Dokument.Number\":\"P0072707\",\"Dokument.ValjaAntud\":\"2008-07-24\",\"Dokument.KehtibKuni\":\"2013-07-25\",\"Dokument.Staatus\":\"KEHTETU\",\"Dokument.Asutus\":\"KODAKONDSUS- JA MIGRATSIOONIOSAKOND - PPA\"},{\"Dokument.Liik\":\"ELAMISÕIGUS\",\"Dokument.Number\":\"1027595982/AO\",\"Dokument.ValjaAntud\":\"2014-02-20\",\"Dokument.Staatus\":\"KEHTIV\",\"Dokument.Asutus\":\"POLITSEI- JA PIIRIVALVEAMET\"},{\"Dokument.Liik\":\"VÄLISRIIGI PASS\",\"Dokument.Number\":\"PE2003293\",\"Dokument.ValjaAntud\":\"2013-06-07\",\"Dokument.KehtibKuni\":\"2023-06-06\",\"Dokument.Staatus\":\"KEHTETU\",\"Dokument.Asutus\":\"IIRIMAA  ASUTUSED\"},{\"Dokument.Liik\":\"ISIKUTUNNISTUS\",\"Dokument.Number\":\"EA0029396\",\"Dokument.ValjaAntud\":\"2014-02-20\",\"Dokument.KehtibKuni\":\"2015-09-25\",\"Dokument.Staatus\":\"KEHTETU\",\"Dokument.Asutus\":\"POLITSEI- JA PIIRIVALVEAMET\"},{\"Dokument.Liik\":\"ISIKUTUNNISTUS\",\"Dokument.Number\":\"EA0044330\",\"Dokument.ValjaAntud\":\"2015-09-11\",\"Dokument.KehtibKuni\":\"2020-09-12\",\"Dokument.Staatus\":\"KEHTETU\",\"Dokument.Asutus\":\"POLITSEI- JA PIIRIVALVEAMET\"},{\"Dokument.Liik\":\"JUHILUBA\",\"Dokument.Number\":\"EV584822\",\"Dokument.ValjaAntud\":\"2020-09-08\",\"Dokument.KehtibKuni\":\"2030-08-20\",\"Dokument.Staatus\":\"KEHTIV\",\"Dokument.Asutus\":\"TRANSPORDIAMET\"},{\"Dokument.Liik\":\"ISIKUTUNNISTUS\",\"Dokument.Number\":\"EB0520704\",\"Dokument.ValjaAntud\":\"2020-09-01\",\"Dokument.KehtibKuni\":\"2025-09-02\",\"Dokument.Staatus\":\"KEHTIV\",\"Dokument.Asutus\":\"POLITSEI- JA PIIRIVALVEAMET\"}]},\"AktiivsedOigused\":null,\"Sallivused\":null,\"Kontakt\":null,\"KeeludJaKasitlused\":null,\"Karistusregister\":null}}}}}}}"
parsedResult = json.loads(rawResult)


def get_nested_key(data, keys):
    for key in keys:
        if key in data:
            data = data[key]
        else:
            return None
    return data


KEHTIV = "KEHTIV"
DOCUMENTS_OF_INTEREST = ["ELAMISLUBA", "ELAMISÕIGUS", "ELAMISLOAKAART", "PASS", "ISIKUTUNNISTUS"]

first_name = get_nested_key(parsedResult, ["result", "response", "r:report", "prod:RR437Response", "response", "Isik",
                                           "Isik.Eesnimi"])
last_name = get_nested_key(parsedResult, ["result", "response", "r:report", "prod:RR437Response", "response", "Isik",
                                          "Isik.Perenimi"])

documents = get_nested_key(parsedResult,
                           ["result", "response", "r:report", "prod:RR437Response", "response", "Isik", "Dokumendid",
                            "Dokument"])

print(f"{first_name} {last_name}:")

for doc in documents:
    doc_type = doc.get("Dokument.Liik")
    if any(interest in doc_type for interest in DOCUMENTS_OF_INTEREST) and doc.get("Dokument.Staatus") == KEHTIV:
        doc_number = doc["Dokument.Number"]
        doc_status = doc["Dokument.Staatus"]
        doc_va = doc["Dokument.ValjaAntud"]

        if "Dokument.KehtibKuni" in doc:
            doc_kk = doc["Dokument.KehtibKuni"]
            print(f"{doc_type} {doc_status} nr: {doc_number} kehtib kuni {doc_kk}")
        else:
            print(f"{doc_type} {doc_status} nr: {doc_number}")