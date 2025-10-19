```json
{
  "id": "da77b2ee93bdd9c7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286121,
  "host_pid": "9e6742732c60:1",
  "hash": "c2b201b7123f6fcb52fb0ca5e9535051834016d6525b7566208573de602702ad",
  "cid": "QmV1c2b201b7123f6fcb52fb0ca5e9535051834016d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286121,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760286121
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "d5099bade325e6f6e55ff57d3215bad8fffe431076dd9909b50c072c7a0c2ebb"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000027727543
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': '30f273873102b27a'}}}