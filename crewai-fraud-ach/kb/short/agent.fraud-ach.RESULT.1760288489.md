```json
{
  "id": "204bf1ac94ca66d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288489,
  "host_pid": "9e6742732c60:1",
  "hash": "0b4ffefb166d0f7f1842a74912d19aaa53aab7be56bfd42ad0bb27720f778e47",
  "cid": "QmV10b4ffefb166d0f7f1842a74912d19aaa53aab7be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288489,
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
      "evaluated_at": 1760288489
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
  "sig": "2cb0b16c51e00a8947fd1545a1a1ef422a52c147d845bb781beb065a26b32353"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022915367
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 39497675, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285763, 'matching_hash': '4fdfaefd2437a484'}}}