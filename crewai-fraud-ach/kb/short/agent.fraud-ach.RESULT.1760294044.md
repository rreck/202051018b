```json
{
  "id": "0ad5de5adfb30e75",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294044,
  "host_pid": "9e6742732c60:1",
  "hash": "f955412029acc91890fb1e2e635d0f6cdbf4afa4cf2d7fb2878001bc1d9cd0b1",
  "cid": "QmV1f955412029acc91890fb1e2e635d0f6cdbf4afa4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294044,
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
      "evaluated_at": 1760294044
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
  "sig": "8e7b135e029fb840ffb74df74e5b27d109d31a37980a7f325c8c5a9644e6fc45"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022318038
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 55308560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285765, 'matching_hash': 'c47c52aff7a65053'}}}