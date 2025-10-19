```json
{
  "id": "036282efc29a7eaa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289968,
  "host_pid": "9e6742732c60:1",
  "hash": "124585ebfce9e6ff8a80f7e9700dae5444a9ec18e4d7ec8bdc6a64eee641f4f3",
  "cid": "QmV1124585ebfce9e6ff8a80f7e9700dae5444a9ec18",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289968,
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
      "evaluated_at": 1760289968
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
  "sig": "a562ece86703420f919359ab99133e8f4801c5759a3cdf037f212e6a9f84d7a1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463967385
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 49840218, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285763, 'matching_hash': 'becd1833b82f29ed'}}}