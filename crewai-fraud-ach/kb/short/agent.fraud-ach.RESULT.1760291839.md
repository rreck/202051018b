```json
{
  "id": "d46573f2d2135132",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291839,
  "host_pid": "9e6742732c60:1",
  "hash": "7032230512b69fc22d59e08508a53b2742653a7e328f100972df974af06095d1",
  "cid": "QmV17032230512b69fc22d59e08508a53b2742653a7e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291839,
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
      "evaluated_at": 1760291839
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
  "sig": "7adada2cba14b1c80bd9fc9d30fdb3ebc5a43b9f4c9c6d1f3455464f6e6d6e59"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271240415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 21652016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285765, 'matching_hash': '8c20097da64de4ba'}}}