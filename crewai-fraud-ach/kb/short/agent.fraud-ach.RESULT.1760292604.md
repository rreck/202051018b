```json
{
  "id": "4afe397f4df102d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292604,
  "host_pid": "9e6742732c60:1",
  "hash": "2364651645b2ea724e2d510bed30c5fb99a8f5259701f9e7912e2955c2dc45d8",
  "cid": "QmV12364651645b2ea724e2d510bed30c5fb99a8f525",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292604,
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
      "evaluated_at": 1760292604
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
  "sig": "486fe7f02f577a7d7f0931a250eda3890fb856f2f6bd0021ae833e29eb05a3f5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273039049
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 68391657, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '71e11df02cc7494b'}}}