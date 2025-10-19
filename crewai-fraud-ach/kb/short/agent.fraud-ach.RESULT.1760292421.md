```json
{
  "id": "5275ac1d33a631c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292421,
  "host_pid": "9e6742732c60:1",
  "hash": "0360bda9bbdf3a8d4499aa5e0fb457258909b60d18640e783c7b886c241363e8",
  "cid": "QmV10360bda9bbdf3a8d4499aa5e0fb457258909b60d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292421,
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
      "evaluated_at": 1760292421
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
  "sig": "5074094948243dd065e264779879d3aec9b16f92e0630e021d61a31227d660a7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022844283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 273, 'threshold': 50, 'total_amount': 51426375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 272, 'first_seen': 1760284979, 'matching_hash': '9c963f39e9fb9122'}}}