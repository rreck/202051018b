```json
{
  "id": "c5191d793b625313",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287318,
  "host_pid": "9e6742732c60:1",
  "hash": "ee18ed908e4ad6848d3e95ae4be2365ce5fb123852f8a48a0a6212e45b92744d",
  "cid": "QmV1ee18ed908e4ad6848d3e95ae4be2365ce5fb1238",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287318,
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
      "evaluated_at": 1760287318
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
  "sig": "43acfcc576e4a13795f55a3a267a2e07c7a1cae3db09ec72c050437baaecead1"
}
```

Fraud detected: duplicate_transaction (score: 73)
Transaction: 021000023218255
Details: {'velocity': {'fraud_detected': True, 'risk_score': 62, 'details': {'transaction_count': 56, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285763, 'matching_hash': '1151ecc015fd8f1a'}}}