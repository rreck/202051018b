```json
{
  "id": "b702deb19c8796f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293617,
  "host_pid": "9e6742732c60:1",
  "hash": "0834a7e7f8593ce99b80bc10a8f0b52d6440bfef49a6f788ffea735471adb4b9",
  "cid": "QmV10834a7e7f8593ce99b80bc10a8f0b52d6440bfef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293617,
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
      "evaluated_at": 1760293617
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
  "sig": "d974b180827e659580124faf3ebd029b7bd01bafe06fccdf3478a74eca38da33"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594139699
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 102591750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '7ab15b33947f4722'}}}