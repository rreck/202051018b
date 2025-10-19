```json
{
  "id": "f09c63e5d4a6346e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293467,
  "host_pid": "9e6742732c60:1",
  "hash": "2b4be91de79d5f6028814ca50cb6bd5e720a9a559393b1d13383210ab418c149",
  "cid": "QmV12b4be91de79d5f6028814ca50cb6bd5e720a9a55",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293467,
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
      "evaluated_at": 1760293467
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
  "sig": "b3c557930b954f61dfd8edcc05b523c4e1e2b3bfceb49f447c57126e1ea04090"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155063461
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 68995512, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285764, 'matching_hash': '55217e698cd3f78f'}}}