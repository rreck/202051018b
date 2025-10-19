```json
{
  "id": "6e6ce451f7c67517",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294449,
  "host_pid": "9e6742732c60:1",
  "hash": "e2f1ce1369a6c7d1954d802ac23c7a2ba916bfaa52e3576eb0919d081b922786",
  "cid": "QmV1e2f1ce1369a6c7d1954d802ac23c7a2ba916bfaa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294449,
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
      "evaluated_at": 1760294449
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
  "sig": "5dbb3359bd1e8eff18bd0c0c70b5c25e5170d2fbd38400f60df3978ba511dfaf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245087309
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 105794332, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': 'fb68af006e2ecbc0'}}}