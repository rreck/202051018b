```json
{
  "id": "56dcab8c593670a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291481,
  "host_pid": "9e6742732c60:1",
  "hash": "169d05c249acf603086201d90c28a632b08acf079304c8988f69ad3d9a7a681a",
  "cid": "QmV1169d05c249acf603086201d90c28a632b08acf07",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291481,
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
      "evaluated_at": 1760291481
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
  "sig": "02f085fba3d2a4c70ebe2b1a3ebf96c619f56cc39626619f171066091e729466"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241906665
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 45618848, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285764, 'matching_hash': '6ca698820fae5f27'}}}