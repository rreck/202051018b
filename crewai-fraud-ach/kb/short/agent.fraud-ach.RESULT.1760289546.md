```json
{
  "id": "7178202d36bf7108",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289546,
  "host_pid": "9e6742732c60:1",
  "hash": "de5513aea887f4cb77b0de1ab62533ead1ab58f3974682b610b14a7f9652c1c2",
  "cid": "QmV1de5513aea887f4cb77b0de1ab62533ead1ab58f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289546,
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
      "evaluated_at": 1760289546
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
  "sig": "b78fe65bbbc79eb0d961767b3eaeb4c030c3f21559250cd77146bccded093bf5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591362197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 50735664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': 'b2660329f17701b7'}}}