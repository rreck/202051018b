```json
{
  "id": "4e3121e8532f3135",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290867,
  "host_pid": "9e6742732c60:1",
  "hash": "494786a98c42549c600e5c72a2765992f1bc46e96935c767109fa784874d8716",
  "cid": "QmV1494786a98c42549c600e5c72a2765992f1bc46e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290867,
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
      "evaluated_at": 1760290867
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
  "sig": "a605372b45be0307b61f4d44ccf4d444df903e677caa0509c637d18eb6a4663b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034789126
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 50732457, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760284979, 'matching_hash': '5ec025bcbfaa0fd9'}}}