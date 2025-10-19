```json
{
  "id": "f5e844ba42d8bf87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287704,
  "host_pid": "9e6742732c60:1",
  "hash": "6fbe3a69a428af926b2f9edb01810d0cc914aecf97a004e0540dcdaff08d16b2",
  "cid": "QmV16fbe3a69a428af926b2f9edb01810d0cc914aecf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287704,
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
      "evaluated_at": 1760287704
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
  "sig": "e2e3cf682fc54134abe9453b3e54549250c4e1576e88bc912c6a3ec655dec879"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 031201462408143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 33550077, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285765, 'matching_hash': '36407d3e627869a5'}}}