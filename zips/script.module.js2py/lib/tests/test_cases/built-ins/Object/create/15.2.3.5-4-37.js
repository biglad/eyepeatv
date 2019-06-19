// Copyright (c) 2012 Ecma International.  All rights reserved.
// Ecma International makes this code available under the terms and conditions set
// forth on http://hg.ecmascript.org/tests/test262/raw-file/tip/LICENSE (the
// "Use Terms").   Any redistribution of this code must retain the above
// copyright and this notice and otherwise comply with the Use Terms.

/*---
es5id: 15.2.3.5-4-37
description: >
    Object.create - 'Properties' is an Error object that uses Object's
    [[Get]] method to access own enumerable property (15.2.3.7 step
    5.a)
includes: [runTestCase.js]
---*/

function testcase() {

        var props = new Error("test");

        (Object.getOwnPropertyNames(props)).forEach(function(name){
            props[name] = {value:11, configurable:true}
        });

        props.prop15_2_3_5_4_37 = {
            value: 12,
            enumerable: true
        };
        var newObj = Object.create({}, props);
        return newObj.hasOwnProperty("prop15_2_3_5_4_37");
    }
runTestCase(testcase);
