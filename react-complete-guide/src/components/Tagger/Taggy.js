import React from 'react'

// Define functional component. Destructure the props.
const Taggy = (props) => {
    var text = props.text
    var spans = props.spans
    var ents = props.ents
    console.log(text)
    console.log(spans)
    // Find the correct color of the given entity type. If the given entity is not found, set the color to grey.
    const findRed = (type) => {
        

        for (let e = 0; e < ents.length; e++) {
            if (ents[e].type === type) {
                return ents[e].color.r
            }
        }
        return 220
        
    }
    const findGreen = (type) => {
        if(ents)
        {
        for (let e = 0; e < ents.length; e++) {
            if (ents[e].type === type) {
                return ents[e].color.g
            }
        }
    }
    return 220
        
    }
    const findBlue = (type) => {
        if(ents)
        {
        for (let e = 0; e < ents.length; e++) {
            if (ents[e].type === type) {
                return ents[e].color.b
            }
        }
    }
    return 220
        
    }

    // Initialize an empty array that will hold the text and entities
    let jsx = []
    

    
    if (Array.isArray(text)) {
        // Rename 'text' to 'tokens' for clarity
        let tokens = [...text]
        console.log(tokens)
        // Loop through the 'spans' array. Use the span data to update our 'tokens' array with entities
        for (let s = 0; s < spans.length; s++) {
            tokens[spans[s].index] = {
                token: tokens[spans[s].index],
                type: spans[s].type.toLowerCase()
            }
        }
        
       
        tokens.forEach(t => {
            if (t.type === 'o') {
                jsx.push(t.token.replace("_",'\xa0\xa0') + "\xa0\xa0")
                
            }
            else {
                jsx.push(
                    <mark
                        style={{
                            padding: '0.25em 0.35em',
                            margin: '0px 0.25em',
                            lineHeight: '1',
                            display: 'inline-block',
                            borderRadius: '0.25em',
                            border: '1px solid',
                            background: `rgba(
                                ${findRed(t.type)},
                                ${findGreen(t.type)},
                                ${findBlue(t.type)},
                                0.2
                            )`,
                            borderColor: `rgb(
                                ${findRed(t.type)},
                                ${findGreen(t.type)},
                                ${findBlue(t.type)}
                            )`
                        }}
                    >
                        {t.token}
                        <span
                            style={{
                                boxSizing: 'border-box',
                                fontSize: '0.6em',
                                lineHeight: '1',
                                padding: '0.35em',
                                borderRadius: '0.35em',
                                textTransform: 'uppercase',
                                display: 'inline-block',
                                verticalAlign: 'middle',
                                margin: '0px 0px 0.1rem 0.5rem',
                                background: `rgb(
                                    ${findRed(t.type)},
                                    ${findGreen(t.type)},
                                    ${findBlue(t.type)}
                                )`
                            }}
                        >
                            {t.type}
                        </span>
                        
                    </mark>
                )
            }
        })
    }

    // Return the markup
   
    
    return (
        
        <div>
            {jsx.map((j, i) => (
                <span key={i}>{j}</span>
            ))}
        </div>
    )

}

export default Taggy