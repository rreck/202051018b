```json
{
  "id": "e2b3d2c32e9425bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290129,
  "host_pid": "9e6742732c60:1",
  "hash": "29050ab4304ef8c20acd848d83caa96dc51c86e7668ee347d42f78b41b10c6de",
  "cid": "QmV129050ab4304ef8c20acd848d83caa96dc51c86e7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290129,
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
      "evaluated_at": 1760290129
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
  "sig": "57a802f3ddbc8a5a70a2793e4eb772a57272ba6882cbe972c7703a27ba33b90c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245928241
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 48556332, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': '062a48cd408462a2'}}}