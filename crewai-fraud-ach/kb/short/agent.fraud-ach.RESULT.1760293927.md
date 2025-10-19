```json
{
  "id": "44d790dff24f9bd9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293927,
  "host_pid": "9e6742732c60:1",
  "hash": "5cc79bcfca2300ca5e557034c5fb74572a5b72f6daad4eecbe5215f638d8b120",
  "cid": "QmV15cc79bcfca2300ca5e557034c5fb74572a5b72f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293927,
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
      "evaluated_at": 1760293927
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
  "sig": "097514a477a1cdfe89209e7e2d4f737d815deaea72ba16c48ed440e82de0868c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272560065
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 304, 'threshold': 50, 'total_amount': 34739296, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 303, 'first_seen': 1760284979, 'matching_hash': 'aab4f056297a675d'}}}