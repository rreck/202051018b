```json
{
  "id": "0c9dd99fd272fef4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293634,
  "host_pid": "9e6742732c60:1",
  "hash": "81275dc86c8b561f65af2bcc3b34320ebd6a58bb4599959eca263b6c3543901d",
  "cid": "QmV181275dc86c8b561f65af2bcc3b34320ebd6a58bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293634,
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
      "evaluated_at": 1760293634
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
  "sig": "2f6f11704bbbba4d4ebf80c03dbe178db34a837b74ddeb0199f958cb6d5c90af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025503816
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 87068400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285765, 'matching_hash': 'fc6cd7074b4844e3'}}}