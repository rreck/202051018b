```json
{
  "id": "09077c5812b59394",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294388,
  "host_pid": "9e6742732c60:1",
  "hash": "f83f67458bf6428e157f15a68dc02c6a1fdf7a867387f3be10c405f1268b04a6",
  "cid": "QmV1f83f67458bf6428e157f15a68dc02c6a1fdf7a86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294388,
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
      "evaluated_at": 1760294388
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
  "sig": "50c9ed6d4fdfc7ef0044b2536d10b6a1f6ff783ab5a6bac6c60aa770b4c44be4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276380856
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 113439576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285764, 'matching_hash': '152950ce26814ef6'}}}