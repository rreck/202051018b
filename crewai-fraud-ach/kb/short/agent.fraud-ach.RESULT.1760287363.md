```json
{
  "id": "d40408944c2eefb6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287363,
  "host_pid": "9e6742732c60:1",
  "hash": "c6bdccbbcb45f6d5d814e3b45adcb7573b1b0ded0e13687c7209dc1fd7812d8b",
  "cid": "QmV1c6bdccbbcb45f6d5d814e3b45adcb7573b1b0ded",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287363,
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
      "evaluated_at": 1760287363
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "62d6ebf2b1bd0adf9e3719e76ca1683cce595a2752a3fbe51389422de22656aa"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000039495479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 23230008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285765, 'matching_hash': 'bbfd7bc59c80a282'}}}