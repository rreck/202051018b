```json
{
  "id": "78aa4b107def68ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291369,
  "host_pid": "9e6742732c60:1",
  "hash": "0c2c5716ad3b5b4454d7c8f65ce077b6462b722ef65e77dc9be6831d3d8aac39",
  "cid": "QmV10c2c5716ad3b5b4454d7c8f65ce077b6462b722e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291369,
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
      "evaluated_at": 1760291369
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
  "sig": "3ffba01343f6ee3f298458c797e6894f999e51a557d77b71310fc6e14e7030d3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153385568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': '556aff2bced704f0'}}}