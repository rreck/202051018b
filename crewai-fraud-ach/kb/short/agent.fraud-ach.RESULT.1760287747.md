```json
{
  "id": "ad53c6d070a11baa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287747,
  "host_pid": "9e6742732c60:1",
  "hash": "deb92994082777227322e25e8b0a8c9deeb502e2423110c460b9e87109d0a5cd",
  "cid": "QmV1deb92994082777227322e25e8b0a8c9deeb502e2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287747,
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
      "evaluated_at": 1760287747
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
  "sig": "13b2a8bf41874145a9d19a29d74aba50ff05577dc6cc8285e709d48ea240b888"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 031201464121559
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 32219303, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285763, 'matching_hash': '1ddc8562b5a9ecf0'}}}: {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7209366}}}