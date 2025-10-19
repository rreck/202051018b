```json
{
  "id": "b2beb72559d61d2a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289685,
  "host_pid": "9e6742732c60:1",
  "hash": "c9b739f0642f7dc83678e42b5c23969a062a6ecaa3811eb3fc97a592e10cd504",
  "cid": "QmV1c9b739f0642f7dc83678e42b5c23969a062a6eca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289685,
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
      "evaluated_at": 1760289685
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
  "sig": "8b2cdf60d145b5f6460634d6feccf3e54643a27c6dc49be8607531b915961bb9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020380567
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 36718110, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285764, 'matching_hash': 'ee2651561ec204b1'}}}