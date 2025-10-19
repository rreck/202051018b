```json
{
  "id": "33655562c0c50c93",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293410,
  "host_pid": "9e6742732c60:1",
  "hash": "11761dc9ef064aa79de37c7af29f81fdab91ebf3dea6afbf111f895ec33b5035",
  "cid": "QmV111761dc9ef064aa79de37c7af29f81fdab91ebf3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293410,
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
      "evaluated_at": 1760293410
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
  "sig": "08cdcd48440ec00dcc4db7754e4b417462a5f11025aba682217f70777f7fc0a5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028841300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 40751830, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': 'f5bed59f6c250fae'}}}