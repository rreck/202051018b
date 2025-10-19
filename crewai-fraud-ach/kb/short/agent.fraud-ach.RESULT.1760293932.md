```json
{
  "id": "afe177d8276ab2cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293932,
  "host_pid": "9e6742732c60:1",
  "hash": "74aaeb17232b55378b2f79106aad47876eb56b3e7d400a083fa5bc6848c915da",
  "cid": "QmV174aaeb17232b55378b2f79106aad47876eb56b3e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293932,
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
      "evaluated_at": 1760293932
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
  "sig": "8dad95e678d0aa0c1f3b24f10385cef0e866d1c98f8c69c468efda2fec2057b3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248710981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 58509588, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': '9a1c8fb9d78dcf4a'}}}