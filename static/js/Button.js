import * as React from 'react';
import { Socket } from './Socket';
import { GoogleLogin } from 'react-google-login';
import { GoogleLogout } from 'react-google-login';


export class Button extends React.Component{
    constructor(props){
        super(props);
        this.state = {value: ''};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event){
        this.setState({value: event.target.value});
    }

    handleSubmit(event){
        event.preventDefault();

        let auth = gapi.auth2.getAuthInstance();
        let user = auth.currentUser.get();
        if(user.isSignedIn()){
            console.log("google token" + user.getAuthResponse().id_token);
        }



    }



}







}