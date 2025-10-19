```json
{
  "id": "fe61a0c8a2626cad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294201,
  "host_pid": "9e6742732c60:1",
  "hash": "30838749c2478110592c02a149137ead084a1d16e04f2d85fcc158c9ad272a56",
  "cid": "QmV130838749c2478110592c02a149137ead084a1d16",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294201,
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
      "evaluated_at": 1760294201
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
  "sig": "4e2b2a7910113b63c75e060747784a16b852784891f9df69161f19eb2947b77c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025840854
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 97890523, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285765, 'matching_hash': 'de322b9b0535588e'}}}