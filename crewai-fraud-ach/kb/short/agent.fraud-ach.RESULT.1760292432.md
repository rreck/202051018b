```json
{
  "id": "1d6063bfe5f0b382",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292432,
  "host_pid": "9e6742732c60:1",
  "hash": "0734ce998761ad283effbb47f0a64d65d91a2f0a21dc26ed4c215219a49e53ca",
  "cid": "QmV10734ce998761ad283effbb47f0a64d65d91a2f0a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292432,
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
      "evaluated_at": 1760292432
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
  "sig": "7a5ea79a1509112ef12ef6832f18968d190c2759566d8592e9d78aae0cf6b866"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035733360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 64668402, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285765, 'matching_hash': '19d9911872be19af'}}}