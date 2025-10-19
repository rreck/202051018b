```json
{
  "id": "ebf8cdebae4d710e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292014,
  "host_pid": "9e6742732c60:1",
  "hash": "cb4088f9f3835c7e97c68847494079dad365e567f11b92b0ada138820866cfba",
  "cid": "QmV1cb4088f9f3835c7e97c68847494079dad365e567",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292014,
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
      "evaluated_at": 1760292014
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
  "sig": "925107cf3a938745fb9f3ee451ae4defe3c16a69d74997207a7dbf846d91e64a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023458666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 264, 'threshold': 50, 'total_amount': 107725992, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 263, 'first_seen': 1760284979, 'matching_hash': 'a7fb9dc83800d725'}}}