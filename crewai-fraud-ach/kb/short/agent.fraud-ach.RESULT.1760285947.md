```json
{
  "id": "7ffe09951ea6d11f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285947,
  "host_pid": "9e6742732c60:1",
  "hash": "ec2b6240e942fa70b68217ac64e04c449a073c7b0592e23515db769f8cd12b82",
  "cid": "QmV1ec2b6240e942fa70b68217ac64e04c449a073c7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285947,
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
      "evaluated_at": 1760285947
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
  "sig": "a4f07675091e694aac23e8ffc864dd7c496862be7cb20b850dc7d13b2a630d4d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100276148173
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285765, 'matching_hash': 'f15677eba424e05f'}}}