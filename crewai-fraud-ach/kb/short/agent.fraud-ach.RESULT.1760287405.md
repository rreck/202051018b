```json
{
  "id": "03334fcc65e56547",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287405,
  "host_pid": "9e6742732c60:1",
  "hash": "349b79529acf20f6590e27e038cc2d93225ad1968cbfb3071aa385a7aeb7db48",
  "cid": "QmV1349b79529acf20f6590e27e038cc2d93225ad196",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287405,
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
      "evaluated_at": 1760287405
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
  "sig": "1f62588f902e428f240bb4da2eec0332cf3ffe692043f208309abf43b9188048"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201465236749
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 14269563, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285764, 'matching_hash': '3442ebeb280b968f'}}}