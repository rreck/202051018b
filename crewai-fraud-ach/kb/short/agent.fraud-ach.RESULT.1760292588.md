```json
{
  "id": "3561564cf0b6b47a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292588,
  "host_pid": "9e6742732c60:1",
  "hash": "02043032685d2aee1a62a53a8e7acf45e5f090f4a330a92213f4acec02383126",
  "cid": "QmV102043032685d2aee1a62a53a8e7acf45e5f090f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292588,
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
      "evaluated_at": 1760292588
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
  "sig": "999a9d18307f902591362ca971ab67cc6ece69fcc830f01f95e16465a1c79734"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275563549
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 85421985, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': 'a33681b350a57503'}}}