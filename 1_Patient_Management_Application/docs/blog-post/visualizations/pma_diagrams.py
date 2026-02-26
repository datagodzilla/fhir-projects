#!/usr/bin/env python3
"""
HealthPlus Patient Management Application - Architecture Diagrams
Generates SVG diagrams using Graphviz for the blog post documentation.

Usage:
    pip install graphviz
    python pma_diagrams.py

Output:
    generated/architecture_overview.svg
    generated/fhir_resource_erd.svg
    generated/crud_sequence.svg
    generated/lazy_loading.svg
    generated/spa_views.svg
"""

import os
try:
    from graphviz import Digraph, Graph
except ImportError:
    print("Install graphviz: pip install graphviz")
    print("Also install system graphviz: brew install graphviz (macOS)")
    exit(1)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'generated')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color scheme matching the app
VERDIGRIS = '#43B3AE'
VERDIGRIS_DARK = '#359490'
VERDIGRIS_BG = '#E8F5F4'
SALMON = '#FA8072'
ORANGE = '#E65100'
ORANGE_BG = '#FFF3E0'
WHITE = '#FFFFFF'
GRAY_700 = '#495057'
GRAY_300 = '#DEE2E6'


def diagram_1_architecture():
    """Primary Architecture Overview"""
    d = Digraph('architecture', format='svg')
    d.attr(rankdir='TB', bgcolor='white', fontname='Helvetica')
    d.attr('node', fontname='Helvetica', fontsize='11', style='filled')
    d.attr('edge', fontname='Helvetica', fontsize='10')

    # Browser subgraph
    with d.subgraph(name='cluster_browser') as b:
        b.attr(label='Browser (Single HTML File - 1658 Lines)',
               style='filled', color=VERDIGRIS, fillcolor=VERDIGRIS_BG,
               fontsize='13', fontname='Helvetica-Bold')
        b.node('ui', 'UI Layer\nHTML/CSS Views\n(Home, Patient List, Form)',
               shape='box', fillcolor=WHITE, color=VERDIGRIS)
        b.node('js', 'JavaScript SPA Engine\nSTATE Object\n(Centralized State)',
               shape='box', fillcolor=WHITE, color=VERDIGRIS)
        b.node('fc', 'fhirFetch() Client\nREST Wrapper\n(Error Handling)',
               shape='box', fillcolor=WHITE, color=VERDIGRIS)

    # HAPI subgraph
    with d.subgraph(name='cluster_hapi') as h:
        h.attr(label='HAPI FHIR R4 Server (hapi.fhir.org/baseR4)',
               style='filled', color=ORANGE, fillcolor=ORANGE_BG,
               fontsize='13', fontname='Helvetica-Bold')
        h.node('re', 'REST Endpoint\nFHIR R4 API',
               shape='box', fillcolor=WHITE, color=ORANGE)
        h.node('pr', 'Patient\nResource Store',
               shape='cylinder', fillcolor=WHITE, color=ORANGE)
        h.node('er', 'Encounter\nResource Store',
               shape='cylinder', fillcolor=WHITE, color=ORANGE)
        h.node('ar', 'Appointment\nResource Store',
               shape='cylinder', fillcolor=WHITE, color=ORANGE)

    # Edges
    d.edge('ui', 'js', label='User Actions\n(click, submit, search)')
    d.edge('js', 'fc', label='API Call\nDispatch')
    d.edge('fc', 're', label='HTTP GET/POST/PUT/DELETE\nAccept: application/fhir+json',
           color=VERDIGRIS, penwidth='2')
    d.edge('re', 'fc', label='JSON Bundle / Resource\nOperationOutcome on Error',
           color=ORANGE, style='dashed', penwidth='2')
    d.edge('re', 'pr', style='dotted')
    d.edge('re', 'er', style='dotted')
    d.edge('re', 'ar', style='dotted')

    d.render(os.path.join(OUTPUT_DIR, 'architecture_overview'), cleanup=True)
    print('  Created: architecture_overview.svg')


