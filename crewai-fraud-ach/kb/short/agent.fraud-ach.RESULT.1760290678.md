```json
{
  "id": "03a9abc84ccc57a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290678,
  "host_pid": "9e6742732c60:1",
  "hash": "15d3131edfc12133cc28e4d59a6be60a9205305b1b7eeea5c4827a2c04285d5a",
  "cid": "QmV115d3131edfc12133cc28e4d59a6be60a9205305b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290678,
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
      "evaluated_at": 1760290678
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
  "sig": "f425739e3770af4675390d8bb76876479f26f585ea8ec31ecc9b16934866639f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592096226
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 77005032, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285765, 'matching_hash': '5e92eb8585c87013'}}}