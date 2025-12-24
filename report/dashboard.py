from fasthtml.common import *
import matplotlib.pyplot as plt

# Import QueryBase, Employee, Team from employee_events
#### YOUR CODE HERE
#import sys
#sys.path.insert(0, '../python-package/employee_events')
from employee_events import QueryBase, Employee, Team


# import the load_model function from the utils.py file
#### YOUR CODE HERE
from utils import load_model

# Add CSS styling
css = """
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    margin: 0;
    padding: 20px;
    min-height: 100vh;
}

.container {
    max-width: 1400px;
    margin: 0 auto;
    background: white;
    border-radius: 15px;
    padding: 30px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
}

h1 {
    color: #667eea;
    text-align: center;
    margin-bottom: 30px;
    font-size: 2.5em;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

#top-filters {
    background: #f8f9fa;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 30px;
    display: flex;
    gap: 20px;
    align-items: center;
    flex-wrap: wrap;
}

button[type="submit"] {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 12px 30px;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
}

button[type="submit"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

select, input[type="radio"] {
    padding: 8px 12px;
    border: 2px solid #e0e0e0;
    border-radius: 6px;
    font-size: 14px;
    transition: border-color 0.3s;
}

select:focus {
    outline: none;
    border-color: #667eea;
}

.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 25px;
    margin: 25px 0;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

th {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 15px;
    text-align: left;
    font-weight: 600;
}

td {
    padding: 12px 15px;
    border-bottom: 1px solid #e0e0e0;
}

tr:hover {
    background: #f8f9fa;
}

img {
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

@media (max-width: 768px) {
    .grid {
        grid-template-columns: 1fr;
    }
}
"""


"""
Below, we import the parent classes
you will use for subclassing
"""
from base_components import (
    Dropdown,
    BaseComponent,
    Radio,
    MatplotlibViz,
    DataTable
    )

from combined_components import FormGroup, CombinedComponent


# Create a subclass of base_components/dropdown
# called `ReportDropdown`
#### YOUR CODE HERE
class ReportDropdown(Dropdown):

    # Overwrite the build_component method
    # ensuring it has the same parameters
    # as the Report parent class's method
    #### YOUR CODE HERE
    def build_component(self, entity_id, model, **kwargs):
    #def build_component(self, model: QueryBase, **kwargs):
        
        #  Set the `label` attribute so it is set
        #  to the `name` attribute for the model
        #### YOUR CODE HERE
        self.label = model.name
        
        # Return the output from the
        # parent class's build_component method
        #### YOUR CODE HERE
        return super().build_component(entity_id, model, **kwargs)
    
    # Overwrite the `component_data` method
    # Ensure the method uses the same parameters
    # as the parent class method
    #### YOUR CODE HERE
    def component_data(self, entity_id, model, **kwargs):
    #def component_data(self, model: QueryBase, **kwargs):
        # Using the model argument
        # call the employee_events method
        # that returns the user-type's
        # names and ids
        #### YOUR CODE HERE
        #data = model.names_ids()
        return model.names()

# Create a subclass of base_components/BaseComponent
# called `Header`
#### YOUR CODE HERE
class Header(BaseComponent):

    # Overwrite the `build_component` method
    # Ensure the method has the same parameters
    # as the parent class
    #### YOUR CODE HERE
    def build_component(self, entity_id, model, **kwargs):
    #def build_component(self, model: QueryBase, **kwargs):
        
        # Using the model argument for this method
        # return a fasthtml H1 objects
        # containing the model's name attribute
        #### YOUR CODE HERE
        #return H1(model.name.capitalize())
        title = f"{model.name.capitalize()} Performance"
        return H1(title)

          

