```json
{
  "id": "5325c670c04cf05a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288865,
  "host_pid": "9e6742732c60:1",
  "hash": "cdcd1193aa9b3f1d9a3fada05d787fe1699e1780e6830654694b8625693fe470",
  "cid": "QmV1cdcd1193aa9b3f1d9a3fada05d787fe1699e1780",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288865,
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
      "evaluated_at": 1760288865
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
  "sig": "a78add46446654ed3e4f4e1edf3e09e857532ec1621b20d6df8f2187c9f7946a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026887900
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 33964414, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285765, 'matching_hash': '21e48734f91c19c6'}}}