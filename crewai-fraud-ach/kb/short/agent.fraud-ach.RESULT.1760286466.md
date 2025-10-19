```json
{
  "id": "5f34039c2cf48e90",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286466,
  "host_pid": "9e6742732c60:1",
  "hash": "7b73a6eb857b442d00c68396a13218abf3a0f7d34e17159da279e7773a244772",
  "cid": "QmV17b73a6eb857b442d00c68396a13218abf3a0f7d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286466,
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
      "evaluated_at": 1760286466
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
  "sig": "452f8f10ba5b297c7ee7c55d1791a050169df798b9339f8da5115ad8a277338f"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 044000033820068
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285763, 'matching_hash': 'f27958456f681c61'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}