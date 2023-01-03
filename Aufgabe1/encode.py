from collections import Counter
import re;
msg = "Knk  ?TURKqkK T;?TUKqwTKqwhrKxU?TcKTwUTUKEsxvKxUHKqhr wTlTUKTwUaKjxUKnsc.qKqhrkUKHTcKHcw??TKOkc;TURKHsqqKqwTKwrcTqKps?TcqKWsxqKtTc sqqTUKrs??TUaK\"wTKlwU;TUKnwTHTcKsUKDxK;TrTURKs!TcKqwTK;TcwT?TUKwvvTcK?wTlTcKwUKHTUKBs HRKxUHKnTUUKUwhr?K!s HKWw lTKmsvRKvxqq?TUKqwTKtTcqhrvshr?TUaKz qKTqKOw??s;KnscRKqsrTUKqwTKTwUKqhrkTUTqRKqhrUTTnTwqqTqKpkT;T TwUKsxlKTwUTvKzq?Kqw?DTURKHsqKqsU;KqkKqhrkTURKHsqqKqwTKq?TrTUK! wT!TUKxUHKwrvKDxrkTc?TUaKMUHKs qKTqKlTc?w;KnscRKqhrnsU;KTqKqTwUTKA xT;T KxUHKl k;KtkcKwrUTUKrTcRKxUHKqwTK;wU;TUKwrvKUshrRK!wqKqwTKDxKTwUTvKWsTxqhrTUK;T sU;?TURKsxlKHTqqTUK-shrKTqKqwhrKqT?D?TRKxUHKs qKqwTK;sUDKUsrTKrTcsUmsvTURKqkKqsrTUKqwTRKHsqqKHsqKWsTxq TwUKsxqKEck?K;T!sx?KnscKxUHKvw?KVxhrTUK;THThm?JKs!TcKHwTKATUq?TcKnscTUKtkUKrT  TvKQxhmTcaK'-sKnk  TUKnwcKxUqKHcsUvshrTUR'KqdcshrKWsTUqT RK'xUHKTwUTK;TqT;UT?TKOsr DTw?Krs ?TUaKehrKnw  KTwUK\"?xThmKtkvK-shrKTqqTURKIcT?T RKHxKmsUUq?KtkvKATUq?TcKTqqTURKHsqKqhrvThm?KqxTqqa'KWsTUqT KcTwhr?TKwUKHwTKWkTrTKxUHK!cshrKqwhrKTwUKnTUw;KtkvK-shrKs!RKxvKDxKtTcqxhrTURKnwTKTqKqhrvThm?TRKxUHKIcT?T Kq?T  ?TKqwhrKsUKHwTK\"hrTw!TUKxUHKmUxddTc?TKHscsUaK-sKcwTlKTwUTKlTwUTK\"?wvvTKsxqKHTcK\"?x!TKrTcsxqbK'VUxddTcRKmUxddTcRKVUTwqhrTURKBTcKmUxddTc?KsUKvTwUTvKWsTxqhrTU,'K-wTKVwUHTcKsU?nkc?T?TUbK'-TcKBwUHRKHTcKBwUHRKHsqKrwvv wqhrTKVwUHR'KxUHKsqqTUKnTw?TcRKkrUTKqwhrKwccTKvshrTUKDxK sqqTUaKWsTUqT RKHTvKHsqK-shrKqTrcK;x?KqhrvThm?TRKcwqqKqwhrKTwUK;ckqqTqK\"?xThmKHstkUKrTcxU?TcRKxUHKIcT?T Kq?wTqqKTwUTK;sUDTKcxUHTKATUq?TcqhrTw!TKrTcsxqRKqT?D?TKqwhrKUwTHTcKxUHK?s?KqwhrKnkr KHsvw?aK-sK;wU;KsxlKTwUvs KHwTKZxTcTKsxlRKxUHKTwUTKq?TwUs ?TKAcsxRKHwTKqwhrKsxlKTwUTKVcxThmTKq?xT?D?TRKmsvKrTcsxq;Tqhr whrTUaKWsTUqT KxUHKIcT?T KTcqhrcsmTUKqkK;Tns ?w;RKHsqqKqwTKls  TUK wTqqTURKnsqKqwTKwUKHTUKWsTUHTUKrwT ?TUaK-wTKz ?TKs!TcKnshmT ?TKvw?KHTvKVkdlTKxUHKqdcshrbK'FwRKwrcK wT!TUKVwUHTcRKnTcKrs?KTxhrKrwTcrTcK;T!cshr?,KVkvv?KUxcKrTcTwUKxUHK! Tw!?K!TwKvwcRKTqK;TqhrwTr?KTxhrKmTwUK:TwHa'K\"wTKlsqq?TK!TwHTKsUKHTcKWsUHKxUHKlxTrc?TKqwTKwUKwrcKWsTxqhrTUaK-sKnscHKTwUK;x?TqKFqqTUKsxl;T?cs;TURKOw hrKxUHKClsUUmxhrTUKvw?KQxhmTcRKsTdlT KxUHKjxTqqTaKWTcUshrKnxcHTUKDnTwKqhrkTUTKET?? TwUKnTwqqK;THThm?RKxUHKWsTUqT KxUHKIcT?T K T;?TUKqwhrKrwUTwUKxUHKvTwU?TURKqwTKnsTcTUKwvKWwvvT aK-wTKz ?TKrs??TKqwhrKUxcKlcTxUH whrKsU;Tq?T  ?RKqwTKnscKs!TcKTwUTK!kTqTKWTfTRKHwTKHTUKVwUHTcUKsxl sxTc?TRKxUHKrs??TKHsqKEck?rsTxq TwUK! kqqK;T!sx?RKxvKqwTKrTc!TwDx khmTUaKBTUUKTwUqKwUKwrcTKITns ?KmsvRKqkKvshr?TKqwTKTqK?k?RKmkhr?TKTqKxUHKsqqKTqRKxUHKHsqKnscKwrcKTwUKATq??s;aK-wTKWTfTUKrs!TUKck?TKzx;TUKxUHKmkTUUTUKUwhr?KnTw?KqTrTURKs!TcKqwTKrs!TUKTwUTKlTwUTKBw??TcxU;KnwTKHwTKZwTcTKxUHKvTcmTU.qRKnTUUKOTUqhrTUKrTcsUmkvvTUaKz qKWsTUqT KxUHKIcT?T KwUKwrcTKjsTrTKmsvTURKHsK shr?TKqwTK!kqrsl?KxUHKqdcshrKrkTrUwqhrbK'-wTKrs!TKwhrRKHwTKqk  TUKvwcKUwhr?KnwTHTcKTU?nwqhrTUS'KAcxTrKvkc;TUqRKTrTKHwTKVwUHTcKTcnshr?KnscTURKq?sUHKqwTKqhrkUKsxlRKxUHKs qKqwTK!TwHTKqkK wT! whrKcxrTUKqsrRKvw?KHTUKtk  TUKck?TUKEshmTURKqkKvxcvT ?TKqwTKtkcKqwhrKrwUbK'-sqKnwcHKTwUK;x?TcKEwqqTUKnTcHTUa'K-sKdshm?TKqwTKWsTUqT Kvw?KwrcTcKHxTccTUKWsUHKxUHK?cx;KwrUKwUKTwUTUKm TwUTUK\"?s  KxUHKqdTcc?TKwrUKvw?KTwUTcKIw??Tc?xTcTKTwUaKFcKvkhr?TKqhrcTwURKnwTKTcKnk  ?TRKTqKrs lKwrvKUwhr?qaK-sUUK;wU;KqwTKDxcKIcT?T RKcxT??T ?TKqwTKnshrKxUHKcwTlbK'\"?TrKsxlRKAsx TUDTcwURK?cs;KBsqqTcKxUHKmkhrKHTwUTvKEcxHTcKT?nsqKIx?TqRKHTcKqw?D?KHcsxqqTUKwvK\"?s  KxUHKqk  KlT??KnTcHTUaKBTUUKTcKlT??Kwq?RKqkKnw  KwhrKwrUKTqqTUa'KIcT?T KlwU;KsUK!w??Tc whrKDxKnTwUTUJKs!TcKTqKnscKs  TqKtTc;T! whrRKqwTKvxqq?TK?xURKnsqKHwTK!kTqTKWTfTKtTc sU;?TaKjxUKnscHKHTvKscvTUKWsTUqT KHsqK!Tq?TKFqqTUK;Tmkhr?RKs!TcKIcT?T K!TmsvKUwhr?qKs qKVcT!qqhrs TUaKGTHTUKOkc;TUKqhr whrKHwTKz ?TKDxKHTvK\"?sT  hrTUKxUHKcwTlbK'WsTUqT RKq?cThmKHTwUTKAwU;TcKrTcsxqRKHsvw?KwhrKlxTr TRKk!KHxK!s HKlT??K!wq?a'KWsTUqT Kq?cThm?TKwrcKs!TcKTwUKVUkThr TwUKrTcsxqRKxUHKHwTKz ?TRKHwTK?cxT!TKzx;TUKrs??TRKmkUU?TKTqKUwhr?KqTrTUKxUHKvTwU?TRKTqKnsTcTUKWsTUqT qKAwU;TcRKxUHKtTcnxUHTc?TKqwhrRKHsqqKTcK;scKUwhr?KlT??KnTcHTUKnk  ?TaKz qKtwTcKBkhrTUKrTcxvKnscTUKxUHKWsTUqT KwvvTcKvs;TcK! wT!RKHsKxT!TcmsvKqwTKHwTKMU;THx HRKxUHKqwTKnk  ?TKUwhr?K sTU;TcKnsc?TUaK'WTHsRKIcT?T R'KcwTlKqwTKHTvKOsTHhrTUKDxRK'qTwKl wUmKxUHK?cs;KBsqqTcSKWsTUqT Kvs;KlT??KkHTcKvs;TcKqTwURKvkc;TUKnw  KwhrKwrUKqhr shr?TUKxUHKmkhrTUa'KzhrRKnwTKusvvTc?TKHsqKscvTK\"hrnTq?TchrTURKs qKTqKHsqKBsqqTcK?cs;TUKvxqq?TRKxUHKnwTKl kqqTUKwrvKHwTKZcsTUTUKxT!TcKHwTKEshmTUKrTcxU?TcSK':wT!TcKIk??RKrw lKxUqKHkhrR'KcwTlKqwTKsxqRK'rsT??TUKxUqKUxcKHwTKnw HTUKZwTcTKwvKBs HK;TlcTqqTURKqkKnsTcTUKnwcKHkhrKDxqsvvTUK;Tq?kc!TUS'KoK'\"dscKUxcKHTwUKITd sTccTR'Kqs;?TKHwTKz ?TRK'TqKrw l?KHwcKs  TqKUwhr?qa'KAcxTrvkc;TUqKvxqq?TKIcT?T KrTcsxqRKHTUKVTqqT Kvw?KBsqqTcKsxlrsTU;TUKxUHKATxTcKsUDxTUHTUaK'Fcq?Knk  TUKnwcK!shmTUR'Kqs;?TKHwTKz ?TRK'whrKrs!TKHTUKEshmklTUKqhrkUKTwU;TrTwD?KxUHKHTUKZTw;K;TmUT?T?a'K\"wTKq?wTqqKHsqKscvTKIcT?T KrwUsxqKDxKHTvKEshmklTURKsxqKHTvKHwTKATxTcl svvTUKqhrkUKrTcsxqqhr x;TUK'VcwThrKrwUTwUR'Kqs;?TKHwTKWTfTRK'xUHKqwTrKDxRKk!KcThr?KTwU;TrTwD?Kwq?RKHsvw?KnwcKHsqKEck?KrwUTwUqhrwT!TUKmkTUUTUa'KMUHKnTUUKIcT?T KHscwUKnscRKnk  ?TKqwTKHTUKLlTUKDxvshrTUKxUHKIcT?T Kqk  ?TKHscwUK!cs?TURKxUHKHsUUKnk  ?TKqwT.qKsxlTqqTUaKz!TcKIcT?T KvTcm?TRKnsqKqwTKwvK\"wUUKrs??TRKxUHKqdcshrbK'ehrKnTwqqKUwhr?RKnwTKwhr.qKvshrTUKqk  JKnwTKmkvvKwhrKHsKrwUTwU,'KoK'-xvvTKIsUqR'Kqs;?TKHwTKz ?TRK'HwTKkTllUxU;Kwq?K;ckqqK;TUx;RKqwTrq?KHxKnkr RKwhrKmkTUU?TKqT !q?KrwUTwUR'Kmcs!!T ?TKrTcsUKxUHKq?Thm?TKHTUKVkdlKwUKHTUKEshmklTUaK-sK;s!KwrcKIcT?T KTwUTUK\"?kqqRKHsqqKqwTKnTw?KrwUTwUlxrcRKvshr?TKHwTKTwqTcUTKZxTcKDxKxUHKqhrk!KHTUKgwT;T KtkcaKWxSK-sKlwU;KqwTKsUKDxKrTx TURK;sUDK;csxqT whrJKs!TcKIcT?T K wTlKlkc?RKxUHKHwTK;k?? kqTKWTfTKvxqq?TKT TUHw; whrKtTc!cTUUTUaKIcT?T Ks!TcK wTlKqhrUxcq?cshmqKDxvKWsTUqT RKkTllUT?TKqTwUK\"?sT  hrTUKxUHKcwTlbK'WsTUqT RKnwcKqwUHKTc kTq?RKHwTKs ?TKWTfTKwq?K?k?a'K-sKqdcsU;KWsTUqT KrTcsxqKnwTKTwUKpk;T KsxqKHTvKVsTlw;RKnTUUKwrvKHwTKZxTcTKsxl;Tvshr?KnwcHaKBwTKrs!TUKqwTKqwhrK;TlcTx?KqwUHKqwhrKxvKHTUKWs qK;Tls  TURKqwUHKrTcxv;TqdcxU;TUKxUHKrs!TUKqwhrK;TmxTqq?SKMUHKnTw KqwTKqwhrKUwhr?KvTrcKDxKlxTchr?TUK!csxhr?TURKqkK;wU;TUKqwTKwUKHsqKWsxqKHTcKWTfTKrwUTwUaK-sKq?sUHTUKwUKs"
hashMap = [];

counter = Counter(msg)
sortedChars = counter.most_common()
dictonary = [x[0] for x in sortedChars];

commonChars = [' ', 'e','n','s','i', 'a','r', 't','h','u', 'd','l','c',',','m','o','g','w','b','f','k','"','.','H','z','G','D','p','v','S','K',"A",'W','F','B',':','M','T','x','!','E','N',"'",'U',';','V','?','Z','I','L','','P','R','j','O','R']

res = {}
for key in dictonary:
    for value in commonChars:
        res[key] = value
        commonChars.remove(value)
        break

#print(res);
#newMsg = msg.translate(str.maketrans(res))
#newMsg = newMsg.lower();

#counter = Counter(newMsg)
#returnMSG = ""
#for x in counter.most_common():
  #returnMSG = returnMSG + x[0];
#
#print(returnMSG);

#stringsList = msg.replace(sortedChars[0][0], '|').split('|');

#for el in stringsList:
 #   for char in el:
  #      dictonary['K'] 

#for sChar, cChar in zip(sortedChars, commonChars):
 #   print(sChar[0],cChar)
  #  msg.replace(sChar[0], cChar);
#print(msg);

#s!RHTl;rwum OUkd*cq?xtnf*D

