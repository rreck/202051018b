```json
{
  "id": "9ea30e6ed1dfeceb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291660,
  "host_pid": "9e6742732c60:1",
  "hash": "697ad179a5c4272b6f9794e19f9c69124affa32fc592b6769968b9f438809a47",
  "cid": "QmV1697ad179a5c4272b6f9794e19f9c69124affa32f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291660,
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
      "evaluated_at": 1760291660
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
  "sig": "c31f74fbdc64db24c17b5873122b79b45351b02558d23eab7c28b3db5f1429a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032306947
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 13878900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': '0095d1181b74b3e8'}}}