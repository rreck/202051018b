```json
{
  "id": "e4813da1885d7ec8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292151,
  "host_pid": "9e6742732c60:1",
  "hash": "0a748ce54e473c4ca9707b53700669f23417e3fe4974009198f6b355c4c3820c",
  "cid": "QmV10a748ce54e473c4ca9707b53700669f23417e3fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292151,
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
      "evaluated_at": 1760292151
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
  "sig": "753c5574f9cf4d27f0e8d3f3c3e385697f69aa2a194efd3a85d17eaf8210efc7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466969713
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 59418954, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': '1e9180284a8352f5'}}}