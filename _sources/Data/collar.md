
# Elephant GPS Collars Data


The Danau Girang Field Centre (DGFC) https://www.dgfc.life/home/ provided us with the collars data for elephants. Collars weighing approximately 14 kg each were officially placed around the elephants' necks to record numerous metrics  every two hours, including time, geolocation, and temperature.
In this study, we modelled twenty-two adult Asian elephants (Elephas maximus), fourteen females and eight males. The collars were created by Africa Wildlife Tracking and fitted ethically by a team of researchers, trackers, and a wildlife vet. Each collar had a Global Positioning System (GPS) receiver and a Very High Frequency (VHF) transmitter. At predetermined intervals, the GPS uploaded each individual's geographical location information to the Globaltrack server, which could be officially obtained from the Globaltrack website (http://www.globaltrack.com). The built-in VHF transmitter aided in retrieving collars that had come off naturally or in locating an individual when additional monitoring was required. The observations in those datasets cover the period range between 2012 to 2018. We refrain from publishing the datasets used in this study because they could be misused to locate an endangered species at risk of poaching. 

![Animal GPS Collars Data](/img/collar.png)

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOexaicG5g0qouMRn5PmKzr",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Naeima/Jasmin/blob/main/Jasmin.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nfEMD0zZny2q",
        "outputId": "700d3374-2b65-4744-aecb-eaff7f0d7e05"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting rdflib\n",
            "  Downloading rdflib-7.0.0-py3-none-any.whl.metadata (11 kB)\n",
            "Collecting isodate<0.7.0,>=0.6.0 (from rdflib)\n",
            "  Downloading isodate-0.6.1-py2.py3-none-any.whl.metadata (9.6 kB)\n",
            "Requirement already satisfied: pyparsing<4,>=2.1.0 in /usr/local/lib/python3.10/dist-packages (from rdflib) (3.1.4)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.10/dist-packages (from isodate<0.7.0,>=0.6.0->rdflib) (1.16.0)\n",
            "Downloading rdflib-7.0.0-py3-none-any.whl (531 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m531.9/531.9 kB\u001b[0m \u001b[31m6.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading isodate-0.6.1-py2.py3-none-any.whl (41 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m41.7/41.7 kB\u001b[0m \u001b[31m1.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: isodate, rdflib\n",
            "Successfully installed isodate-0.6.1 rdflib-7.0.0\n"
          ]
        }
      ],
      "source": [
        "!pip install rdflib"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "import pandas as pd\n",
        "import csv\n",
        "from rdflib import Graph, Namespace, URIRef, Literal\n",
        "from rdflib.namespace import RDF, XSD\n",
        "\n",
        "# Prompt for file upload\n",
        "uploaded = files.upload()\n",
        "\n",
        "# Read the uploaded CSV file into a pandas DataFrame\n",
        "for filename in uploaded.keys():\n",
        "    print('User uploaded file \"{name}\" with length {length} bytes'.format(\n",
        "        name=filename, length=len(uploaded[filename])))\n",
        "    df = pd.read_csv(filename)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 112
        },
        "id": "ZiQ4mWZKpPyq",
        "outputId": "cee08729-a827-491f-fcb8-63a19c5f5d83"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-697e264a-ffb4-4583-94d0-d0502d2b0dc2\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-697e264a-ffb4-4583-94d0-d0502d2b0dc2\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving Jasmin.csv to Jasmin.csv\n",
            "User uploaded file \"Jasmin.csv\" with length 91201 bytes\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# GPS collar\n",
        "import csv\n",
        "from rdflib import Graph, Namespace, URIRef, Literal\n",
        "from rdflib.namespace import RDF, XSD\n",
        "\n",
        "# Define namespaces\n",
        "FOO = Namespace(\"https://w3id.org/def/foo#\")\n",
        "SOSA = Namespace(\"http://www.w3.org/ns/sosa/\")\n",
        "GEO = Namespace(\"http://www.w3.org/2003/01/geo/wgs84_pos#\")\n",
        "\n",
        "# Create a new graph\n",
        "g = Graph()\n",
        "\n",
        "# Bind namespaces\n",
        "g.bind(\"foo\", FOO)\n",
        "g.bind(\"sosa\", SOSA)\n",
        "g.bind(\"geo\", GEO)\n",
        "\n",
        "# Path to your CSV file\n",
        "csv_file_path = \"Jasmin.csv\"  # Adjust the path accordingly\n",
        "\n",
        "# Read and process data\n",
        "with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:\n",
        "    reader = csv.DictReader(csvfile, delimiter=',')\n",
        "\n",
        "    # Print headers for debugging\n",
        "    print(\"Headers:\", reader.fieldnames)\n",
        "\n",
        "    for row in reader:\n",
        "        identifier = row.get('ID', '').strip()\n",
        "        local_date = row.get('LocalDate', '').strip()\n",
        "        local_time = row.get('LocalTime', '').strip()\n",
        "        gmt_date = row.get('GMTDate', '').strip()\n",
        "        gmt_time = row.get('GMTTime', '').strip()\n",
        "        lat = row.get('lat', '').strip()\n",
        "        long = row.get('long', '').strip()\n",
        "        temperature = row.get('Temperature', '').strip()\n",
        "        speed = row.get('Speed', '').strip()\n",
        "        direction = row.get('Direction', '').strip()\n",
        "        altitude = row.get('Altitude', '').strip()\n",
        "        cov = row.get('Cov', '').strip()\n",
        "        hdop = row.get('HDOP', '').strip()\n",
        "        distance = row.get('Distance', '').strip()\n",
        "        count = row.get('Count', '').strip()\n",
        "\n",
        "\n",
        "        # Create observation URI\n",
        "        observation = URIRef(f\"https://w3id.org/def/foo#{identifier}\")\n",
        "        g.add((observation, RDF.type, FOO.gPSObservation))\n",
        "        g.add((observation, FOO.id, Literal(identifier, datatype=XSD.string)))\n",
        "        g.add((observation, FOO.madeBySensor, FOO.jasminGPS))  # Link sensor to observation\n",
        "        g.add((observation, FOO.hasFeatureOfInterest, FOO.jasmin))\n",
        "\n",
        "        # Add observation properties\n",
        "        g.add((observation, FOO.localDate, Literal(local_date, datatype=XSD.date)))\n",
        "        g.add((observation, FOO.localTime, Literal(local_time, datatype=XSD.time)))\n",
        "        g.add((observation, FOO.gMTDate, Literal(gmt_date, datatype=XSD.date)))\n",
        "        g.add((observation, FOO.gMTTime, Literal(gmt_time, datatype=XSD.time)))\n",
        "        g.add((observation, GEO.latitude, Literal(lat, datatype=XSD.double)))\n",
        "        g.add((observation, GEO.longitude, Literal(long, datatype=XSD.double)))\n",
        "\n",
        "        # Add observable properties if available\n",
        "        if temperature:\n",
        "            g.add((observation, FOO.temperature, Literal(temperature, datatype=XSD.double)))\n",
        "        if speed:\n",
        "            g.add((observation, FOO.speed, Literal(speed, datatype=XSD.double)))\n",
        "        if direction:\n",
        "            g.add((observation, FOO.direction, Literal(direction, datatype=XSD.integer)))\n",
        "        if altitude:\n",
        "            g.add((observation, FOO.altitude, Literal(altitude, datatype=XSD.string)))\n",
        "        if cov:\n",
        "            g.add((observation, FOO.cov, Literal(cov, datatype=XSD.double)))\n",
        "        if hdop:\n",
        "            g.add((observation, FOO.hDOP, Literal(hdop, datatype=XSD.double)))\n",
        "        if distance:\n",
        "            g.add((observation, FOO.distance, Literal(distance, datatype=XSD.double)))\n",
        "        if count:\n",
        "            g.add((observation, FOO.cOUNT, Literal(count, datatype=XSD.integer)))\n",
        "\n",
        "# Serialize the graph to a file\n",
        "output_file = \"sensor_knowledge_graph.ttl\"\n",
        "g.serialize(destination=output_file, format=\"turtle\")\n",
        "\n",
        "print(f\"Knowledge graph has been serialized to {output_file}\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x6bYckTpnwbQ",
        "outputId": "4d2c25aa-e828-4d51-b519-e1e93937b641"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Headers: ['ID', 'LocalDate', 'LocalTime', 'GMTDate', 'GMTTime', 'lat', 'long', 'Temperature', 'Speed', 'Direction', 'Altitude', 'Cov', 'HDOP', 'Distance', 'Count']\n",
            "Knowledge graph has been serialized to sensor_knowledge_graph.ttl\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Download the file\n",
        "files.download(output_file)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 37
        },
        "id": "IVnXoxRjoXrq",
        "outputId": "e62fe3cd-1e71-4bae-a67d-ce382e81f8de"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_edfeafde-7887-44dc-9297-1411ba828e9c\", \"sensor_knowledge_graph.ttl\", 529751)"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "_KM7pR2zolAi"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}

