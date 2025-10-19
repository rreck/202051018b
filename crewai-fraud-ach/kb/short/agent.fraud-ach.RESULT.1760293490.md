```json
{
  "id": "46709f18aa844b97",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293490,
  "host_pid": "9e6742732c60:1",
  "hash": "deb8bbddc49a7464f96df44bf075a0b6ee1a059c0b7b3f49b69c4b09e19cd114",
  "cid": "QmV1deb8bbddc49a7464f96df44bf075a0b6ee1a059c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293490,
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
      "evaluated_at": 1760293490
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
  "sig": "5e3982ef9736305eebd94a627091abaab3e943621b858a7498de9e6cb17ef0f3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 69696312, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}