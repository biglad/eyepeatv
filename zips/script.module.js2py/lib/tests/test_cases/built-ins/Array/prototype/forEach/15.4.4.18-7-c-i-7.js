// Copyright (c) 2012 Ecma International.  All rights reserved.
// Ecma International makes this code available under the terms and conditions set
// forth on http://hg.ecmascript.org/tests/test262/raw-file/tip/LICENSE (the
// "Use Terms").   Any redistribution of this code must retain the above
// copyright and this notice and otherwise comply with the Use Terms.

/*---
es5id: 15.4.4.18-7-c-i-7
description: >
    Array.prototype.forEach - element to be retrieved is inherited
    data property on an Array-like object
includes: [runTestCase.js]
---*/

function testcase() {

        var kValue = 'abc';
        var testResult = false;

        function callbackfn(val, idx, obj) {
            if (idx === 5) {
                testResult = (val === kValue);
            }
        }

        var proto = { 5: kValue };

        var Con = function () { };
        Con.prototype = proto;

        var child = new Con();
        child.length = 10;

        Array.prototype.forEach.call(child, callbackfn);

        return testResult;
    }
runTestCase(testcase);
