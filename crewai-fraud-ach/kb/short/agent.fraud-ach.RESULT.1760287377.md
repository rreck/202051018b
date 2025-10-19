```json
{
  "id": "6277a25e9426c649",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287377,
  "host_pid": "9e6742732c60:1",
  "hash": "16220373ac2078ffb8836b4ea551fc3a16dfab42b6562b8d461f5f25177719bc",
  "cid": "QmV116220373ac2078ffb8836b4ea551fc3a16dfab42",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287377,
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
      "evaluated_at": 1760287377
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
  "sig": "b47ffeddd2a0109cc8ab11bff322127d4b8b9e9069bb95dacf2c7916ccddc824"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000240814513
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 17170784, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285763, 'matching_hash': '8ef20234ae18fb17'}}}