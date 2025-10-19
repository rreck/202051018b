```json
{
  "id": "4326113fa18005fc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285872,
  "host_pid": "9e6742732c60:1",
  "hash": "27cd19270e4c1406b5997dcf0538fca021fae4cf4403bcc88e0783d98b97102d",
  "cid": "QmV127cd19270e4c1406b5997dcf0538fca021fae4cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285872,
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
      "evaluated_at": 1760285872
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
  "sig": "52f70873c15e9810e6c373b0a09e2ba8ed45756ae5ab70cb8de29e122e13c7b8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241250323
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760285763, 'matching_hash': 'd18939bbbb7c2a14'}}}