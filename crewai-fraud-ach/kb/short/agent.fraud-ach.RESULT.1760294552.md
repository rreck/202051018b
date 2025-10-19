```json
{
  "id": "7c1a329d5ea2ccee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294552,
  "host_pid": "9e6742732c60:1",
  "hash": "07267966d5310c1fa84f136cf4313f8e999a86d75d6a97b0c1cf3f00ae521d6a",
  "cid": "QmV107267966d5310c1fa84f136cf4313f8e999a86d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294552,
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
      "evaluated_at": 1760294552
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
  "sig": "17578db0d8d816dfcca2287a449290b957cb07410225f1bb5fcb6fd7e21294ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032365153
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 95134800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285764, 'matching_hash': 'db9686895aceb522'}}}