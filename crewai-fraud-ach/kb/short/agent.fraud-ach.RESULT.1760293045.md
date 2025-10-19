```json
{
  "id": "06fc0f2e6ad164d9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293045,
  "host_pid": "9e6742732c60:1",
  "hash": "e89d3acc30794b2c5f3127d0fbcb5cfaef2e531c734f1c8028aa396fb69c9c6d",
  "cid": "QmV1e89d3acc30794b2c5f3127d0fbcb5cfaef2e531c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293045,
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
      "evaluated_at": 1760293045
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
  "sig": "207c8b50e196904e25347b54e92f865aa69999d8700a87463b16b92e3d321291"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029964192
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 63715050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285764, 'matching_hash': '3fa9c762fe00e5a2'}}}