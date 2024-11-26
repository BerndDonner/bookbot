# run with:                nix develop
# see metadata with:       nix flake metadata
# debug with:              nix repl
#                          :lf .#
# check with:              nix flake check
# If you want to update a locked input to the latest version, you need to ask
# for it:                  nix flake lock --update-input nixpkgs
# show available packages: nix-env -qa
#                          nix search nixpkgs
# show nixos version:      nixos-version
# 

{
  description = "Boot.dev Environment for Nix 24.05";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-24.05";
  };

  outputs = { self, nixpkgs }: {
    devShells = {
      x86_64-linux.default  = self.buildDevShell "x86_64-linux";
      aarch64-linux.default = self.buildDevShell "aarch64-linux";
      x86_64-darwin.default = self.buildDevShell "x86_64-darwin";
    };
  } // {
    buildDevShell = system: let
      pkgs = import nixpkgs { inherit system; };
    in
      pkgs.mkShell {
        name = "impurePythonEnv";
        venvDir = "./.venv";

        packages = (with pkgs; [
          go
        ]) ++
        ([
          (pkgs.callPackage ./bootdev.nix {})
        ]);

        buildInputs = with pkgs; [
          python3Packages.python
          python3Packages.venvShellHook
        ];

        postVenvCreation = ''
          unset SOURCE_DATE_EPOCH
          pip install -r requirements.txt
        '';
      };
  };
}
