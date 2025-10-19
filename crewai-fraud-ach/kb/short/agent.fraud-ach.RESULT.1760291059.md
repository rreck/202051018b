```json
{
  "id": "2fad959c5d384b12",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291059,
  "host_pid": "9e6742732c60:1",
  "hash": "1bad4bf37729666d52b38e5a7fa351f9984c93260b070642924bb2768c22e72b",
  "cid": "QmV11bad4bf37729666d52b38e5a7fa351f9984c9326",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291059,
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
      "evaluated_at": 1760291059
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
  "sig": "a9793c174c70c08a3ef2afef95f106b23148d235b8d1cd4664f597b8653191d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243661505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 69382356, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285764, 'matching_hash': '37851bbce8ea73db'}}}