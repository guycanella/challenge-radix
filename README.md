<div
    style="
        display: flex; align-items: center; gap: 2rem;padding: 2rem;  background-image: linear-gradient(90deg, #2A1844 0%, #532F88 100%)
    "
>
    <img src="radix_logo.webp" alt="Logo radix" />
    <h1 style="color: white">Radix Challenge</h1>
</div>

<h2>The Challenge</h2>

<p>
    You work for a company which installed sensors in their equipments. Your job is to develop an API which capture the measures of these sensors in real-time. To solve this problem I assumed some points:
    <ol>
        <li>I worked only with 10 equipments and each equipment has 1 sensor attached to it.</li>
        <li>The equipmentId of the equipments varies from EQ-12486 to EQ-12495.</li>
        <li>The sensor measurement interval is 2h, so each sensor capture 12 measures per day.</li>
        <li>The possible values measured by the sensor, rise between 0.0 and 90.0.</li>
    </ol>
</p>

<h2>The Project</h2>

<p>
This project was developed using:

<ul>
    <li>Backend:</li>
    <ul>
        <li>Python</li>
        <li>FastAPI</li>
        <li>PostgreSQL</li>
        <li>Docker</li>
        <li>and other libs</li>
    </ul>
    <li>Frontend:</li>
    <ul>
        <li>React</li>
        <li>Typescript</li>
        <li>Recharts</li>
        <li>and other libs</li>
    </ul>
</ul>
</p>

<p>
You can check other requirements in files <code>pyproject.toml</code> and <code>package.json</code> in backend and frontend folders, respectively.
</p>

<h2>Installation</h2>

<p>
    To install the dependencies, run the script <code>install_dependencies.sh</code>:
</p>

```bash
$ ./install_dependencies.sh
```

<p>
    <b>Obs:</b> you will need <code>poetry</code> and one of javascript package managers (<code>pnpm</code>, <code>yarn</code> or <code>npm</code>) installed in your computer.
</p>

<p>
    If  you want, you can install the dependencies manually.
    First go to the <code>backend folder</code> and run:
</p>

```bash
$ poetry install
```

<p>
    Then go to the <code>frontend folder</code> and run:
</p>

```bash
$ pnpm install
```

<h2>Getting started</h2>

<p>
    First, you'll need a <code>docker</code> container working with a postgreSQL database running. So,
</p>

<ol>
    <li>
        Create an <code>.env</code> file inside the backend folder. Your file must have this structure
    </li>
    <pre>
    POSTGRES_USER="&lt;YOUR_POSTGRES_USER&gt;"
    POSTGRES_PASSWORD="&lt;YOUR_POSTGRES_PASSWORD&gt;"
    POSTGRES_DB="&lt;NAME_OF_YOUR_DATABASE&gt;"
    TABLE_NAME="&lt;NAME_OF_YOUR_TABLE&gt;"
    DB_HOST="localhost"
    PORT="5432"
    DB_URL="postgresql+psycopg2://&lt;YOUR_POSTGRES_USER&gt;:&lt;YOUR_POSTGRES_PASSWORD&gt;@localhost:5432/&lt;NAME_OF_YOUR_DATABASE&gt;"
    </pre>
    <p>
        <b>Obs:</b> in this case we are using port <code>5432</code> but you can choose another one.
    </p>
    <li>
        Still inside the backend folder run
    </li>
    <pre>$ docker-compose up -d</pre>
    <p>This will start a container with PostgreSQL.</p>
    <li>
        To generate and apply the migration (to create table <code>data_sensor</code>) run
    </li>
    <pre>$ alembic revision --autogenerate -m "add data_sensor table"</pre>
    <pre>$ source .env</pre>
    <pre>$ alembic upgrade head"</pre>
    <li>
        Go back to the <code>root</code> folder and run the script <code>generate_and_insert_data_sensor.sh</code>
    </li>
    <pre>$ ./generate_and_insert_data_sensor.sh</pre>
    <p>
        <b>Obs:</b> the script <code>generate_and_insert_data_sensor.sh</code> checks the version of python and run two other scrips: <code>generate_sensor_data.py</code> and <code>insert_sensor_data.py</code>. It works correctly in Debian environments (Debian, Ubuntu, Linux Mint, etc) because of the structure of the directories. If your operational system is a different one, you should run the python scripts separately.
    </p>
    <p>
        <b>Obs:</b> it will create some data and insert in your database.
    </p>
    <li>
        If everything goes well, just run the file <code>run_project.sh</code> to start both backend and front end
    </li>
    <pre>$ ./run_project.sh</pre>
</ol>