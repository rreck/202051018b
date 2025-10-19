```json
{
  "id": "dde6baca15fb4de3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289026,
  "host_pid": "9e6742732c60:1",
  "hash": "258f140f9c8899f7ad5aafaac0700fdbdb356984be258f00c7ea0177f3af1f75",
  "cid": "QmV1258f140f9c8899f7ad5aafaac0700fdbdb356984",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289026,
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
      "evaluated_at": 1760289026
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
  "sig": "e48b943e4b48daba49c1f205422a05d4d86308f188cabcd671001ad6f38bf002"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021395098
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 40051686, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285765, 'matching_hash': '9c6ceec1730a6176'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '033505362', 'validation_error': 'Invalid routing number checksum'}}}