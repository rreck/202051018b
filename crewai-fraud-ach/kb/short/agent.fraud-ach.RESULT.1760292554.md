```json
{
  "id": "add6c1aace3c817d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292554,
  "host_pid": "9e6742732c60:1",
  "hash": "53af5ef8e1a2353a09db7f7024036b7bb7df0721ca24463528556bd42120f51c",
  "cid": "QmV153af5ef8e1a2353a09db7f7024036b7bb7df0721",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292554,
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
      "evaluated_at": 1760292554
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
  "sig": "395c96cc16e2cfe143966f00822221fa559719c7f997094e119466de4f6c1c6d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466771941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 73597800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': 'aa929aac6878f78f'}}}