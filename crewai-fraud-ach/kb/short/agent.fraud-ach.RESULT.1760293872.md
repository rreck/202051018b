```json
{
  "id": "ea57bf349b998d64",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293872,
  "host_pid": "9e6742732c60:1",
  "hash": "0d57eb18d3ace7d0516f13730c3e8e0575d04e4130d20eccb1eab7e69c9b9094",
  "cid": "QmV10d57eb18d3ace7d0516f13730c3e8e0575d04e41",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293872,
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
      "evaluated_at": 1760293872
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
  "sig": "374928dcab87cdba5f9b2aca479edc180227c5b068eeb05ea36158de0d300a8d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037507630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 81888888, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '9b4ed9a2b11bf5fa'}}}