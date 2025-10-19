```json
{
  "id": "06d70e495e41e2a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290811,
  "host_pid": "9e6742732c60:1",
  "hash": "0e8e8cd07b777d21313520c3674bb6c050727b795de42197905536909ce44c1a",
  "cid": "QmV10e8e8cd07b777d21313520c3674bb6c050727b79",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290811,
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
      "evaluated_at": 1760290811
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
  "sig": "f38d6b926dd8494dda62e2af94333656bccaf3e5756f1e1175d6a332a7d43c47"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277570300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 64715680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': '94740eaab516570d'}}}