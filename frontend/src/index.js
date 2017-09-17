
import React from 'react';
import ReactDOM from 'react-dom';

var data = require('./ajax/data.json');


    let users = [];
    data.results.forEach(function(element) {
        users.push(element.name);
    })

const usersList = users.map((user) =>
    <li>{user}</li>
);


const element = (
    <ul>
        {usersList}
    </ul>
);

ReactDOM.render(element, document.getElementById('root'))




