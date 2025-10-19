```json
{
  "id": "238ff7bf0bd03a04",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290406,
  "host_pid": "9e6742732c60:1",
  "hash": "7d2067de410a9f91271c24267d367b86f7091a469f5367a8c6717e10b51a3643",
  "cid": "QmV17d2067de410a9f91271c24267d367b86f7091a46",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290406,
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
      "evaluated_at": 1760290406
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
  "sig": "be780e912ba01abdd20423e84c7c132c776a62aecc20ce938952f3ffb88126b0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249254910
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 17015502, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285765, 'matching_hash': '80dc97a16e454830'}}}