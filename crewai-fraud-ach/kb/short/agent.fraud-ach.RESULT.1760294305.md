```json
{
  "id": "709d050a01ce9db2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294305,
  "host_pid": "9e6742732c60:1",
  "hash": "c3f7041096d0fa6b8ed056da2af45516dcb2bd86f4d7d791297ff1118a69be46",
  "cid": "QmV1c3f7041096d0fa6b8ed056da2af45516dcb2bd86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294305,
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
      "evaluated_at": 1760294305
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
  "sig": "742df20f284c476a9eaa86c1ec13ed1c5b1a6c7c693b24ceff836efa4a971655"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593711033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 65004995, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285765, 'matching_hash': 'a63e704272eccc25'}}}