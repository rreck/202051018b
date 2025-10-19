```json
{
  "id": "7e1268d3a514a79e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294731,
  "host_pid": "9e6742732c60:1",
  "hash": "40a14dac46eca362048c94c78bb588c0f61183a3a89b84593175ea8777f7f8df",
  "cid": "QmV140a14dac46eca362048c94c78bb588c0f61183a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294731,
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
      "evaluated_at": 1760294731
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
  "sig": "bd733354fd05c5bb86ff5b54f7faaaf14cd5e5054ec0f70d5de80e374e4a0f99"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020807792
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 50726493, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285764, 'matching_hash': '8390351bce6e669b'}}}