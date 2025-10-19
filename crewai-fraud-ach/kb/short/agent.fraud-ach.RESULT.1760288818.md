```json
{
  "id": "c32caa402ced094b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288818,
  "host_pid": "9e6742732c60:1",
  "hash": "4d7f1352a7ca713362c0079239b30f8fb68c4f37eee94d0a348d8d030aa892fb",
  "cid": "QmV14d7f1352a7ca713362c0079239b30f8fb68c4f37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288818,
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
      "evaluated_at": 1760288818
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
  "sig": "b70a17c19276d9e488066bfdd66b40614cf1bffb12f7ce101cdc5cc3422fd702"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595770141
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285763, 'matching_hash': '07c751792fcc9457'}}}een': 1760285764, 'matching_hash': '6ca698820fae5f27'}}}