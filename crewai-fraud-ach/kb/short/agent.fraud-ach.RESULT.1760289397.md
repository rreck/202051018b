```json
{
  "id": "0645e461384403c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289397,
  "host_pid": "9e6742732c60:1",
  "hash": "cc0afcf0e7ef1ece26e2de0cc9dddb1c21858a308fdc88ddbf7506f6c1f71178",
  "cid": "QmV1cc0afcf0e7ef1ece26e2de0cc9dddb1c21858a30",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289397,
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
      "evaluated_at": 1760289397
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
  "sig": "8837af6d966128d19ddafdf5096f38d747409473d3f0e051527e089741b77df9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031152991
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 14743578, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285763, 'matching_hash': '75441ab8b948ac4d'}}}