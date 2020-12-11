'use strict';

const { Contract } = require('fabric-contract-api');

class myapp extends Contract {

    async initLedger(ctx) {
        console.info('============= START : Initialize Ledger ===========');
        const phones = [
            {
                color: 'blue',
                make: 'test',
                model: 'test',
                price: '199',
                condition: 'new'
            },
            {
                color: 'red',
                make: 'Ford',
                model: 'Mustang',
                price: 'Brad',
            },
            {
                color: 'green',
                make: 'Hyundai',
                model: 'Tucson',
                price: 'Jin Soo',
            },
            {
                color: 'yellow',
                make: 'Volkswagen',
                model: 'Passat',
                price: 'Max',
            },
            {
                color: 'black',
                make: 'Tesla',
                model: 'S',
                price: 'Adriana',
            },
            {
                color: 'purple',
                make: 'Peugeot',
                model: '205',
                price: 'Michel',
            },
            {
                color: 'white',
                make: 'Chery',
                model: 'S22L',
                price: 'Aarav',
            },
            {
                color: 'violet',
                make: 'Fiat',
                model: 'Punto',
                price: 'Pari',
            },
            {
                color: 'indigo',
                make: 'Tata',
                model: 'Nano',
                price: 'Valeria',
            },
            {
                color: 'brown',
                make: 'Holden',
                model: 'Barina',
                price: 'Shotaro',
            },
        ];

        for (let i = 0; i < phones.length; i++) {
            phones[i].docType = 'phone';
            await ctx.stub.putState('PHONE' + i, Buffer.from(JSON.stringify(phones[i])));
            console.info('Added <--> ', phones[i]);
        }
        console.info('============= END : Initialize Ledger ===========');
    }

    async queryPhone(ctx, phoneNumber) {
        const phoneAsBytes = await ctx.stub.getState(phoneNumber); // get the phone from chaincode state
        if (!phoneAsBytes || phoneAsBytes.length === 0) {
            throw new Error(`${phoneNumber} does not exist`);
        }
        console.log(phoneAsBytes.toString());
        return phoneAsBytes.toString();
    }

    async createPhone(ctx, phoneNumber, make, model, color, price,condition) {
        console.info('============= START : Create Phone ===========');

        const phone = {
            color,
            docType: 'phone',
            make,
            model,
            price,
            condition
        };

        await ctx.stub.putState(phoneNumber, Buffer.from(JSON.stringify(phone)));
        console.info('============= END : Create Phone ===========');
    }

    async queryAllPhones(ctx) {
        const startKey = 'PHONE0';
        const endKey = 'PHONE999';
        const allResults = [];
        for await (const {key, value} of ctx.stub.getStateByRange(startKey, endKey)) {
            const strValue = Buffer.from(value).toString('utf8');
            let record;
            try {
                record = JSON.parse(strValue);
            } catch (err) {
                console.log(err);
                record = strValue;
            }
            allResults.push({ Key: key, Record: record });
        }
        console.info(allResults);
        return JSON.stringify(allResults);
    }

    async changePhoneprice(ctx, phoneNumber, newprice) {
        console.info('============= START : changePhoneprice ===========');

        const phoneAsBytes = await ctx.stub.getState(phoneNumber); // get the phone from chaincode state
        if (!phoneAsBytes || phoneAsBytes.length === 0) {
            throw new Error(`${phoneNumber} does not exist`);
        }
        const phone = JSON.parse(phoneAsBytes.toString());
        phone.price = newprice;

        await ctx.stub.putState(phoneNumber, Buffer.from(JSON.stringify(phone)));
        console.info('============= END : changePhoneprice ===========');
    }

}

module.exports = myapp;