# Create a subclass of base_components/MatplotlibViz
# called `LineChart`
#### YOUR CODE HERE
class LineChart(MatplotlibViz):
    
    # Overwrite the parent class's `visualization`
    # method. Use the same parameters as the parent
    #### YOUR CODE HERE
    def visualization(self, entity_id, model, **kwargs):
    #def visualization(self, model: QueryBase, asset_id: int, **kwargs):

        # Pass the `asset_id` argument to
        # the model's `event_counts` method to
        # receive the x (Day) and y (event count)
        #### YOUR CODE HERE
        df = model.event_counts(entity_id)

        if df.empty or len(df) == 0:
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, 'No data available', ha='center', va='center')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            return

        # Use the pandas .fillna method to fill nulls with 0
        #### YOUR CODE HERE
        df = df.fillna(0)
        
        # User the pandas .set_index method to set
        # the date column as the index
        #### YOUR CODE HERE
        df = df.set_index(df.columns[0])
        
        # Sort the index
        #### YOUR CODE HERE
        df = df.sort_index()
        
        # Use the .cumsum method to change the data
        # in the dataframe to cumulative counts
        #### YOUR CODE HERE
        df = df.cumsum()
        
        
        # Set the dataframe columns to the list
        # ['Positive', 'Negative']
        #### YOUR CODE HERE
        df.columns = ['Positive', 'Negative']

        # Initialize a pandas subplot
        # and assign the figure and axis
        # to variables
        #### YOUR CODE HERE
        fig, ax = plt.subplots()
        
        # call the .plot method for the
        # cumulative counts dataframe
        #### YOUR CODE HERE
        df.plot(ax=ax)
        # pass the axis variable
        # to the `.set_axis_styling`
        # method
        # Use keyword arguments to set 
        # the border color and font color to black. 
        # Reference the base_components/matplotlib_viz file 
        # to inspect the supported keyword arguments
        #### YOUR CODE HERE
        self.set_axis_styling(
            ax,
            bordercolor='black',
            fontcolor='black'
            )

        name_result = model.username(entity_id)
        name = name_result[0][0] if name_result else "Unknown"
        
        # Set title and labels for x and y axis
        #### YOUR CODE HERE
        ax.set_title(f'Cumulative Event Counts Over Time - {name}', fontsize=16)
        ax.set_xlabel('Date', fontsize=14)
        ax.set_ylabel('Cumulative Event Count', fontsize=14)


# Create a subclass of base_components/MatplotlibViz
# called `BarChart`
#### YOUR CODE HERE
class BarChart(MatplotlibViz):

    # Create a `predictor` class attribute
    # assign the attribute to the output
    # of the `load_model` utils function
    #### YOUR CODE HERE
    predictor = load_model()

    # Overwrite the parent class `visualization` method
    # Use the same parameters as the parent
    #### YOUR CODE HERE
    def visualization(self, entity_id, model, **kwargs):

        # Using the model and asset_id arguments
        # pass the `asset_id` to the `.model_data` method
        # to receive the data that can be passed to the machine
        # learning model
        #### YOUR CODE HERE
        data = model.model_data(entity_id)

        if data.empty or len(data) == 0:
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, 'No data available for prediction', 
                ha='center', va='center', fontsize=14)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            return
        
        # Using the predictor class attribute
        # pass the data to the `predict_proba` method
        #### YOUR CODE HERE
        proba = self.predictor.predict_proba(data)
        
        # Index the second column of predict_proba output
        # The shape should be (<number of records>, 1)
        #### YOUR CODE HERE
        proba = proba[:, 1]
        
        
        # Below, create a `pred` variable set to
        # the number we want to visualize
        #
        # If the model's name attribute is "team"
        # We want to visualize the mean of the predict_proba output
        #### YOUR CODE HERE
        if model.name == "team":
            pred = proba.mean() 
        # Otherwise set `pred` to the first value
        # of the predict_proba output
        #### YOUR CODE HERE
        else:
            pred = proba[0]

        # Add color based on risk level
        if pred < 0.1:
            color = '#2ecc71'  # Green - low risk
        elif pred < 0.2:
            color = '#f39c12'  # Orange - medium risk
        else:
            color = '#e74c3c'  # Red - high risk

        # Initialize a matplotlib subplot
        #### YOUR CODE HERE
        fig, ax = plt.subplots()

        # Run the following code unchanged
        ax.barh([''], [pred], color=color)
        ax.set_xlim(0, 1)

        name_result = model.username(entity_id)
        name = name_result[0][0] if name_result else "Unknown"

        ax.set_title('Predicted Recruitment Risk', fontsize=16)
        
        # pass the axis variable
        # to the `.set_axis_styling`
        # method
        #### YOUR CODE HERE
        self.set_axis_styling(
            ax,
            bordercolor='black',
            fontcolor='black'
            )

