```json
{
  "id": "a29ff8f90e310c1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286271,
  "host_pid": "9e6742732c60:1",
  "hash": "bfbcc6ea98f9b2bd1c8d2089cb23564caac16f3040dfc2bfe1d63e0755e91d1e",
  "cid": "QmV1bfbcc6ea98f9b2bd1c8d2089cb23564caac16f30",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286271,
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
      "evaluated_at": 1760286271
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
  "sig": "10d823dc1ab8d350316dad2551be5a6120dd9e33dc9bd40ca8cf2ef24b8a490c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105150645649
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285763, 'matching_hash': 'dd1021bcf813c8ae'}}}