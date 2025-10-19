```json
{
  "id": "c1d1ce75779a9acb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294221,
  "host_pid": "9e6742732c60:1",
  "hash": "8cd5e7960a40f203fafdc84554b55a07ce65088e7093b5b02bf464e8e4ab94d3",
  "cid": "QmV18cd5e7960a40f203fafdc84554b55a07ce65088e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294221,
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
      "evaluated_at": 1760294221
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
  "sig": "91bf32540fbe7df123feb8ce62ecbfa75beecd30976d3b7d0ce4dafe29bb071b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031959136
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 18021042, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': 'f67377943b0624b0'}}}