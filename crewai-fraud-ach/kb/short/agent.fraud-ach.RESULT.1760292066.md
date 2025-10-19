```json
{
  "id": "3585f770c6d5155b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292066,
  "host_pid": "9e6742732c60:1",
  "hash": "8d28c847b373d00b570b480bc8ca24a509ba557ff9f95120ac5c22edcbecd526",
  "cid": "QmV18d28c847b373d00b570b480bc8ca24a509ba557f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292066,
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
      "evaluated_at": 1760292066
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
  "sig": "cb6e21a5244eb8f8461c291f3fa8226dc15f5f53dfc0b5da9951a51a68dd6266"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157316048
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 47250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285764, 'matching_hash': '8f4887477877b00a'}}}