<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/staciekith/mental-unload">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Mental unload</h3>

  <p align="center">
    Free your mind from daily tasks.
    <br />
    <a href="https://github.com/staciekith/mental-unload"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/staciekith/mental-unload">View Demo</a>
    ·
    <a href="https://github.com/staciekith/mental-unload/issues">Report Bug</a>
    ·
    <a href="https://github.com/staciekith/mental-unload/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

API using Python and Flask to get handy with these technologies.

Following the principles of clean architecture / hexagonal architecture:
- separate user side, business logic and server side
- dependencies go to business logic (business logic does not depend on user side and server side)
- layers are isolated by adapters

### Entities
Entities represent the domain objects with plain objects. They encapsulate the most general and high-level rules. They are the least likely to change when something external changes.

### Use cases / business logic
Use cases represent the business actions with pure business logic. They define interfaces for the data they need and throws business exceptions. They orchestrate the flow of data to and from the entities.
They are to be used in APIs, cli commands, tasks, etc.

### Input DTOs
Input DTOs are immutable data structure used as arguments in the use cases' function. DTOs should be validated before being passed to use cases.

### Interface adapters
Interface adapters are wrappers used to call a third party API or another component (e.g. databases). This prevents the use cases / business logic to be polluted with irrelevant details and names. They convert data from the format most convenient for the use cases and entities, to the format most convenient for external components.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* pip3
* python3
* postgresql database
* virtualenv
  ```sh
  pip3 install virtualenv
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/staciekith/mental-unload.git
   ```
2. Create a virtual environment for your project
   ```sh
   make venv-create
   ```
3. Install Python packages
   ```sh
   make req
   ```
4. Create a `.env` file
   ```.env
   DATABASE_URL="postgresql://my-db-host/my-db-name"
   ```
5. Initialize and run the project
   ```sh
   make migration-gen
   make run
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Please refer to the [Postman collection](https://www.getpostman.com/collections/81c82ff4d5838ce2ad79) for usage exemples.


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Automatically create a reminder when an event is created as done
- [x] Create/update an event and even_type
- [x] Validations
- [x] Errors management
- [x] Tests repositories
- [x] Tests use cases
- [x] Tests endpoints
- [ ] Authentication / Authorization
- [ ] API documentation


See the [open issues](https://github.com/staciekith/mental-unload/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

KITH Stacie - [@orenjibean](https://twitter.com/orenjibean) - stae.dev@gmail.com

Project Link: [https://github.com/staciekith/mental-unload](https://github.com/staciekith/mental-unload)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/staciekith/mental-unload.svg?style=for-the-badge
[contributors-url]: https://github.com/staciekith/mental-unload/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/staciekith/mental-unload.svg?style=for-the-badge
[forks-url]: https://github.com/staciekith/mental-unload/network/members
[stars-shield]: https://img.shields.io/github/stars/staciekith/mental-unload.svg?style=for-the-badge
[stars-url]: https://github.com/staciekith/mental-unload/stargazers
[issues-shield]: https://img.shields.io/github/issues/staciekith/mental-unload.svg?style=for-the-badge
[issues-url]: https://github.com/staciekith/mental-unload/issues
[license-shield]: https://img.shields.io/github/license/staciekith/mental-unload.svg?style=for-the-badge
[license-url]: https://github.com/staciekith/mental-unload/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/staciekith
[product-screenshot]: images/screenshot.png
