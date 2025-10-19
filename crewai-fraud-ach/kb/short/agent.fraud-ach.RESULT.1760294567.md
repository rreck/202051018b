```json
{
  "id": "20cb0f3a7ead967e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294567,
  "host_pid": "9e6742732c60:1",
  "hash": "ad0260af937894015b89d6ab1c17165b3111978bad1bd0ebe75f7b3130554074",
  "cid": "QmV1ad0260af937894015b89d6ab1c17165b3111978b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294567,
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
      "evaluated_at": 1760294567
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
  "sig": "f1894c14a8ccd85114ebf5e4ea09524ae0f25a52d578f86cdb4b8e7c8aafc84c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462125361
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 42053040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285764, 'matching_hash': '410e2c6110d1d339'}}}