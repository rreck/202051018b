```json
{
  "id": "ed185b51331d15b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287716,
  "host_pid": "9e6742732c60:1",
  "hash": "1d9ca001a92a3a2e84c03f036f14ab9fa5e87b6398a10cb93f35ebd21a3ab2cc",
  "cid": "QmV11d9ca001a92a3a2e84c03f036f14ab9fa5e87b63",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287716,
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
      "evaluated_at": 1760287716
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
  "sig": "cc6504c7088fcfc291c45d873df9d39d8b300b626adfa7f0d884ea6b3e76ad99"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 121000248569332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 10415090, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285763, 'matching_hash': '521bb7eb391c7339'}}}