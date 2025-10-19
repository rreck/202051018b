```json
{
  "id": "c3c47bc1c8bd8ccb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287441,
  "host_pid": "9e6742732c60:1",
  "hash": "1e8f2b8e3011b734cc3bd7143ffc6635e9edd820c4a43afe39727daa53b89574",
  "cid": "QmV11e8f2b8e3011b734cc3bd7143ffc6635e9edd820",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287441,
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
      "evaluated_at": 1760287441
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "9c560de920b7f499a390fd656cc558e4dab2097c36f03d5799854108ff8a1134"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000021053905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50, 'total_amount': 15268200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285764, 'matching_hash': '608646e34fdf4d5c'}}}