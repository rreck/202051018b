```json
{
  "id": "1d6b2de66f5e31b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286864,
  "host_pid": "9e6742732c60:1",
  "hash": "fb525519f1ce3efa7a9c49c7c061665ae5617f1e3dbfdd045cbd83cd159f0a9c",
  "cid": "QmV1fb525519f1ce3efa7a9c49c7c061665ae5617f1e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286864,
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
      "evaluated_at": 1760286864
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "3c6ddbf9f796ef9157796590eb1756d6106040f7ffeee7d600f750a256128847"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100276193597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10149600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285763, 'matching_hash': 'c482c58c8f3e1991'}}}