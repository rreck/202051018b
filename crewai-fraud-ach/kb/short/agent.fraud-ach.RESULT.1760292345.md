```json
{
  "id": "e43d11103d343ccc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292345,
  "host_pid": "9e6742732c60:1",
  "hash": "ddd862c1bbf765f7ab846525b95ff0e6b58a965b47ee1701f04033ed8b5dfdd2",
  "cid": "QmV1ddd862c1bbf765f7ab846525b95ff0e6b58a965b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292345,
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
      "evaluated_at": 1760292345
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
  "sig": "7716413c2ab71d2ef6c7f586ae74d57911b2012311019c7c100c56182c99f0ee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 62058360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}