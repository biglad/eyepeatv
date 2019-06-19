// Copyright (c) 2012 Ecma International.  All rights reserved.
// Ecma International makes this code available under the terms and conditions set
// forth on http://hg.ecmascript.org/tests/test262/raw-file/tip/LICENSE (the
// "Use Terms").   Any redistribution of this code must retain the above
// copyright and this notice and otherwise comply with the Use Terms.

/*---
es5id: 15.4.4.22-9-c-ii-18
description: >
    Array.prototype.reduceRight - 'accumulator' used for first
    iteration is the value of 'initialValue' when it is present on an
    Array
includes: [runTestCase.js]
---*/

function testcase() {

        var arr = [11, 12];
        var testResult = false;
        var initVal = 6.99;

        function callbackfn(prevVal, curVal, idx, obj) {
            if (idx === 1) {
                testResult = (prevVal === initVal);
            }
            return curVal;
        }

        arr.reduceRight(callbackfn, initVal);

        return testResult;
    }
runTestCase(testcase);
