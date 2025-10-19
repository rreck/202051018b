```json
{
  "id": "2ea5b0b6bb6624a5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291888,
  "host_pid": "9e6742732c60:1",
  "hash": "157e2ae4e05d98d60260a32df08a1381e3da095c2410cdaf3ca1b980804692fa",
  "cid": "QmV1157e2ae4e05d98d60260a32df08a1381e3da095c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291888,
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
      "evaluated_at": 1760291888
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
  "sig": "c1ad97df52651e6fd82de1ae3256f72ff0cd012e3e2c0944322a5d5eda2939fd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596502557
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 20099140, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285764, 'matching_hash': 'c368684e8d9c7f24'}}}