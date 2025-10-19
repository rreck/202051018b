```json
{
  "id": "3ce9c38477fb2161",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292197,
  "host_pid": "9e6742732c60:1",
  "hash": "a83b2d4ce73bc03fe28bbf872e4365429b664442ef2f33a22672407c90beb1fe",
  "cid": "QmV1a83b2d4ce73bc03fe28bbf872e4365429b664442",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292197,
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
      "evaluated_at": 1760292198
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
  "sig": "b5158ff5ae62b2d0573475d30630ef5b61bf0e0be491f71505d3c0f6a0d94013"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240116635
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 72924096, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': 'faa8e9f78afe3726'}}}