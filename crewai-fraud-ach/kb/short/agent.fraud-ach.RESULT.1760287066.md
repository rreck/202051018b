```json
{
  "id": "323fc0fe99327ebb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287066,
  "host_pid": "9e6742732c60:1",
  "hash": "3f0b99ab5624dba40e6269fda2c68754080f38dd0c2d6caf9748895f70b308a0",
  "cid": "QmV13f0b99ab5624dba40e6269fda2c68754080f38dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287066,
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
      "evaluated_at": 1760287066
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
  "sig": "af53050c4dfe0ec8d82b4c6946f75f56ba0073089605180d3aef90b6f4058ce5"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000241053391
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 20138701, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285763, 'matching_hash': '6e04470f15e4fc18'}}}