```json
{
  "id": "b07498886fb9f5e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294061,
  "host_pid": "9e6742732c60:1",
  "hash": "bf57b866786430924443e6536d5503d3d247a40aa73f4f1fdfcebc97ce346305",
  "cid": "QmV1bf57b866786430924443e6536d5503d3d247a40a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294061,
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
      "evaluated_at": 1760294061
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
  "sig": "29bab14d875bc5efc123e1abbecfcca71a4fc7f99a857812c309dbb78195070e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036798243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 102123252, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '9f3869b775bbb8aa'}}}