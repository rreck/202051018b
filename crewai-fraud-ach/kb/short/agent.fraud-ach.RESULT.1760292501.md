```json
{
  "id": "a2fd859e99ad677e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292501,
  "host_pid": "9e6742732c60:1",
  "hash": "64a68f70ab6fe2086dff9f98a3755201cc7ba4ae8b2052ffae04e5a2bde51e35",
  "cid": "QmV164a68f70ab6fe2086dff9f98a3755201cc7ba4ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292501,
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
      "evaluated_at": 1760292501
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "ff4899dfddd57b9f11f93ecf964a2df7bac42dd116da3ed2cfa2eed766132281"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000245827798
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 99500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': '00b0e4c8ffd2abdb'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}routing number checksum'}}}