```json
{
  "id": "e506293ea68ee03b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289017,
  "host_pid": "9e6742732c60:1",
  "hash": "bf5445c03c1ac4d6e19024be621103eba00cbb05d12f24d9b9bd24aec2e98bd5",
  "cid": "QmV1bf5445c03c1ac4d6e19024be621103eba00cbb05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289017,
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
      "evaluated_at": 1760289018
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
  "sig": "fd7bf935a0e9e5d8c6df5a9d2114e65fcfc78db0491e3eb0f45d9be525e6dcc8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029303857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 29008074, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285763, 'matching_hash': '4510d576292a5401'}}}