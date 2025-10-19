```json
{
  "id": "592f87678737881d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287701,
  "host_pid": "9e6742732c60:1",
  "hash": "6b83a74332deb698f0a63d08784956c33fc39b14f38cbc181ce562c15cbc121d",
  "cid": "QmV16b83a74332deb698f0a63d08784956c33fc39b14",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287701,
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
      "evaluated_at": 1760287701
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
  "sig": "1df3e2c1c0ad0fb61da80c95c6205327bde495e3d2935ee44705ba05faaf1907"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 122105154242410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285765, 'matching_hash': '26a9af32f02bfdfc'}}}