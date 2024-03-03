import {NavigationContainer} from "@react-navigation/native"
import {createNativeStackNavigator} from "@react-navigation/native-stack"
import GetStarted from './app/screens/LoginScreen/GetStarted';
import Account from './app/screens/LoginScreen/Account';
import SpotifyLogin from './app/screens/LoginScreen/SpotifyLogin';

const Stack = createNativeStackNavigator()

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="GetStarted">
        <Stack.Screen name="GetStarted" component = {GetStarted}/>
        <Stack.Screen name="Account" component = {Account}/>
        <Stack.Screen name="SpotifyLogin" component = {SpotifyLogin}/>
      </Stack.Navigator>
    </NavigationContainer>
  );
}
