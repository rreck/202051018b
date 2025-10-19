```json
{
  "id": "90cb4c8545d870d0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292418,
  "host_pid": "9e6742732c60:1",
  "hash": "7ae70368c376ea58f13351ce5e29033691ad1c7dd4c7a89b99e0dc8624ed9f30",
  "cid": "QmV17ae70368c376ea58f13351ce5e29033691ad1c7d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292418,
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
      "evaluated_at": 1760292418
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
  "sig": "4a8a1461ba114de2f9e3e7de98d6af3801c3579d04b854d91df904a282440515"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026682072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 66226475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285764, 'matching_hash': 'ef2983ea6f6c1303'}}}