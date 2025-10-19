```json
{
  "id": "7b08e1cfbab481c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287647,
  "host_pid": "9e6742732c60:1",
  "hash": "88ea0190f1c3ad8a7429bdc825070065394217d253c4a248dc6f3b1f0d399ded",
  "cid": "QmV188ea0190f1c3ad8a7429bdc825070065394217d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287647,
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
      "evaluated_at": 1760287647
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
  "sig": "e2472334682bbf59572cf1cd26f5d5749744ef04d1138c32e7d37c8415eea5d2"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 122105151005829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50, 'total_amount': 18128458, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285765, 'matching_hash': 'ea26f24e3d1967f5'}}}