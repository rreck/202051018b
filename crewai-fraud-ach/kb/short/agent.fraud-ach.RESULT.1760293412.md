```json
{
  "id": "1293a45e79cf3058",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293412,
  "host_pid": "9e6742732c60:1",
  "hash": "fab4c023be87eecb0571b4183e59f0ff5c6b053d778eb9fb1dbae53e158965db",
  "cid": "QmV1fab4c023be87eecb0571b4183e59f0ff5c6b053d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293412,
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
      "evaluated_at": 1760293412
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
  "sig": "7aedeac742da66c2811bcf85d1ee5439a9eded13f70d92c0f14d95c5b9cbd6bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464554990
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 59538634, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': 'ab9afd20a22fc7b8'}}}