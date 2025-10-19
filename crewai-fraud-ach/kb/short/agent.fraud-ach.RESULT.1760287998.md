```json
{
  "id": "0d014138be4bd5c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287998,
  "host_pid": "9e6742732c60:1",
  "hash": "e8322ea320012059820ecd02c8849103db323d7b240b5e170ae65761efa8d7cc",
  "cid": "QmV1e8322ea320012059820ecd02c8849103db323d7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287998,
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
      "evaluated_at": 1760287998
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
  "sig": "863671bca1435726a4b3a8115eb108a6989fb21ad9da01a7fcbec2b3b7b383e9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022785658
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 31783517, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285764, 'matching_hash': 'fafce013233f49bd'}}}