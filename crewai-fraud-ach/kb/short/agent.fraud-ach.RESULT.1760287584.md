```json
{
  "id": "16ef05c279dffad0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287584,
  "host_pid": "9e6742732c60:1",
  "hash": "d537211830029c7d0e5baf65e12a104c18c35543e9ea6100382e516c6e178202",
  "cid": "QmV1d537211830029c7d0e5baf65e12a104c18c35543",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287584,
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
      "evaluated_at": 1760287584
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
  "sig": "c96ca4c379ad068bdd502e7c7daab45dc3a7023843d898c9abe67e5d9d77e8cd"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 021000029513246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285764, 'matching_hash': '556e5d87a3998e0a'}}}