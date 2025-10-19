```json
{
  "id": "c09fc45047bc04e3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287225,
  "host_pid": "9e6742732c60:1",
  "hash": "de572931f784ac0ccfc22b3f631ac70e69cf527ba0eb6de5d76d5b43bb197ead",
  "cid": "QmV1de572931f784ac0ccfc22b3f631ac70e69cf527b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287225,
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
      "evaluated_at": 1760287225
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
  "sig": "997fb284359d32af8b4c104dad2ee0bf3126dd00c9aa029539be4651672d7415"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 16548896, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}