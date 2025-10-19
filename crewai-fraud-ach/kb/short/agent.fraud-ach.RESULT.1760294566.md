```json
{
  "id": "a6ee3a48e7c2e3e7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294566,
  "host_pid": "9e6742732c60:1",
  "hash": "d0cc1a8f8f2d3637058ea3bb2ce72debde8a5c118bc3b8941fe4cc6c131c6093",
  "cid": "QmV1d0cc1a8f8f2d3637058ea3bb2ce72debde8a5c11",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294566,
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
      "evaluated_at": 1760294566
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
  "sig": "43bb27aeb8e1c8cc51cbfcc6e1341123c775fedf3643b993dee74d8a531b405e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153312612
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 24000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': 'b6b1aeb6185e45bf'}}}