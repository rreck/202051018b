```json
{
  "id": "4b87f2982016bfb9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287489,
  "host_pid": "9e6742732c60:1",
  "hash": "597559eafbba4cbd0f36589928095522a06c17ea30653647fa341fda3c56a890",
  "cid": "QmV1597559eafbba4cbd0f36589928095522a06c17ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287489,
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
      "evaluated_at": 1760287489
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
  "sig": "bdc1e1e6b1bce3dc52bbda2ced1e6a1788d8e9f6171d15f16e1ed5f7e499d603"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 122105152451584
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50, 'total_amount': 24634522, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285763, 'matching_hash': '0001f0028f567562'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8052182}}}