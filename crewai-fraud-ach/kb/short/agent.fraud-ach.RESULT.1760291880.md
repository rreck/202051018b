```json
{
  "id": "555e18a9d05e7c00",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291880,
  "host_pid": "9e6742732c60:1",
  "hash": "7858abcb68065db67571226c964b07bda8ceae0104018ca0093630facc9699dc",
  "cid": "QmV17858abcb68065db67571226c964b07bda8ceae01",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291880,
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
      "evaluated_at": 1760291880
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
  "sig": "a77c07be487831dd7dd5658797eac199625e9caf17cf1eb12397ea6bb7c9e1f3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278037585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 19649960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': '27cb7a10328c75d5'}}}