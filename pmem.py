#!/usr/bin/env python3
"""
pmem 1.0 - Biomimicry-driven persistent memory for CrewAI agents
Auditable, on-prem, emergent group-think via structured files
"""

import json
import hashlib
import time
import os
import re
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from pathlib import Path
from collections import defaultdict
import math

# Constants per spec
TAU_DAYS = 7  # co-occurrence window
LAMBDA_DECAY = 0.01  # weight decay per day
CLUSTER_MIN_SOURCES = 5
CLUSTER_MIN_WEIGHT = 0.6
SYNTHESIS_MIN_CLUSTERS = 2
SYNTHESIS_MAX_JS_DIV = 0.25
CONSENSUS_MIN_QUORUM = 0.67
UPDATE_THRESHOLD = 0.05
MAX_ATOMIC_KB = 64
MAX_ROLLUP_KB = 512

# Valid keys per spec
VALID_KEYS = {
    "IDEA", "TASK", "PROBLEM", "ACTION", "RESULT", "LESSON",
    "CLUSTER", "SYNTHESIS", "META", "ECHO", "CONSENSUS"
}

ATOMIC_KEYS = {"IDEA", "TASK", "PROBLEM", "ACTION", "RESULT", "LESSON"}
EMERGENT_KEYS = {"CLUSTER", "SYNTHESIS", "META", "ECHO", "CONSENSUS"}


@dataclass
class AICP:
    """AI Content Provenance headers"""
    prov: Dict[str, Any]  # Verifiable Credential
    ucon: Dict[str, Any]  # Usage Control constraints
    eval: Dict[str, Any]  # Evaluation metadata


@dataclass
class Edge:
    """Bidirectional link between artifacts"""
    source_id: str
    target_id: str
    weight: float
    last_updated: int


@dataclass
class PMemHeader:
    """Machine-readable header for all pmem artifacts"""
    id: str
    scope: str  # agent or crew
    key: str
    epoch: int
    host_pid: str
    hash: str
    cid: str  # content-addressable ID
    aicp: AICP
    sources: List[str]
    edges: List[Dict[str, Any]]
    metrics: Dict[str, Any]
    thresholds: Dict[str, Any]
    tags: List[str]
    sig: str


