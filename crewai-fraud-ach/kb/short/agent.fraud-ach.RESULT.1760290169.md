```json
{
  "id": "1bf38887ac558308",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290169,
  "host_pid": "9e6742732c60:1",
  "hash": "f8e235ae2bd2a4463425766942b2a0656c1a259725ed15a528d728c40c0582e2",
  "cid": "QmV1f8e235ae2bd2a4463425766942b2a0656c1a2597",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290169,
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
      "evaluated_at": 1760290169
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
  "sig": "e920e9d4060e398dd9de0d376256f6861f40ed1be2fa3c206d45ad75e821fbc9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243340063
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 60615126, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': '5f2724e98c8a67b0'}}}