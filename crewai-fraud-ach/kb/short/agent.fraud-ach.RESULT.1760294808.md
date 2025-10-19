```json
{
  "id": "a48f67888b11e368",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294808,
  "host_pid": "9e6742732c60:1",
  "hash": "bc27a45f81d0fd08538603adfe2e3cff3573047fed768c6ad810ce8e7d175b2a",
  "cid": "QmV1bc27a45f81d0fd08538603adfe2e3cff3573047f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294808,
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
      "evaluated_at": 1760294808
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
  "sig": "de45fa08964b072f59dddca76ce3dc467130f5a27abb340cc17b7b241587268c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466882033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 73397590, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': '7e4548b1f8f2bba3'}}}