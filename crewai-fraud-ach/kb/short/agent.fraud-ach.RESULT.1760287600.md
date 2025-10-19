```json
{
  "id": "db05ea9b5c92b5e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287600,
  "host_pid": "9e6742732c60:1",
  "hash": "3e2a8c79782b4c6026d53c77ee36ff91b37fa92c4267c606cc4413e4e25c67a5",
  "cid": "QmV13e2a8c79782b4c6026d53c77ee36ff91b37fa92c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287600,
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
      "evaluated_at": 1760287600
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
  "sig": "64a3e868d7de9a499c6b2b33178342f432bb8740a1da5a3b2c3775a663344086"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 044000035593386
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285763, 'matching_hash': '6253d15ae41563d2'}}}