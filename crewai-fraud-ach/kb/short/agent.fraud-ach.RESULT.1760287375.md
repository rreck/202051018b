```json
{
  "id": "dfa009e7dbee1fec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287375,
  "host_pid": "9e6742732c60:1",
  "hash": "49a6a84c1c24ba775587a5878f8022e2b247ce9b0f3625911eea6935dd260e19",
  "cid": "QmV149a6a84c1c24ba775587a5878f8022e2b247ce9b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287375,
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
      "evaluated_at": 1760287375
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
  "sig": "d95acbc86e5c0c92e74354291bf63b6db4d3a0387201ecd39641d8ce607c8918"
}
```

Fraud detected: duplicate_transaction (score: 75)
Transaction: 121000244346820
Details: {'velocity': {'fraud_detected': True, 'risk_score': 66, 'details': {'transaction_count': 58, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285763, 'matching_hash': 'e760cf0efa3150cb'}}}een': 1760285763, 'matching_hash': '86add4fc1587ca1b'}}}