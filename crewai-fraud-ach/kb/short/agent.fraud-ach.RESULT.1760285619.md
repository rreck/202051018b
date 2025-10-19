```json
{
  "id": "89929e15be34e030",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285619,
  "host_pid": "9e6742732c60:1",
  "hash": "690003f446dc236f7ce53d203f06a7ba68dac14341a1d566eab475f06b23700c",
  "cid": "QmV1690003f446dc236f7ce53d203f06a7ba68dac143",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285619,
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
      "evaluated_at": 1760285619
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
  "sig": "dff3faec3529829657e233fe99cd117b8d74c9bf100df315409a9c4b1e6be619"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 26547822, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}