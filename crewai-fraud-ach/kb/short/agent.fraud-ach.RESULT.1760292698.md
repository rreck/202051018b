```json
{
  "id": "4b9ba4fbd2cff972",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292698,
  "host_pid": "9e6742732c60:1",
  "hash": "82fdbc767049b1e9e795f108ff5d34fff44441a3b02fe06128305485ab963d5c",
  "cid": "QmV182fdbc767049b1e9e795f108ff5d34fff44441a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292698,
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
      "evaluated_at": 1760292698
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
  "sig": "1f61552cf2482732ead55f3aa53d2720a06249822289a16a7a60f753f267a4fb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028850671
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 19296774, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': '07a264c4d7b66912'}}}