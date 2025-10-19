```json
{
  "id": "e1a6d68219bf41fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293869,
  "host_pid": "9e6742732c60:1",
  "hash": "69013ad47781886a8c8f8834f349f964c8a00e22d5387fb75ac7426c43957728",
  "cid": "QmV169013ad47781886a8c8f8834f349f964c8a00e22",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293869,
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
      "evaluated_at": 1760293869
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
  "sig": "9b702d51b3f140d1c007f6cada35ccb424a76bfad51e3d1141d0a2244e1eeaac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596367142
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 102845074, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '4f1a5a8d43b99e0b'}}}