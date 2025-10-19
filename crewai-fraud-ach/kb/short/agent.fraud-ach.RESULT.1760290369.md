```json
{
  "id": "c73f374c788ca999",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290369,
  "host_pid": "9e6742732c60:1",
  "hash": "42498a1d27080828bc052821b739edc0843c507942b01734334bd17178ec5dae",
  "cid": "QmV142498a1d27080828bc052821b739edc0843c5079",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290369,
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
      "evaluated_at": 1760290369
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
  "sig": "cd6b13f099494dfc45be555076bca4737a3afe63fcfc4c94175ac0d3fd5ca4f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 47100704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}