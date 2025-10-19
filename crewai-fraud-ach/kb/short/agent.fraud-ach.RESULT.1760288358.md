```json
{
  "id": "4edb44ac3b0db2d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288358,
  "host_pid": "9e6742732c60:1",
  "hash": "4ec72b7615a83f4783b10a620ef7db69b148073b17094972c9e3dc9322063e68",
  "cid": "QmV14ec72b7615a83f4783b10a620ef7db69b148073b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288358,
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
      "evaluated_at": 1760288358
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
  "sig": "7ddab9eee81c46763dadb14f08615385163ef23944eb0cfd3146f9a25150910f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027703590
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 32746623, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285763, 'matching_hash': '3a097b663e3dde58'}}}