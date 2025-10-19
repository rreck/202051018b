```json
{
  "id": "c2a39f3b7deb50f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288187,
  "host_pid": "9e6742732c60:1",
  "hash": "8bdf5ef98db20b35486a55a700d252e550ef6295895cecd119ed3efc1063a883",
  "cid": "QmV18bdf5ef98db20b35486a55a700d252e550ef6295",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288187,
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
      "evaluated_at": 1760288187
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
  "sig": "b9bdb163cbcae14859fd512693d23c782c286af1177cbfa5acb81ec05d9ef5f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597800882
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 17459595, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285765, 'matching_hash': 'e972b74e8fc22124'}}}