def diagram_2_erd():
    """FHIR Resource Relationships (ERD)"""
    d = Digraph('erd', format='svg')
    d.attr(rankdir='LR', bgcolor='white', fontname='Helvetica')
    d.attr('node', fontname='Courier', fontsize='10', shape='record',
           style='filled', fillcolor=WHITE)

    d.node('patient', '''{Patient|
        id : string (PK)\\l|
        name : HumanName\\l|
        gender : code\\l|
        birthDate : date\\l|
        telecom : ContactPoint\\l|
        address : Address\\l|
        meta : Meta\\l}''',
        color=VERDIGRIS)

    d.node('encounter', '''{Encounter|
        id : string (PK)\\l|
        status : code\\l|
        class : Coding\\l|
        reasonCode : CodeableConcept\\l|
        period : Period\\l|
        subject : Reference(Patient)\\l}''',
        color=ORANGE)

    d.node('appointment', '''{Appointment|
        id : string (PK)\\l|
        status : code\\l|
        start : dateTime\\l|
        participant : Reference(Patient)\\l}''',
        color='#0D47A1')

    d.node('condition', '''{Condition|
        id : string (PK)\\l|
        code : CodeableConcept\\l|
        subject : Reference(Patient)\\l}''',
        color=GRAY_700)

    d.edge('patient', 'encounter', label='  subject  \n  1..* ',
           color=ORANGE, penwidth='2')
    d.edge('patient', 'appointment', label='  participant  \n  0..* ',
           color='#0D47A1', penwidth='2')
    d.edge('encounter', 'condition', label='  diagnosis  \n  0..1 ',
           color=GRAY_700, style='dashed')

    d.render(os.path.join(OUTPUT_DIR, 'fhir_resource_erd'), cleanup=True)
    print('  Created: fhir_resource_erd.svg')


def diagram_3_crud():
    """CRUD Operations Sequence"""
    d = Digraph('crud', format='svg')
    d.attr(rankdir='TB', bgcolor='white', fontname='Helvetica')
    d.attr('node', fontname='Helvetica', fontsize='10', style='filled')

    # Create flow
    with d.subgraph(name='cluster_create') as c:
        c.attr(label='CREATE', style='filled', fillcolor='#E8F5E9',
               color='#2E7D32', fontsize='12', fontname='Helvetica-Bold')
        c.node('c1', 'Fill Form\n+ Submit', shape='box', fillcolor=WHITE)
        c.node('c2', 'validateForm()\nbuildPatientResource()', shape='box',
               fillcolor=VERDIGRIS_BG, color=VERDIGRIS)
        c.node('c3', 'POST /Patient\n(JSON body)', shape='box',
               fillcolor=ORANGE_BG, color=ORANGE)
        c.node('c4', '201 Created\n+ Patient ID', shape='box',
               fillcolor='#E8F5E9', color='#2E7D32')

    # Read flow
    with d.subgraph(name='cluster_read') as r:
        r.attr(label='READ / SEARCH', style='filled', fillcolor='#E3F2FD',
               color='#0D47A1', fontsize='12', fontname='Helvetica-Bold')
        r.node('r1', 'Browse All\nor Search', shape='box', fillcolor=WHITE)
        r.node('r2', 'GET /Patient?\n_count=50&_offset=0\n&_sort=-_lastUpdated',
               shape='box', fillcolor=ORANGE_BG, color=ORANGE)
        r.node('r3', 'Bundle\n{entries[], total}', shape='box',
               fillcolor='#E3F2FD', color='#0D47A1')

    # Update flow
    with d.subgraph(name='cluster_update') as u:
        u.attr(label='UPDATE', style='filled', fillcolor='#FFF3E0',
               color=ORANGE, fontsize='12', fontname='Helvetica-Bold')
        u.node('u1', 'Select Patient\n+ Click Update', shape='box',
               fillcolor=WHITE)
        u.node('u2', 'GET /Patient/{id}\n(pre-fill form)', shape='box',
               fillcolor=ORANGE_BG, color=ORANGE)
        u.node('u3', 'Edit + Submit\nPUT /Patient/{id}', shape='box',
               fillcolor=ORANGE_BG, color=ORANGE)
        u.node('u4', '200 OK\nUpdated', shape='box',
               fillcolor='#FFF3E0', color=ORANGE)

    # Delete flow
    with d.subgraph(name='cluster_delete') as dl:
        dl.attr(label='DELETE', style='filled', fillcolor='#FFEBEE',
                color='#C62828', fontsize='12', fontname='Helvetica-Bold')
        dl.node('d1', 'Select + Delete\nConfirm Modal', shape='box',
                fillcolor=WHITE)
        dl.node('d2', 'DELETE /Patient/{id}', shape='box',
                fillcolor=ORANGE_BG, color=ORANGE)
        dl.node('d3', '409 Conflict?\nRetry with\n?_cascade=delete',
                shape='diamond', fillcolor='#FFEBEE', color='#C62828')
        dl.node('d4', '204 No Content', shape='box',
                fillcolor='#FFEBEE', color='#C62828')

    # Create edges
    d.edge('c1', 'c2')
    d.edge('c2', 'c3')
    d.edge('c3', 'c4')

    # Read edges
    d.edge('r1', 'r2')
    d.edge('r2', 'r3')

    # Update edges
    d.edge('u1', 'u2')
    d.edge('u2', 'u3')
    d.edge('u3', 'u4')

    # Delete edges
    d.edge('d1', 'd2')
    d.edge('d2', 'd3')
    d.edge('d3', 'd4', label='Yes: cascade')
    d.edge('d3', 'd4', label='No: direct', style='dashed')

    d.render(os.path.join(OUTPUT_DIR, 'crud_sequence'), cleanup=True)
    print('  Created: crud_sequence.svg')


