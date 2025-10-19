```json
{
  "id": "6275d62301979764",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289909,
  "host_pid": "9e6742732c60:1",
  "hash": "2bee181e79a51154d3f9b19f7e0ef4ce49b50b4320de438c571c958094e3dd66",
  "cid": "QmV12bee181e79a51154d3f9b19f7e0ef4ce49b50b43",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289909,
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
      "evaluated_at": 1760289909
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
  "sig": "942efac1b229cf27ff0839c8458745e394567ff41bae068708e19a051f6dd81b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242634243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 60941464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285764, 'matching_hash': '8925ee68733f12e3'}}}