```json
{
  "id": "aba0ba6d3cfa5e9b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287615,
  "host_pid": "9e6742732c60:1",
  "hash": "c837361e6f915404766cae66107ea43881edf2bb7bff2e6944afe677d2962dfa",
  "cid": "QmV1c837361e6f915404766cae66107ea43881edf2bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287615,
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
      "evaluated_at": 1760287615
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
  "sig": "f08d07fe10306b223499294d4cf83425c36bba69c3879e01139fcaf3fe8c464e"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 122105155194168
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 24132570, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285765, 'matching_hash': '7ab74b64ae25594e'}}}