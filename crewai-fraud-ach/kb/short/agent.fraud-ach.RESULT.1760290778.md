```json
{
  "id": "2f05597b1d0cf58a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290778,
  "host_pid": "9e6742732c60:1",
  "hash": "7a9a51345f791eae5fcd17abb1dcbfad77fc41233da37cd007cea54e1f35dcdd",
  "cid": "QmV17a9a51345f791eae5fcd17abb1dcbfad77fc4123",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290778,
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
      "evaluated_at": 1760290778
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
  "sig": "cc33b0a9727602ddf97ab259ae238a3086505c9ba10e0ef2e74aa115d575c263"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023390591
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 49767636, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285764, 'matching_hash': '65b6a0d7e3017724'}}}