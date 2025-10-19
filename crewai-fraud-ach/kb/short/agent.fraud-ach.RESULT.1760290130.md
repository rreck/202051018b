```json
{
  "id": "2e617fd3bd67c1b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290130,
  "host_pid": "9e6742732c60:1",
  "hash": "4f2ce6177aa8203def65ca775bbd98fd9ddc67166878ff1740d56fc473d2e5fa",
  "cid": "QmV14f2ce6177aa8203def65ca775bbd98fd9ddc6716",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290130,
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
      "evaluated_at": 1760290130
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
  "sig": "5a1c991ff18e54521c2141bdaf92c53e0ec9681061efe2ca6bfab3fc39f6323a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467867880
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285765, 'matching_hash': 'd47cb9c035f50d52'}}}een': 1760285763, 'matching_hash': '760b7e67ac1502b4'}}}