def diagram_4_lazy_loading():
    """Lazy Loading for Encounter/Appointment"""
    d = Digraph('lazy', format='svg')
    d.attr(rankdir='LR', bgcolor='white', fontname='Helvetica')
    d.attr('node', fontname='Helvetica', fontsize='10', style='filled')

    d.node('table', 'Table Renders\n50 Patient Rows',
           shape='box', fillcolor=VERDIGRIS_BG, color=VERDIGRIS)
    d.node('placeholder', 'Placeholder Cells\n"Loading..."',
           shape='box', fillcolor='#FFF9C4', color='#F9A825')
    d.node('queue', 'Throttled Worker Queue\n(6 concurrent max)',
           shape='diamond', fillcolor=ORANGE_BG, color=ORANGE)

    d.node('enc1', 'GET /Encounter?\nsubject=Patient/1',
           shape='box', fillcolor=WHITE, color=GRAY_700)
    d.node('enc2', 'GET /Encounter?\nsubject=Patient/2',
           shape='box', fillcolor=WHITE, color=GRAY_700)
    d.node('enc3', '... up to\nPatient/50',
           shape='box', fillcolor=WHITE, color=GRAY_700)

    d.node('cache', 'encounterCache{}\nappointmentCache{}',
           shape='cylinder', fillcolor=VERDIGRIS_BG, color=VERDIGRIS)
    d.node('update', 'Update Table Cells\nwith Actual Data',
           shape='box', fillcolor='#E8F5E9', color='#2E7D32')

    d.edge('table', 'placeholder')
    d.edge('placeholder', 'queue')
    d.edge('queue', 'enc1')
    d.edge('queue', 'enc2')
    d.edge('queue', 'enc3')
    d.edge('enc1', 'cache')
    d.edge('enc2', 'cache')
    d.edge('enc3', 'cache')
    d.edge('cache', 'update')

    d.render(os.path.join(OUTPUT_DIR, 'lazy_loading'), cleanup=True)
    print('  Created: lazy_loading.svg')


def diagram_5_spa_views():
    """SPA View Architecture"""
    d = Digraph('spa', format='svg')
    d.attr(rankdir='TB', bgcolor='white', fontname='Helvetica')
    d.attr('node', fontname='Helvetica', fontsize='10', style='filled')

    d.node('start', '', shape='point', width='0.2')
    d.node('home', 'HOME\n\nHero Banner\nMetric Cards\nAction Buttons\nSearch Bar',
           shape='box', fillcolor=VERDIGRIS_BG, color=VERDIGRIS,
           style='filled,rounded')

    d.node('list', 'PATIENT LIST\n\nTable + Pagination\nCheckboxes\nBulk Actions',
           shape='box', fillcolor='#E3F2FD', color='#0D47A1',
           style='filled,rounded')

    d.node('create', 'CREATE FORM\n\nEmpty Form\nValidation',
           shape='box', fillcolor='#E8F5E9', color='#2E7D32',
           style='filled,rounded')

    d.node('update', 'UPDATE FORM\n\nPre-filled Form\nCalendar\nVisit History',
           shape='box', fillcolor=ORANGE_BG, color=ORANGE,
           style='filled,rounded')

    d.node('delete', 'DELETE MODAL\n\nConfirmation\nBulk Delete',
           shape='box', fillcolor='#FFEBEE', color='#C62828',
           style='filled,rounded')

    d.edge('start', 'home')
    d.edge('home', 'list', label='Browse All\n/ Search')
    d.edge('home', 'create', label='Create\nNew Patient')
    d.edge('list', 'update', label='Select +\nUpdate')
    d.edge('list', 'delete', label='Select +\nDelete')
    d.edge('create', 'home', label='Back / Save', style='dashed')
    d.edge('update', 'home', label='Back / Save', style='dashed')
    d.edge('delete', 'list', label='Confirm /\nCancel', style='dashed')

    d.render(os.path.join(OUTPUT_DIR, 'spa_views'), cleanup=True)
    print('  Created: spa_views.svg')


if __name__ == '__main__':
    print('Generating HealthPlus PMA Architecture Diagrams...\n')
    diagram_1_architecture()
    diagram_2_erd()
    diagram_3_crud()
    diagram_4_lazy_loading()
    diagram_5_spa_views()
    print(f'\nAll diagrams saved to: {OUTPUT_DIR}/')
