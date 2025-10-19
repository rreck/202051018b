```json
{
  "id": "9222378c235087e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285865,
  "host_pid": "9e6742732c60:1",
  "hash": "1fd0541ba051012161cde6f08830a06f05908817df82469945a5b74038745ce6",
  "cid": "QmV11fd0541ba051012161cde6f08830a06f05908817",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285865,
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
      "evaluated_at": 1760285865
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
  "sig": "64307cedeec5ac3e04d57d4fe82741fd75440b6e7b26df0907c95c60fb1eb668"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000249881393
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760285763, 'matching_hash': '72e20928773d23d6'}}}