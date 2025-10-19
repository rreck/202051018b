```json
{
  "id": "0d76c565da25f879",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291967,
  "host_pid": "9e6742732c60:1",
  "hash": "441e1961fbe7fc84f53835d264821d567faec0ced65b34bdc03de78135929d8b",
  "cid": "QmV1441e1961fbe7fc84f53835d264821d567faec0ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291967,
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
      "evaluated_at": 1760291967
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
  "sig": "4ef47912784778b9e0a7eea48896ac9d7502fad38eb4778397e2f6f6385e0765"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594081907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 92668598, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': 'b8f6a044d6b1da81'}}}