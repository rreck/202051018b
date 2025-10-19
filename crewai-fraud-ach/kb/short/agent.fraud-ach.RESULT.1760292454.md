```json
{
  "id": "441ebc49055894fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292454,
  "host_pid": "9e6742732c60:1",
  "hash": "798daeba08c298e1cbacb11258e70d6e3a9900283a089874cc82897ba67db990",
  "cid": "QmV1798daeba08c298e1cbacb11258e70d6e3a990028",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292454,
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
      "evaluated_at": 1760292454
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
  "sig": "8cc994b214a46bcfa8a6d610192c945fca4a0958cadb6d93e9499fab43d2935a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025820321
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 51047964, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': 'cf65bb25527720c5'}}}