# Create a subclass of combined_components/CombinedComponent
# called Visualizations       
#### YOUR CODE HERE
class Visualizations(CombinedComponent):

    # Set the `children`
    # class attribute to a list
    # containing an initialized
    # instance of `LineChart` and `BarChart`
    #### YOUR CODE HERE
    children = [
        LineChart(),
        BarChart()
        ]

    # Leave this line unchanged
    outer_div_type = Div(cls='grid')
            
# Create a subclass of base_components/DataTable
# called `NotesTable`
#### YOUR CODE HERE
class NotesTable(DataTable):

    # Overwrite the `component_data` method
    # using the same parameters as the parent class
    #### YOUR CODE HERE
    def component_data(self, entity_id, model, **kwargs):
        
        # Using the model and entity_id arguments
        # pass the entity_id to the model's .notes 
        # method. Return the output
        #### YOUR CODE HERE
        return model.notes(entity_id)
    

class DashboardFilters(FormGroup):

    id = "top-filters"
    action = "/update_data"
    method="POST"

    children = [
        Radio(
            values=["Employee", "Team"],
            name='profile_type',
            hx_get='/update_dropdown',
            hx_target='#selector'
            #hx_indicator='#loading' 
            ),
        ReportDropdown(
            id="selector",
            name="user-selection")
        ]
    
# Create a subclass of CombinedComponents
# called `Report`
#### YOUR CODE HERE
class Report(CombinedComponent):

    # Set the `children`
    # class attribute to a list
    # containing initialized instances 
    # of the header, dashboard filters,
    # data visualizations, and notes table
    #### YOUR CODE HERE
    children = [
        Header(),
        DashboardFilters(),
        Visualizations(),
        NotesTable()
        ]

# Wrap in a styled container
def __call__(self, entity_id, model):
	content = super().__call__(entity_id, model)
	return Div(content, cls='container')

# Initialize a fasthtml app 
#### YOUR CODE HERE
app, rt = fast_app(hdrs=(Style(css),))

# Initialize the `Report` class
#### YOUR CODE HERE
report = Report()

# Create a route for a get request
# Set the route's path to the root
#### YOUR CODE HERE
#@app.get('/')
@rt('/')
    # Call the initialized report
    # pass the integer 1 and an instance
    # of the Employee class as arguments
    # Return the result
    #### YOUR CODE HERE
def dashboard_root():
    #return report(entity_id=1, model=Employee())
    return report(1, Employee())
    #return report.render(model=Employee(), entity_id=1)


# Create a route for a get request
# Set the route's path to receive a request
# for an employee ID so `/employee/2`
# will return the page for the employee with
# an ID of `2`. 
# parameterize the employee ID 
# to a string datatype
#### YOUR CODE HERE
@rt('/employee/{id:int}')
def employee_report(id: int):

    # Call the initialized report
    # pass the ID and an instance
    # of the Employee SQL class as arguments
    # Return the result
    #### YOUR CODE HERE
    #return report(entity_id=id, model=Employee())
    return report(id, Employee())
    #return report.render(model=Employee(), entity_id=id)

# Create a route for a get request
# Set the route's path to receive a request
# for a team ID so `/team/2`
# will return the page for the team with
# an ID of `2`. 
# parameterize the team ID 
# to a string datatype
#### YOUR CODE HERE
@rt('/team/{id:int}')
def team_report(id: int):

    # Call the initialized report
    # pass the id and an instance
    # of the Team SQL class as arguments
    # Return the result
    #### YOUR CODE HERE
    #return report(entity_id=id, model=Team())
    return report(id, Team())
    #return report.render(model=Team(), entity_id=id)


# Keep the below code unchanged!
@rt('/update_dropdown{r}')
def update_dropdown(r):
    dropdown = DashboardFilters.children[1]
    print('PARAM', r.query_params['profile_type'])
    if r.query_params['profile_type'] == 'Team':
        return dropdown(None, Team())
    elif r.query_params['profile_type'] == 'Employee':
        return dropdown(None, Employee())


#@app.post('/update_data')
@rt('/update_data')
async def update_data(r):
    from fasthtml.common import RedirectResponse
    data = await r.form()
    profile_type = data._dict['profile_type']
    id = data._dict['user-selection']
    if profile_type == 'Employee':
        return RedirectResponse(f"/employee/{id}", status_code=303)
    elif profile_type == 'Team':
        return RedirectResponse(f"/team/{id}", status_code=303)
    
serve()

