```json
{
  "id": "4aa301320641935d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290098,
  "host_pid": "9e6742732c60:1",
  "hash": "45668f651c0243864568aa135453d945fb6535f00927be670204043bdd4ec820",
  "cid": "QmV145668f651c0243864568aa135453d945fb6535f0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290098,
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
      "evaluated_at": 1760290098
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
  "sig": "227d94ad1e44cdac4162b22e17fe91e96367d38b4c931488ca5be0b38446de98"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247533282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 21149718, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285765, 'matching_hash': '15ae64209d1fefcb'}}}