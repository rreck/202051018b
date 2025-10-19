```json
{
  "id": "813c00bc5ed3e0fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287607,
  "host_pid": "9e6742732c60:1",
  "hash": "02453932395bfda817ecb9dafeec0f2e7c1009c56f0e856318d643011a58abb5",
  "cid": "QmV102453932395bfda817ecb9dafeec0f2e7c1009c5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287607,
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
      "evaluated_at": 1760287607
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
  "sig": "6f88906e94acf066990491f4cd95a99fbab8d1973fec5c20433ca29e7cb8a31e"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 021000023367694
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 27680070, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285763, 'matching_hash': '23afc27b7b9a7115'}}}}}}