```json
{
  "id": "082a97b136ce88a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292467,
  "host_pid": "9e6742732c60:1",
  "hash": "fb9c3c4e585a4766ce0ebfb765865d501b4dfb0660e3e319d1981bacc22a9cd0",
  "cid": "QmV1fb9c3c4e585a4766ce0ebfb765865d501b4dfb06",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292467,
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
      "evaluated_at": 1760292467
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
  "sig": "211f471eb6342263f499bb1789f9f7d6611cf04464ba9bc7bc2df244894f24c2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460216158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 274, 'threshold': 50, 'total_amount': 72351892, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 273, 'first_seen': 1760284979, 'matching_hash': 'd03ac62e4cd65436'}}}