class PMemSystem:
    """Core pmem 1.0 implementation"""

    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.kb_short = self.base_path / "kb" / "short"
        self.kb_long = self.base_path / "kb" / "long"
        self.kb_short.mkdir(parents=True, exist_ok=True)
        self.kb_long.mkdir(parents=True, exist_ok=True)

        # In-memory edge graph
        self.edges: Dict[Tuple[str, str], Edge] = {}

    def get_epoch(self) -> int:
        """Get current Unix epoch in seconds"""
        return int(time.time())

    def get_host_pid(self) -> str:
        """Get host and PID identifier"""
        import socket
        return f"{socket.gethostname()}:{os.getpid()}"

    def compute_hash(self, content: str) -> str:
        """Compute SHA-256 hash of content"""
        return hashlib.sha256(content.encode()).hexdigest()

    def compute_cid(self, data: Dict) -> str:
        """Compute content-addressable ID"""
        canonical = json.dumps(data, sort_keys=True)
        return f"cid:{hashlib.sha256(canonical.encode()).hexdigest()[:16]}"

    def generate_filename(self, scope: str, key: str, epoch: int) -> str:
        """Generate strict filename: <scope>.<KEY>.<EPOCH>.md"""
        if key not in VALID_KEYS:
            raise ValueError(f"Invalid key: {key}. Must be one of {VALID_KEYS}")
        if scope not in ["agent", "crew"]:
            raise ValueError(f"Invalid scope: {scope}. Must be 'agent' or 'crew'")
        return f"{scope}.{key}.{epoch}.md"

    def create_aicp(self, issuer: str, context: Dict = None) -> AICP:
        """Create AICP headers with provenance"""
        epoch = self.get_epoch()

        prov = {
            "@context": "https://www.w3.org/2018/credentials/v1",
            "type": ["VerifiableCredential", "AIContentProvenance"],
            "issuer": issuer,
            "issuanceDate": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(epoch)),
            "credentialSubject": {
                "id": f"urn:uuid:{os.urandom(16).hex()}",
                "timestamp": epoch,
                "host_pid": self.get_host_pid()
            }
        }

        ucon = {
            "constraints": context.get("constraints", []) if context else [],
            "obligations": context.get("obligations", []) if context else [],
            "permissions": context.get("permissions", ["read"]) if context else ["read"]
        }

        eval_data = {
            "quality": context.get("quality", 0.0) if context else 0.0,
            "confidence": context.get("confidence", 0.0) if context else 0.0,
            "reviewers": context.get("reviewers", []) if context else []
        }

        return AICP(prov=prov, ucon=ucon, eval=eval_data)

    def create_artifact(
        self,
        scope: str,
        key: str,
        body: str,
        sources: List[str] = None,
        tags: List[str] = None,
        metrics: Dict[str, Any] = None,
        issuer: str = "pmem-system"
    ) -> Tuple[str, PMemHeader]:
        """Create a new pmem artifact with full headers"""

        epoch = self.get_epoch()
        filename = self.generate_filename(scope, key, epoch)

        # Build header
        sources = sources or []
        tags = tags or []
        metrics = metrics or {}

        artifact_id = f"{scope}.{key}.{epoch}"
        content_hash = self.compute_hash(body)

        header = PMemHeader(
            id=artifact_id,
            scope=scope,
            key=key,
            epoch=epoch,
            host_pid=self.get_host_pid(),
            hash=content_hash,
            cid=self.compute_cid({"body": body, "epoch": epoch}),
            aicp=self.create_aicp(issuer),
            sources=sources,
            edges=[],
            metrics=metrics,
            thresholds={
                "tau_days": TAU_DAYS,
                "lambda_decay": LAMBDA_DECAY,
                "cluster_min_sources": CLUSTER_MIN_SOURCES,
                "cluster_min_weight": CLUSTER_MIN_WEIGHT
            },
            tags=tags,
            sig=""  # Placeholder for digital signature
        )

        # Compute signature over header (excluding sig field itself)
        header_dict_for_sig = asdict(header)
        header_dict_for_sig["sig"] = ""
        header_json = json.dumps(header_dict_for_sig, sort_keys=True)
        header.sig = self.compute_hash(header_json)

        return filename, header

    def write_artifact(
        self,
        scope: str,
        key: str,
        body: str,
        sources: List[str] = None,
        tags: List[str] = None,
        metrics: Dict[str, Any] = None,
        issuer: str = "pmem-system"
    ) -> str:
        """Write artifact to filesystem"""

        # Normalize body (strip trailing whitespace to ensure hash consistency)
        body = body.strip()

        filename, header = self.create_artifact(scope, key, body, sources, tags, metrics, issuer)

        # Determine directory
        target_dir = self.kb_short if key in ATOMIC_KEYS else self.kb_long
        filepath = target_dir / filename

        # Build file content (serialize AICP properly)
        header_dict = asdict(header)
        header_block = "```json\n" + json.dumps(header_dict, indent=2) + "\n```\n\n"
        full_content = header_block + body + "\n"  # Add trailing newline

        # Check size limits
        size_kb = len(full_content.encode()) / 1024
        max_kb = MAX_ATOMIC_KB if key in ATOMIC_KEYS else MAX_ROLLUP_KB
        if size_kb > max_kb:
            raise ValueError(f"Artifact exceeds {max_kb} KB limit: {size_kb:.1f} KB")

        # Write atomically
        filepath.write_text(full_content)

        # Update edges if sources exist
        if sources:
            for src_id in sources:
                self.add_edge(src_id, header.id, 1.0)

        return str(filepath)

    def read_artifact(self, filepath: str) -> Tuple[PMemHeader, str]:
        """Read and parse artifact from filesystem"""
        content = Path(filepath).read_text()

        # Extract JSON header
        match = re.search(r'```json\n(.*?)\n```', content, re.DOTALL)
        if not match:
            raise ValueError("No JSON header found in artifact")

        header_json = json.loads(match.group(1))

        # Reconstruct AICP
        aicp_data = header_json["aicp"]
        aicp = AICP(
            prov=aicp_data["prov"],
            ucon=aicp_data["ucon"],
            eval=aicp_data["eval"]
        )

        # Reconstruct header
        header = PMemHeader(
            id=header_json["id"],
            scope=header_json["scope"],
            key=header_json["key"],
            epoch=header_json["epoch"],
            host_pid=header_json["host_pid"],
            hash=header_json["hash"],
            cid=header_json["cid"],
            aicp=aicp,
            sources=header_json["sources"],
            edges=header_json["edges"],
            metrics=header_json["metrics"],
            thresholds=header_json["thresholds"],
            tags=header_json["tags"],
            sig=header_json["sig"]
        )

        # Extract body
        body = content[match.end():].strip()

        # Verify hash
        computed_hash = self.compute_hash(body)
        if computed_hash != header.hash:
            raise ValueError(f"Hash mismatch in {filepath}")

        return header, body

    def add_edge(self, source_id: str, target_id: str, weight: float):
        """Add or update edge between artifacts"""
        weight = max(0.0, min(1.0, weight))  # clip [0,1]
        edge = Edge(source_id, target_id, weight, self.get_epoch())
        self.edges[(source_id, target_id)] = edge

    def decay_weights(self):
        """Apply exponential weight decay based on time"""
        current_epoch = self.get_epoch()

        for key, edge in list(self.edges.items()):
            days_elapsed = (current_epoch - edge.last_updated) / 86400
            decay_factor = math.exp(-LAMBDA_DECAY * days_elapsed)
            new_weight = edge.weight * decay_factor

            if new_weight < 0.001:  # prune negligible edges
                del self.edges[key]
            else:
                edge.weight = max(0.0, min(1.0, new_weight))

    def find_clusters(self) -> List[Dict[str, Any]]:
        """Find clusters meeting threshold criteria"""
        self.decay_weights()

        # Group edges by target
        targets = defaultdict(list)
        for (src, tgt), edge in self.edges.items():
            if edge.weight >= CLUSTER_MIN_WEIGHT:
                targets[tgt].append((src, edge.weight))

        clusters = []
        for tgt, sources in targets.items():
            if len(sources) >= CLUSTER_MIN_SOURCES:
                clusters.append({
                    "target": tgt,
                    "sources": [{"id": src, "weight": w} for src, w in sources],
                    "count": len(sources),
                    "avg_weight": sum(w for _, w in sources) / len(sources)
                })

        return clusters

    def create_cluster(
        self,
        scope: str,
        members: List[Dict[str, Any]],
        summary: str,
        pattern: str,
        issuer: str = "pmem-consolidation"
    ) -> str:
        """Create CLUSTER emergent artifact"""

        source_ids = [m["id"] for m in members]
        avg_weight = sum(m["weight"] for m in members) / len(members)

        body = f"""# CLUSTER

## Summary
{summary}

## Members ({len(members)})
{chr(10).join(f"- {m['id']} (weight: {m['weight']:.3f})" for m in members)}

## Pattern
{pattern}

## Governance
- Co-occurrence window: {TAU_DAYS} days
- Weight decay: {LAMBDA_DECAY}/day
- Average weight: {avg_weight:.3f}

## Next Steps
Eligible for SYNTHESIS if ≥{SYNTHESIS_MIN_CLUSTERS} clusters with JS divergence ≤{SYNTHESIS_MAX_JS_DIV}
"""

        metrics = {
            "member_count": len(members),
            "avg_weight": avg_weight,
            "pattern_type": pattern
        }

        return self.write_artifact(
            scope=scope,
            key="CLUSTER",
            body=body,
            sources=source_ids,
            metrics=metrics,
            issuer=issuer
        )

    def verify_provenance(self, filepath: str) -> bool:
        """Verify AICP-PROV verifiable credential"""
        try:
            header, _ = self.read_artifact(filepath)

            # Check required AICP fields
            if not header.aicp.prov.get("issuer"):
                return False
            if not header.aicp.prov.get("credentialSubject"):
                return False

            # Verify signature (same logic as creation)
            header_dict_for_sig = asdict(header)
            header_dict_for_sig["sig"] = ""
            original_sig = header.sig
            computed_sig = self.compute_hash(json.dumps(header_dict_for_sig, sort_keys=True))

            return computed_sig == original_sig

        except Exception:
            return False

    def check_ucon_conflict(self, artifacts: List[str]) -> bool:
        """Check for UCON constraint conflicts across artifacts"""
        constraints_sets = []

        for filepath in artifacts:
            try:
                header, _ = self.read_artifact(filepath)
                constraints_sets.append(set(header.aicp.ucon.get("constraints", [])))
            except Exception:
                return True  # Error = conflict

        # Check for contradictory constraints (simplified)
        for i, cs1 in enumerate(constraints_sets):
            for cs2 in constraints_sets[i+1:]:
                # Check for explicit conflicts (e.g., "no-export" vs "allow-export")
                if any(c.startswith("no-") and c[3:] in cs2 for c in cs1):
                    return True
                if any(c.startswith("no-") and c[3:] in cs1 for c in cs2):
                    return True

        return False

    def list_artifacts(self, key: Optional[str] = None) -> List[str]:
        """List all artifacts, optionally filtered by key"""
        artifacts = []

        for directory in [self.kb_short, self.kb_long]:
            for filepath in directory.glob("*.md"):
                if key:
                    if f".{key}." in filepath.name:
                        artifacts.append(str(filepath))
                else:
                    artifacts.append(str(filepath))

        return sorted(artifacts)


def main():
    """Example usage of pmem 1.0"""

    pmem = PMemSystem()

    print("pmem 1.0 initialized")
    print(f"kb/short: {pmem.kb_short}")
    print(f"kb/long: {pmem.kb_long}")

    # Create example atomic artifact
    filepath = pmem.write_artifact(
        scope="agent",
        key="IDEA",
        body="Implement bidirectional edge tracking with time-decay weights",
        tags=["architecture", "pmem"],
        metrics={"priority": 0.9},
        issuer="example-agent"
    )

    print(f"\nCreated: {filepath}")

    # Read it back
    header, body = pmem.read_artifact(filepath)
    print(f"Verified hash: {header.hash[:16]}...")
    print(f"AICP issuer: {header.aicp.prov['issuer']}")

    # Verify provenance
    is_valid = pmem.verify_provenance(filepath)
    print(f"Provenance valid: {is_valid}")


if __name__ == "__main__":
    main()
