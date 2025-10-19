```json
{
  "id": "cd2cdb93316c1745",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291187,
  "host_pid": "9e6742732c60:1",
  "hash": "52d8fcdfb6400dcc117f4d00447bf662de5682ec91b0e47b20c735fc18ca2305",
  "cid": "QmV152d8fcdfb6400dcc117f4d00447bf662de5682ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291187,
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
      "evaluated_at": 1760291187
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
  "sig": "b5679287087b293aefd834701b70a3d0ed47d5ff9938ed1aecac8e01a5b7c508"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028017264
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 76844807, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285763, 'matching_hash': '707a4137bac9b143'}}}