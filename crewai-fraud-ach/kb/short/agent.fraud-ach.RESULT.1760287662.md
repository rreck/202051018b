```json
{
  "id": "4417cca8e320b159",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287662,
  "host_pid": "9e6742732c60:1",
  "hash": "3242338fdc93ea2d38c5e2b5bdde6c3fb511c39d78452887f5c2dac45e4877c5",
  "cid": "QmV13242338fdc93ea2d38c5e2b5bdde6c3fb511c39d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287662,
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
      "evaluated_at": 1760287662
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
  "sig": "1277ba8d275d4417c121bf21b1ab49862a47c239e433e000f48255801ce25a73"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000024763111
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 13661404, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285764, 'matching_hash': '9fa093ca4f14e7a1'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '051442869', 'validation_error': 'Invalid routing number checksum'}}}