```python
!pip install rdflib

from google.colab import files
import pandas as pd
import csv
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, XSD

# Prompt for file upload
uploaded = files.upload()

# Read the uploaded CSV file into a pandas DataFrame
for filename in uploaded.keys():
    print('User uploaded file "{name}" with length {length} bytes'.format(
        name=filename, length=len(uploaded[filename])))
    df = pd.read_csv(filename)

# GPS collar
import csv
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, XSD

# Define namespaces
FOO = Namespace("https://w3id.org/def/foo#")
SOSA = Namespace("http://www.w3.org/ns/sosa/")
GEO = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")

# Create a new graph
g = Graph()

# Bind namespaces
g.bind("foo", FOO)
g.bind("sosa", SOSA)
g.bind("geo", GEO)

# Path to your CSV file
csv_file_path = "Jasmin.csv"  # Adjust the path accordingly

# Read and process data
with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    # Print headers for debugging
    print("Headers:", reader.fieldnames)

    for row in reader:
        identifier = row.get('ID', '').strip()
        local_date = row.get('LocalDate', '').strip()
        local_time = row.get('LocalTime', '').strip()
        gmt_date = row.get('GMTDate', '').strip()
        gmt_time = row.get('GMTTime', '').strip()
        lat = row.get('lat', '').strip()
        long = row.get('long', '').strip()
        temperature = row.get('Temperature', '').strip()
        speed = row.get('Speed', '').strip()
        direction = row.get('Direction', '').strip()
        altitude = row.get('Altitude', '').strip()
        cov = row.get('Cov', '').strip()
        hdop = row.get('HDOP', '').strip()
        distance = row.get('Distance', '').strip()
        count = row.get('Count', '').strip()

        # Create sensor URI
        sensor = URIRef(f"https://w3id.org/def/foo#{identifier}")
        g.add((sensor, RDF.type, FOO.Jasmin))
        g.add((sensor, FOO.ID, Literal(identifier, datatype=XSD.string)))
        g.add((sensor, FOO.hasFeatureOfInterest, FOO.ElephasMaximus))

        # Create observation URI
        observation = URIRef(f"https://w3id.org/def/foo#{identifier}")
        g.add((observation, RDF.type, FOO.Observation))
        g.add((observation, FOO.madeBySensor, sensor))  # Link sensor to observation

        # Add observation properties
        g.add((observation, FOO.LocalDate, Literal(local_date, datatype=XSD.date)))
        g.add((observation, FOO.LocalTime, Literal(local_time, datatype=XSD.time)))
        g.add((observation, FOO.GMTDate, Literal(gmt_date, datatype=XSD.date)))
        g.add((observation, FOO.GMTTime, Literal(gmt_time, datatype=XSD.time)))
        g.add((observation, FOO.Latitude, Literal(lat, datatype=XSD.double)))
        g.add((observation, FOO.Longitude, Literal(long, datatype=XSD.double)))

        # Add observable properties if available
        if temperature:
            g.add((observation, FOO.Temperature, Literal(temperature, datatype=XSD.double)))
        if speed:
            g.add((observation, FOO.Speed, Literal(speed, datatype=XSD.double)))
        if direction:
            g.add((observation, FOO.Direction, Literal(direction, datatype=XSD.integer)))
        if altitude:
            g.add((observation, FOO.Altitude, Literal(altitude, datatype=XSD.string)))
        if cov:
            g.add((observation, FOO.Cov, Literal(cov, datatype=XSD.double)))
        if hdop:
            g.add((observation, FOO.HDOP, Literal(hdop, datatype=XSD.double)))
        if distance:
            g.add((observation, FOO.Distance, Literal(distance, datatype=XSD.double)))
        if count:
            g.add((observation, FOO.Count, Literal(count, datatype=XSD.integer)))

# Serialize the graph to a file
output_file = "sensor_knowledge_graph.ttl"
g.serialize(destination=output_file, format="turtle")

print(f"Knowledge graph has been serialized to {output_file}")

# Download the file
files.download(output_file)


```python
# adding serialized data to stardog 

 conn_details = {
 'endpoint': 'http://localhost:5820',
 'username': 'admin',
  'password': 'admin'
 }
with stardog.Admin(**conn_details) as admin:
    Jasmin = admin.new_database('Jasmin')

 conn = stardog.Connection('Jasmin', **conn_details)

 conn.begin()

 conn.add(
    stardog.content.File('Jasmin.rdf', stardog.content_types.TURTLE),
)

 conn.commit()
```
