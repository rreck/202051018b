```json
{
  "id": "36334865caeaf843",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290119,
  "host_pid": "9e6742732c60:1",
  "hash": "86fbfca2122bec74aa82b870dd430ae16980b9e7e92f6f55f0406d2179b61a1a",
  "cid": "QmV186fbfca2122bec74aa82b870dd430ae16980b9e7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290119,
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
      "evaluated_at": 1760290119
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
  "sig": "009416efc8a14112f3f40206bf66a5a04ee5a66dab157523f69f984ef31cb93c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243661505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 59351172, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285764, 'matching_hash': '37851bbce8ea73db'}}}