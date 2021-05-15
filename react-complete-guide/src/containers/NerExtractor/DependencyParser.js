import React, { Component } from 'react'
import { ArcherContainer, ArcherElement } from 'react-archer';
const rootStyle = { display: 'flex', justifyContent: 'center' };
const rowStyle = { margin: '200px 0', display: 'flex', justifyContent: 'space-between', }
const boxStyle = { padding: '10px', border: '1px solid black', };

const DependencyParser = (props) => {

    // var word_block = props.sentence.map((source => {

    //     var relations = [];
    //     props.sentence.forEach(
    //         target => {
    //             if (target['head'] === source['index']) {
    //                 relations.push({
    //                     targetId: target['head'],
    //                     targetAnchor: 'top',
    //                     sourceAnchor: 'bottom',
    //                     style: { strokeColor: 'blue', strokeWidth: 1 },
    //                     label: <div style={{ marginTop: '-20px' }}></div>
    //                 })
    //             }
    //         }
    //     )


    //     return <ArcherElement
    //         id={element['index']}
    //         relations={[
    //             {
    //                 targetId: 'element3',
    //                 targetAnchor: 'left',
    //                 sourceAnchor: 'right',
    //                 style: { strokeColor: 'blue', strokeWidth: 1 },
    //                 label: <div style={{ marginTop: '-20px' }}>Arrow 2</div>,
    //             },
    //         ]}
    //     >
    //         <div style={boxStyle}>Element 2</div>
    //     </ArcherElement>
    // }))
    // var depLabelBlock;

    // var input = props.sentence
    // var relation_source_depLabel = {

    // }
    // input.forEach(element => {

    //     var source = element['head'].toString()
    //     var target = source+"to"+element['index'];

    // })


    var relation = [];
    var input = props.sentence;
    input.forEach(element => {
        var source = element['head']
        var target = element['index']
        var depLabel = element['depLabel']
        relation.push(
            {
                source: source.toString(),
                target: source.toString() + "depNode" + target.toString(),
                depLabel: depLabel
            }
        )
        relation.push(
            {
                source: source.toString() + "depNode" + target.toString(),
                target: target.toString(),
                depLabel: depLabel
            }
        )


    })
    var word_block = input.map(element => {

        var index = element['index']

        var local_relations = [];
        relation.forEach(rlt => {
            if (rlt['source'] === index) {
                local_relations.push(
                    {
                        targetId: rlt['target'],
                        targetAnchor: 'top',
                        sourceAnchor: 'bottom',
                        style: { strokeColor: 'blue', strokeWidth: 1 },
                        label: <div style={{ marginTop: '-20px' }}>{rlt['depLabel']}</div>,
                    }
                )
            }
        })


        return (
            <ArcherElement
                id={index}
                relations={local_relations}
            >
                <div style={boxStyle}>{element['form']}</div>
            </ArcherElement>
        )

    })

    var intermidiate = []
    relation.forEach(element => {
        var source = element['source'];
        var target = element['target']
        if (source.includes('depNode')) {
            intermidiate.push(
                <ArcherElement
                    id={source}
                    relations={[
                        {
                            targetId: target,
                            targetAnchor: 'top',
                            sourceAnchor: 'bottom',
                            style: { strokeColor: 'blue', strokeWidth: 1 },
                        label: <div style={{ marginTop: '-20px' }}>{element['depLabel']}</div>,
                        },
                    ]}
                >

                </ArcherElement>

            )
        }
    })




    return (
        <div style={{ height: '500px', margin: '50px' }}>
            <ArcherContainer strokeColor="red">
                <div style={rootStyle}>
                    {intermidiate}

                </div>
                <div style={rowStyle}>
                    {word_block}

                </div>
            </ArcherContainer>
        </div>
    )
}
export default DependencyParser