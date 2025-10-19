```json
{
  "id": "cfc7c7bccf3e1d64",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291068,
  "host_pid": "9e6742732c60:1",
  "hash": "34d48746e9420d476a888119ccf2e2a5af19cd4f117fbd6da3f28791150a1488",
  "cid": "QmV134d48746e9420d476a888119ccf2e2a5af19cd4f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291068,
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
      "evaluated_at": 1760291068
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
  "sig": "1c4da58d03e3954927d9524cb99f06ee5cfccbcdbb50f3eedae61d19e5a3c6a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027783214
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 117413802, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760284979, 'matching_hash': '00d004b11e9e3015'}}}