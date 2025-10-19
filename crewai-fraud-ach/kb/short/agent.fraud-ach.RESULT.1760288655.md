```json
{
  "id": "5c0853fbf35c4880",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288655,
  "host_pid": "9e6742732c60:1",
  "hash": "72dbfa3e50c85fa4675a875f0a584b3d778adfcf5e09b42ae811bd904846e63a",
  "cid": "QmV172dbfa3e50c85fa4675a875f0a584b3d778adfcf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288655,
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
      "evaluated_at": 1760288655
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "8ee1a807b3a49bdea8c7474da8782da86ee0a407ff4ca35d1ffb61b4278bcbf6"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000240623413
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 50000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285764, 'matching_hash': 'b41427cac750dd0e'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}