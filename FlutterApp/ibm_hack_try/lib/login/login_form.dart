import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:ibm_hack_try/bloc_login/bloc/login_bloc.dart';

import '../global.dart';


class LoginForm extends StatefulWidget {
  @override
  State<LoginForm> createState() => _LoginFormState();
}

class _LoginFormState extends State<LoginForm> {
  double screenHeight;
  final _usernameController = TextEditingController();
  final _passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    screenHeight = MediaQuery.of(context).size.height;
    _onLoginButtonPressed() {
      BlocProvider.of<LoginBloc>(context).add(LoginButtonPressed(
        username: _usernameController.text,
        password: _passwordController.text,
      ));
      Common.currentUser = _usernameController.text; 
      
    }

    return BlocListener<LoginBloc, LoginState>(
      listener: (context, state) {
        if (state is LoginFaliure) {
          Scaffold.of(context).showSnackBar(SnackBar(
            content: Text('${state.error}'),
            backgroundColor: Colors.red,
          ));
        }
      },
      child: BlocBuilder<LoginBloc, LoginState>(
        builder: (context, state) {
          return Container(
            margin: EdgeInsets.only(top: screenHeight / 3 -50),
            padding: EdgeInsets.only(left: 10, right: 10),
            color: Colors.white,
            alignment: Alignment.topCenter,
            child: Form(
              child: Padding(
                padding: EdgeInsets.all(10.0),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.start,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    Text("Your Username", 
                      style: TextStyle(color: Color(0xff3B5EE6),fontWeight: FontWeight.bold, fontFamily: 'Montserrat', fontSize: 10),),
                    TextFormField(
                      decoration: InputDecoration(
                        fillColor: Colors.grey[300],
                        filled: true,
                        labelText: 'username', prefixIcon: Icon(Icons.person, color: Color(0xff3B5EE6)),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.all(Radius.circular(25.0)))),
                      controller: _usernameController,
                    ),
                    SizedBox(height: 25),
                    Text("Password", 
                      style: TextStyle(color: Color(0xff3B5EE6),fontWeight: FontWeight.bold, fontFamily: 'Montserrat', fontSize: 10),),
                    TextFormField(
                      decoration: InputDecoration(
                        fillColor: Colors.grey[300],
                        filled: true,
                        labelText: 'password', prefixIcon: Icon(Icons.security, color: Color(0xff3B5EE6)),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.all(Radius.circular(25.0)))),
                      controller: _passwordController,
                      obscureText: true,
                    ),
                    Container(
                      width: MediaQuery.of(context).size.width * 0.85,
                      height: MediaQuery.of(context).size.width * 0.22,
                      child: Padding(
                        padding: EdgeInsets.only(top: 30.0),
                        child: RaisedButton(
                          color: Color(0xff3B5EE6),
                          onPressed: state is! LoginLoading
                              ? _onLoginButtonPressed
                              : null,
                          child: Text(
                            'LOG IN',
                            style: TextStyle(
                              fontSize: 18.0,
                              color: Colors.white
                            ),
                          ),
                          shape: StadiumBorder(
                            side: BorderSide(
                              color: Colors.white,
                              width: 2,
                            ),
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}
