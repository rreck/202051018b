```json
{
  "id": "72056332a3938e8d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288585,
  "host_pid": "9e6742732c60:1",
  "hash": "0de2a68ca0c8be1f3a40b0d4d802f7a5451cc6e6bbeb939d02a8af5d940810dc",
  "cid": "QmV10de2a68ca0c8be1f3a40b0d4d802f7a5451cc6e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288585,
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
      "evaluated_at": 1760288585
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
  "sig": "4a0d7208fddab477835e861538383b618da3c01252f2ccc8e1cad653057f5595"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030232602
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285763, 'matching_hash': '54bba9b5de699774'}}}een': 1760285763, 'matching_hash': 'cfffbd2ec30a8ce4'}}}