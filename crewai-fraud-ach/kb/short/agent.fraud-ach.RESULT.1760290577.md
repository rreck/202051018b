```json
{
  "id": "65685e35097aee3a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290577,
  "host_pid": "9e6742732c60:1",
  "hash": "ad1275eab9fe6ebf39803e6707548330c5ddec4bf55b308aa451973ac60e79ab",
  "cid": "QmV1ad1275eab9fe6ebf39803e6707548330c5ddec4b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290577,
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
      "evaluated_at": 1760290577
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
  "sig": "df0be2857f86f22edce03b962160097de25835efe67343815a09607a64ededed"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241647784
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 16929836, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': '5747783cddc76b25'}}}