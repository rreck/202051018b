```json
{
  "id": "778320e84b71764e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287658,
  "host_pid": "9e6742732c60:1",
  "hash": "f14006dd422b5f7a430facb1ca22494410b91386ab2cfb21dbb996db26c73e6e",
  "cid": "QmV1f14006dd422b5f7a430facb1ca22494410b91386",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287658,
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
      "evaluated_at": 1760287658
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
  "sig": "fa68a5739c91b583b9a4756968022ca8a28619f3421069ec914acfa42f23bbac"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000030152104
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 19781676, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285763, 'matching_hash': 'f9baa0480a932ad2'}}}: {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7365830}}}