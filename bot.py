import time
import logging
from datetime import datetime
from iqoptionapi.stable_api import IQ_Option

Iq=IQ_Option("loggin","password")
Iq.connect()

modo_da_conta= "REAL" #tipo da conta onde a compra será feita = PRACTICE ou REAL
Iq.change_balance(modo_da_conta)

#variaveis 

btc_buy_price=54000.00 # preço inicial de compra antes do bot calcular a média 
btc_buy_price2=10000.00#
btc_new_price=0#
btc_temp=0#



#parametros para a compra
instrument_type="crypto" #tipo
instrument_id="BTCUSD" #qual comprar
side="buy" #buy or sell
leverage=3 #x3 multiplicador *NÂO MUDAR*
type="market" 
limit_price=None
stop_price=None
stop_lose_kind="percent"
stop_lose_value=99 # % de perda para vender 
take_profit_kind="percent"
take_profit_value=2 # % de ganhos para vender
use_trail_stop=True
auto_margin_call=False
use_token_for_commission=False
Iq.subscribe_top_assets_updated(instrument_type) #stuff to the search price work


while True:
    print('1')
    date=datetime.now()#seta o tempo
    date_now=date.strftime("%H:%M")#seta o tempo como str


    #busca o preço atual do biticoin
    print('2')
    if Iq.get_top_assets_updated(instrument_type)!=None:
        print('3')
        list=Iq.get_top_assets_updated(instrument_type)
        print('4')
        price_btc=(list[0]["cur_price"]['value'])
        btc_new_price+=price_btc
        btc_temp+=1
        print(date_now)
        print("BTC $:",price_btc)
        print('VDV $:',btc_buy_price)
        print(' ')
        
        #seta um novo valor para a compra em 6 em 6 horas
        if date_now == '00:00':
            btc_buy_price=btc_new_price/btc_temp
            btc_buy_price=btc_buy_price-100
            btc_buy_price2=btc_buy_price-400
            btc_new_price=0
            btc_temp=0
            time.sleep(120)
        
        elif date_now == '06:00':
            btc_buy_price=btc_new_price/btc_temp
            btc_buy_price=btc_buy_price-100
            btc_buy_price2=btc_buy_price-400
            btc_new_price=0
            btc_temp=0
            time.sleep(120)

        elif date_now == '12:00':
            btc_buy_price=btc_new_price/btc_temp
            btc_buy_price=btc_buy_price-100
            btc_buy_price2=btc_buy_price-400
            btc_new_price=0
            btc_temp=0
            time.sleep(120)

        elif date_now == '18:00':
            btc_buy_price=btc_new_price/btc_temp
            btc_buy_prie=btc_buy_price-100
            btc_buy_price2=btc_buy_price-500
            btc_new_price=0
            btc_temp=0
            time.sleep(120)



        #busca o valor total de fundos na carteira
        print('5')
        wallet=Iq.get_balance()
        wallet_comprar= wallet / 2 #quantidade que ele ira comprar com base no valor total que a sua carteira esta no momento
        time.sleep(1)
        print('6')

        #buy btc if he is price valeu is lower that btc buy price
        if price_btc < btc_buy_price and wallet >= 20:
            print('7')
            amount=wallet_comprar # seta o valor da compra como metade do valor da carteira 

            check,id=Iq.buy_order(instrument_type=instrument_type, instrument_id=instrument_id,
            side=side, amount=amount,leverage=leverage,
            type=type,limit_price=limit_price, stop_price=stop_price,
            stop_lose_value=stop_lose_value, stop_lose_kind=stop_lose_kind,
            take_profit_value=take_profit_value, take_profit_kind=take_profit_kind,
            use_trail_stop=use_trail_stop, auto_margin_call=auto_margin_call,
            use_token_for_commission=use_token_for_commission)
            print('8')
            time.sleep(20)

            if check:
                print("Purchased R$",wallet_comprar)
            else:
                pass
        if price_btc < btc_buy_price2 and wallet >= 4:

            amount=wallet_comprar
            if wallet < 8:
                amount=wallet
             # seta o valor da compra como metade do valor da carteira 

            check,id=Iq.buy_order(instrument_type=instrument_type, instrument_id=instrument_id,
            side=side, amount=amount,leverage=leverage,
            type=type,limit_price=limit_price, stop_price=stop_price,
            stop_lose_value=stop_lose_value, stop_lose_kind=stop_lose_kind,
            take_profit_value=take_profit_value, take_profit_kind=take_profit_kind,
            use_trail_stop=use_trail_stop, auto_margin_call=auto_margin_call,
            use_token_for_commission=use_token_for_commission)
            time.sleep(20)

            if check:
                print("Purchased R$",wallet_comprar)
            else:
                pass




        
