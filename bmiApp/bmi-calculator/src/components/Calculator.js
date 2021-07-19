import { useState } from 'react';

const Calculator = (props) => {

    const BMIResult = () => {
        const result = parseInt(weight) / (parseInt(height) / 100 * parseInt(height) / 100);
        return result;

    }

    const [weight, setWeight] = useState('');
    const [height, setHeight] = useState('');

    return(
        <div className="calculator-container">
            <h1>BMI CALCULATOR</h1>
            <label> Height in cms.
                <input type="tel" className="info" onChange={
                    (e) => setHeight(e.target.value)
                } />
            </label>
            <label> Weight in kgs.
                <input type="tel" className="info" onChange={(e) => setWeight(e.target.value)} />
            </label>
            <input type="submit" value="OK" id="submit" onClick={ BMIResult } />
            <br/>
            <h3 id="resultText">Your BMI result is: <h2 id="result">{BMIResult()} kg/m²</h2> </h3>
            <br/>
            <p>If it is below 18.5 kg/m², then you are skinny.</p>
            <p>If it is between 18.5 kg/m² and 23.9 kg/m², it is normal.</p>
            <p>If it is between 25 kg/m² and 29.9 kg/m², then you are overweight.</p>
            <p>If it is between 30 kg/m² and 39.9 kg/m², then you are obese.</p>
            <p>If it is above 40 kg/m², then you are extremely obese.</p>

            
        </div>
        
    )
} 

export default Calculator;