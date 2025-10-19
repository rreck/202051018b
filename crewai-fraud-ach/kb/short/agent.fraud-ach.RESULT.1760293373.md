```json
{
  "id": "b564b586e4805a44",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293373,
  "host_pid": "9e6742732c60:1",
  "hash": "7ec1a396312faaa197786e6c3c00a708d98a713ff4e5baf0b5a8704d91429a91",
  "cid": "QmV17ec1a396312faaa197786e6c3c00a708d98a713f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293373,
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
      "evaluated_at": 1760293373
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
  "sig": "d417e88fea1309c0cf5d66cd7cabd7e85d175f4a356cacea4026dadc380f7e54"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037120396
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 24526425, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '29cd45017b863efa'}}}