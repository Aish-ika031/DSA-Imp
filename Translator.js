//useEffect: A hook used to perform side effects in function components, such as data fetching, subscriptions, or manual DOM changes. It runs after the render and can also be set to run only under certain conditions (e.g., when certain values change).
//useState: A hook used to create and manage state in a functional component. It allows you to define a state variable and a function to update that state within the component.
import { useEffect, useState } from 'react';

// This import is used to import languages.js file which we have created to store all the diffrenet langauge combinations which we will be giving theb user to make a chice...
import lang from './../language';


function Translator() {

    //This uses the useState hook to define a state variable called fromText representing some text in one language and a function setFromText to update it.
    const [fromText, setFromText] = useState('');

    //This uses the useState hook to define a variable called toText which represtnts the tranlsated text and a fucntion setToText to update its value.
    const [toText, setToText] = useState('');

    //This line is used to define a state variable and set its value to En-GB (British English)
    const [fromLanguage, setFromLanguage] = useState('en-GB');

    //This line is used to deg=fine a state varibale and set iy=ts value to Hi-IN (Hindi Indian Language)
    const [toLanguage, setToLanguage] = useState('hi-IN');

    //This line is used to define an emepty array (because we are passing empty paarmeter in usestate fucntion) which will be used to store all the availabe languages value and setLanguages.. 
    //fucntion is idefined which will be used to update the setLanguaues array values later.
    const [languages, setLanguages] = useState({});

    //This is used to define a boolean variable to check whethr a process of translation is happening or Notification.
    const [loading, setLoading] = useState(false);

    //This line sets the languages state to the value of lang when the component is rendered for the first time . The useeffect ensures that the intialization happens only once...
    // and not another time till the compoonet is mounted or unmounted again.
    useEffect(() => {
        setLanguages(lang);
    }, []);


    const copyContent = (text) => {

        //this is a arrow fucntion created whuch is used to copy the provided text as a paratmer to the system so that it is eaily availbe to use in the next steps for translation..
        navigator.clipboard.writeText(text);
    }

    //an arrow fucntion which handles what text needs to be spoken in the browser takes two parameter the Text and the langauge in which the text needs to be spoken
    const utterText = (text, language) => {

        //In this line we are creating a varibale synth which has the sppech syntheis interface that is used to handle the text to sppech. it comes form WebSearch API.
        const synth = window.speechSynthesis;

        //In this line a text is assifgned and now the uterance has the owrd which needs to be spkoen by the Text to sppech.
        const utterance = new SpeechSynthesisUtterance(text);

        //Utterance variable langauge is assigend with the language which the user will provide as per his/her choice
        utterance.lang = language;
        
        //Text to speecvh haapens by calling speak method form synth interface and providing the utterance as the parameter which ocntains the text and the lkanguege to be spoekn
        synth.speak(utterance);
    }



    //Inm this peice of code we are bascially doing the swapping of the langueges and text.
    //here we are defining an arrow fucntuion to handle this scenario.
    //We have already mentioned in the start that the objective of our project is to transalte text from one langauge to another nad vice versa.
    //so using this fucntion we are trying to achieve this feature as now the both right and left cloumns iwll swap values whtehr be it langauge to snetnces in those langauges so translate can happedn in reverse directionalso.
    const handleExchange = () => {
        let tempValue = fromText;
        setFromText(toText);
        setToText(tempValue);

        let tempLang = fromLanguage;
        setFromLanguage(toLanguage);
        setToLanguage(tempLang);
    };


    // this fucntion is used to handle the tarnsaltion procvess by taking the input text and getting the translated text from the api and upadting the values acxcordingly.
    const handleTranslate = () => {

        // this variable is now set to true because we are starting the translation procvess hnece it indicate sthat the process i s happening and when we are done with the translatio we will simply update this value with false.
        setLoading(true);

        //url contaisn the whole URl for our API which has the API and the from and to language also.
        let url = `https://api.mymemory.translated.net/get?q=${fromText}&langpair=${fromLanguage}|${toLanguage}`;

        //${fromText}: this contains the text which needs to be translated
        //${fromLanguage} : this contains the langiuage in which the current sentnece user has typed
        //${toLanguage} : this contains the language in which the user wnats the sentence or text to be translated.

        //fetch method is used to make a HTTP reuqtes using the URL which we have provided to start with the tarnlsation process using API
        fetch(url)

        // This line is used to tarnsform the repsonse which we are getting form the fetch methiod into JSON format using .json() method so that the JSON can be used later.
        .then((res) => res.json())

        //This is used to update the relevant values which are getting as a response JSON from the API  into the respective values which have created earlier and also update the loaidng valuw to false as now the tranlsation process has ended.
        .then((data) => {
            setToText(data.responseData.translatedText);
            setLoading(false);
        });
    };

    const handleIconClick = (target, id) => {

        //this is used define an arrow function called handleIconClick that takes two parameters:
        //target: This represents the element(image or icon) that was clicked when user intiated the tarnlsation
        //id: This is a string identifier indicating whether the operation should be performed on the source (fromText) or target (toText) text operation is tranlsation.
        
        //This line checsks if the FromText or Text Text anyone of it is empty then we simplty return out ot fucntion as without having any sentence whetehr doing in any
        //direction is not valid because sentencs is balnk.
        if (!fromText || !toText) return;
        
        
        if (target.classList.contains('fa-copy')) {
            //This section is used to copy the current text into clipboard so that text to speech can occur easily. 
            //But the text which needs to be spoken depends so if id has from then from text is copied like which user gave inoput
            //else To Text is copied to clipboard so it will be spoken. 
            if (id === 'from') {
                copyContent(fromText);
            } else {
                copyContent(toText);
            }
            } else {

                //This section is used to handle utter text operation using from langauge if the id has value from else To language which user has made a choice while giving the input.
            if (id === 'from') {
                utterText(fromText, fromLanguage);
            } else {
                utterText(toText, toLanguage);
            }
        }
    };

//UI Part implmentaion begins here.
// This section is same a s HTMl
    return (
        <>
        <div className="wrapper">
            <div className="text-input">
// Basiaclly we have created a recatngular section which is divided into tow blocks : right and left
//left block will have div : one Input Text fronm user and one for language slecetion
//right blcok willl aslo have div : one to displauy the result which we are getting as a response from the user.
                <textarea name="from" className="from-text" placeholder="Enter Text" id="from" value={fromText} onChange={(e) => setFromText(e.target.value)}></textarea>
                <textarea name="to" className="to-text" id="to" value={toText} readonly></textarea>
            </div>
            <ul className="controls">
                <li className="row from">
                    <div className="icons">
                        <i id="from" className="fa-solid fa-volume-high" onClick={(e) => handleIconClick(e.target, 'from')}></i>
                        <i id="from" className="fa-solid fa-copy" onClick={(e) => handleIconClick(e.target, 'from')}></i>
                    </div>
                    <select value={fromLanguage} onChange={(e) => setFromLanguage(e.target.value)}>
                    {Object.entries(languages).map(([code, name]) => (
                        <option key={code} value={code}>
                        {name}
                        </option>
                    ))}
                    </select>

                </li>

                //This section  is used to handle to exchange the langauge and text via UI purpose as we have mentioned above in the code of JS.
                //Simply we are doing those steops now in UI via react ...
                <li className="exchange" onClick={handleExchange}><i className="fa-solid fa-arrow-right-arrow-left"></i></li>
                <li className="row to">
                    <select value={toLanguage} onChange={(e) => setToLanguage(e.target.value)}>
                    {Object.entries(languages).map(([code, name]) => (
                        <option key={code} value={code}>
                        {name}
                        </option>
                    ))}
                    </select>
                    <div className="icons">
                        <i id="to" className="fa-solid fa-copy" onClick={(e) => handleIconClick(e.target, 'to')}></i>
                        <i id="to" className="fa-solid fa-volume-high" onClick={(e) => handleIconClick(e.target, 'to')}></i>
                    </div>
                </li>
            </ul>
        </div>

        //This sectionn is used to handle the laoding in progress process so as above in the code we have created a loading variablw which will be upadted when the process is ongoing..
        //so to handle this we will ahving a button Translate when user types the sentnece and then selects the language in which he/she wants to transfor it and then click translate button.
        //so duing this process we are providing a meesage as Translating so that user can get a idea that the translation is in progress.
        <button onClick={handleTranslate} disabled={loading}>
            {loading ? 'Translating...' : 'Translate Text'}
        </button>
        </>
    )
}

//This command is used to export the app as a defaulkt so that it can be eaisly imported and used in other application eaisly without any hassle by providing any simple name.
export default Translator;