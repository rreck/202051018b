```json
{
  "id": "e47c9766b5940b72",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287336,
  "host_pid": "9e6742732c60:1",
  "hash": "1c59c6477bae9250f5a15704f58bd60628ac062ed966e5d33e02a5755629abaf",
  "cid": "QmV11c59c6477bae9250f5a15704f58bd60628ac062e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287336,
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
      "evaluated_at": 1760287336
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "1ae85d9d55de58ec97fe9c817e53c35110a106fc186129697d0c3a309d218f77"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 56, 'threshold': 50, 'total_amount': 17821888, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}