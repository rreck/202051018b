```json
{
  "id": "caa5522c12ed062e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287909,
  "host_pid": "9e6742732c60:1",
  "hash": "9486df94e90fe48d7c4e5f20dfd96f59285bb036c37feaf888111c37bf1b53c6",
  "cid": "QmV19486df94e90fe48d7c4e5f20dfd96f59285bb036",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287909,
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
      "evaluated_at": 1760287909
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
  "sig": "68deef944822e83df4f770ebe19776173c0b49e9f1b18d5b96c3e09aa8ca1a03"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248914863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285765, 'matching_hash': '9c0338b7ffb65590'}}}