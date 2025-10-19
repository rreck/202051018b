```json
{
  "id": "d14629d1aced05ea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291275,
  "host_pid": "9e6742732c60:1",
  "hash": "5fa6ee5688f0307bb33068b4a3ca3c76a9be90a1543d081bc5cba48be5cc34cf",
  "cid": "QmV15fa6ee5688f0307bb33068b4a3ca3c76a9be90a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291275,
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
      "evaluated_at": 1760291275
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
  "sig": "ca887e9dee43db1cce559e786d6737bacef1215381b941c8e579d7b5fe0e1415"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272525723
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 15675912, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': '7f6b158faad48b99'}}}