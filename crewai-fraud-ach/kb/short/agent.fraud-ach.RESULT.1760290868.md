```json
{
  "id": "a6a97bd0a3364794",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290868,
  "host_pid": "9e6742732c60:1",
  "hash": "e27870445df4bf819776a07380aecd16d27b8305a82a6f6798bdecfa14e04114",
  "cid": "QmV1e27870445df4bf819776a07380aecd16d27b8305",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290868,
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
      "evaluated_at": 1760290868
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
  "sig": "2de5dd809f48a650a3c8a1f113b0819f4d9adc0f28398ada108fdf99d4493ea2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596811195
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 35507423, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285765, 'matching_hash': '0f37bc2cbfa5aec6'}}}