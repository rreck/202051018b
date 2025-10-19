```json
{
  "id": "8e1b57e46276c885",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294068,
  "host_pid": "9e6742732c60:1",
  "hash": "08cbc4c7f6480e0285e9e76ac4f380f0fe5bb7c3e8d3323103ff67507fb23f3f",
  "cid": "QmV108cbc4c7f6480e0285e9e76ac4f380f0fe5bb7c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294068,
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
      "evaluated_at": 1760294068
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
  "sig": "3c9dc6244efd75da377c9771f54102730267be62cf4f3a25e15932aa984ff56c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243661505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 96550146, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285764, 'matching_hash': '37851bbce8ea73db'}}}