```json
{
  "id": "9e330fe6da8c3e70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291818,
  "host_pid": "9e6742732c60:1",
  "hash": "8c739d7ef77261e808c5e61168148621e6ea53b85a70a6bfd043c247434e0319",
  "cid": "QmV18c739d7ef77261e808c5e61168148621e6ea53b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291818,
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
      "evaluated_at": 1760291818
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
  "sig": "396a798682051e2cc7c1db610fb24c364b7d21f0ed328a878e5da10b6d157896"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156237747
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 14329184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': 'b60e159429465bd2'}}}